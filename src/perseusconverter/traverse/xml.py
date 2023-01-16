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
"""Common traverser interface.
The purpose of a traverser is to traverse a Greek PDL TEI2 file in an ordered manner."""
import os
import re
from abc import abstractmethod
from pathlib import PurePath
from typing import Tuple

from lxml.etree import Element, parse

from greektextify.text.bracket import Bracketing
from greektextify.text.heard import GreekHeard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.unheard import GreekUnheard
from greektextify.text.word import GreekWord
from perseusconverter.traverse.traverser import AbstractTraverser


class AbstractXmlTraverser(AbstractTraverser):

    SKIP_TAGS = ('note', 'foreign', 'bibl', 'del')

    def __init__(self, path: PurePath, ignore: Tuple[str]):
        tokenizer = Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ])
        AbstractTraverser.__init__(self, tokenizer, path)
        self._filename = path.name
        self._ignore = ignore
        self._fd = open(str(path))
        self._tree = parse(self._fd)
        self._root = self._tree.getroot()
        self._id = list()
        self._hierarchy = None

        if self.format == "TEI.2":
            self._get_id()
            self._build_hier()

    @property
    def format(self) -> str:
        return self._root.tag

    @property
    def hierarchy(self) -> str:
        return self._hierarchy

    @property
    def root(self) -> Element:
        return self._root

    def traverse(self):
        self._traverse(self._root[1])

    @abstractmethod
    def general(self, xml: Element, skip: bool):
        return NotImplemented()

    def _do_skip(self, xml: Element) -> bool:
        path = self._tree.getpath(xml).strip()
        skip = xml.tag if xml.tag in self.SKIP_TAGS else ''
        return path.find(skip) or path in self._ignore

    def _clean_xpath(self, xml: Element) -> str:
        return re.sub(r"\[\d+\]", '', self._tree.getpath(xml))

    def _get_id(self):
        for tid in self._root.xpath("text[1]"):
            if "id" in tid.attrib.keys():
                self._id.append(tid.attrib["id"])

    def _build_hier(self):
        ref = self._tree.getroot().find("teiHeader/encodingDesc/refsDecl[1][@doctype='TEI.2']")
        units = list()
        if ref is not None:
            for state in ref.iterfind("state"):
                units.append(state.attrib['unit'])
            self._hierarchy = "-".join(units)

    def _traverse(self, xml: Element, in_skip: bool = False):
        self.general(xml, in_skip)
        in_skip = in_skip if not self._do_skip(xml) else True
        for el in xml:
            self._traverse(el, in_skip)
