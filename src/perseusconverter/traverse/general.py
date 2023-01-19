#
# Copyright (c) 2022 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
#
# Permission to use, copy, modify, and/or distribute this software for any purpose with
# or without fee is hereby granted, provided that the above copyright notice and this
# permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
# THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
#     https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC
#
# Contributors:
#     Kristoffer Paulsson - initial implementation
#
"""General traverser without specific purpose."""
from pathlib import PurePath
from typing import List, Tuple

from lxml.etree import Element, parse, ElementTree

from greektextify.nlp.contextual import ContextObject, NlpOperation
from greektextify.text.bracket import Bracketing
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.standardize import Standardize
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord
from perseusconverter.traverse.xml import AbstractXmlTraverser


class AbstractTeiTraverser(AbstractXmlTraverser, ContextObject):

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractXmlTraverser.__init__(self, path, tree, tokenizer)
        ContextObject.__init__(self)

        self._hierarchy_init()

    def _hierarchy_init(self):
        pass

    def _hierarchy_update(self, xml: Element):
        pass

    def general(self, xml: Element, skip: bool):
        pass

    @staticmethod
    def open(filename: PurePath) -> "AbstractTeiTraverser":
        tree = None
        with open(str(filename)) as fd:
            tree = parse(fd)

        root = tree.getroot()

        tokenizer = Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
        ])

        if root.tag == "TEI.2":
            return Tei2Traverser(filename, tree, tokenizer)
        elif root.tag == "{http://www.tei-c.org/ns/1.0}TEI":
            return Tei1Traverser(filename, tree, tokenizer)
        else:
            raise ValueError("Xml is not a valid TEI format! {}".format(root.tag))


class Tei1Traverser(AbstractTeiTraverser):
    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractTeiTraverser.__init__(self, path, tree, tokenizer)

    def _hierarchy_init(self):
        raise NotImplemented

    def _hierarchy_update(self, xml: Element):
        raise NotImplemented

    def general(self, xml: Element, skip: bool):
        raise NotImplemented


class Tei2Traverser(AbstractTeiTraverser):

    SKIP_TAGS = ('note', 'foreign', 'bibl', 'del')

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractTeiTraverser.__init__(self, path, tree, tokenizer)
        self._id = list()
        self._get_id()

    def _get_id(self):
        for tid in self._root.xpath("text[1]"):
            if "id" in tid.attrib.keys():
                self._id.append(tid.attrib["id"])

    def _hierarchy_init(self):
        ref = self._tree.getroot().find("teiHeader/encodingDesc/refsDecl[1][@doctype='TEI.2']")
        # ref = self._root.find("teiHeader/encodingDesc/refsDecl[@doctype='TEI.2']")
        units = list()
        if ref is not None:
            for state in ref.iterfind("state"):
                units.append(state.attrib['unit'])
            self._hierarchy = ("-".join(units), tuple(units), dict())

    def _hierarchy_update(self, xml: Element):
        if "type" in xml.attrib.keys():
            unit = xml.attrib["type"].lower()  # if xml.tag != "l" else "line"
            if unit in self._hierarchy[1]:
                num = xml.attrib["n"] if 'n' in xml.attrib else 'n/a'
                self._hierarchy[2][unit] = num

    def general(self, xml: Element, skip: bool):
        if not isinstance(xml.tag, str) or skip:
            return
        if self._do_skip(xml):
            if xml.text:
                self._tokenize(xml.tail, xml)
        else:
            self._tokenize(xml.text, xml)
            self._tokenize(xml.tail, xml)

    @NlpOperation()
    def _tokenize(self, text: str, e: Element) -> List[str]:
        if text is not None:
            std = Standardize.pdl(text.strip())
            if std != '':
                print(self._hierarchy)
                tokens = self._tokenizer.tokenize(std)
                for token in tokens:
                    if len(token) > 1:
                        print(GreekWord.glyphen(token))
                print(tokens)
