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
from typing import List

from lxml.etree import Element, parse, ElementTree, QName

from greektextify.beta.punctuation import BetaPunctuation
from greektextify.beta.word import BetaWord
from greektextify.nlp.contextual import ContextObject, NlpOperation
from greektextify.text.bracket import Bracketing
from greektextify.nlp.detoken import Detokenizer
from greektextify.text.pdl_standard import PdlUtfStandard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.beta.pdl_standard import PdlBetaStandard
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord
from perseusconverter.traverse.xml import AbstractXmlTraverser


class AbstractTeiTraverser(AbstractXmlTraverser, ContextObject):

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractXmlTraverser.__init__(self, path, tree, tokenizer)
        ContextObject.__init__(self)

        self._hierarchy_init()

    def _hierarchy_init(self):
        self._hierarchy = ("", list(), dict())

    def _hierarchy_update(self, xml: Element):
        keys = xml.attrib.keys()
        if "type" in keys:
            unit = xml.attrib.get("type").lower()
            num = xml.attrib["n"] if 'n' in xml.attrib else 'n/a'
            if unit == "textpart" and "subtype" in keys:
                unit = xml.attrib.get("subtype").lower()

            if unit not in self._hierarchy[1]:
                self._hierarchy[1].append(unit)
                self._hierarchy[2][unit] = num
            else:
                self._hierarchy[2][unit] = num

    @staticmethod
    def utf_tokenizer():
        return Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ], PdlUtfStandard())

    @staticmethod
    def beta_tokenizer():
        return Tokenize([
            BetaWord,  # GreekWord,
            Bracketing,
            BetaPunctuation,  # GreekPunctuation,
            GreekQuotation,
            Spacing,
        ], PdlBetaStandard())

    @staticmethod
    def open(filename: PurePath) -> "AbstractTeiTraverser":
        tree = None
        with open(str(filename)) as fd:
            tree = parse(fd)

        root = tree.getroot()

        tokenizer = AbstractTeiTraverser.beta_tokenizer()

        tag = QName(root).localname
        if tag == "TEI.2":
            return Tei2Traverser(filename, tree, tokenizer)
        elif tag == "TEI":
            return Tei1Traverser(filename, tree, tokenizer)
        else:
            raise ValueError("Xml is not a valid TEI format! {}".format(tag))


class Tei1Traverser(AbstractTeiTraverser):

    SKIP_TAGS = ('note', 'foreign', 'bibl', )  # 'del')

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractTeiTraverser.__init__(self, path, tree, tokenizer)

    def do_text(self, xml: Element):
        self._tokenize(xml.text, xml)

    def do_tail(self, xml: Element):
        self._tokenize(xml.tail, xml)

    @NlpOperation()
    def _tokenize(self, text: str, e: Element) -> List[str]:
        if text is not None:
            std = self._tokenizer.standardize(text.strip())
            if std != '':
                # print(self._hierarchy)
                tokens = self._tokenizer.tokenize(std)
                print(tokens)
                # for token in tokens:
                #    if len(token) > 1:
                #        print(token, Detokenizer.build_word(BetaWord.glyphen(token)))
                # print(tokens)


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

    """def _hierarchy_init(self):
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
                self._hierarchy[2][unit] = num"""

    def do_text(self, xml: Element):
        self._tokenize(xml.text, xml)

    def do_tail(self, xml: Element):
        self._tokenize(xml.tail, xml)

    @NlpOperation()
    def _tokenize(self, text: str, e: Element) -> List[str]:
        if text is not None:
            std = self._tokenizer.standardize(text.strip())
            if std != '':
                # print(self._hierarchy)
                tokens = self._tokenizer.tokenize(std)
                print(tokens)
                # for token in tokens:
                #    if len(token) > 1:
                #        print(token, Detokenizer.build_word(BetaWord.glyphen(token)))
                # print(tokens)
