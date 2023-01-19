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
import re
from abc import abstractmethod
from pathlib import PurePath
from typing import Tuple, List, Dict

from lxml.etree import Element, ElementTree

from greektextify.text.token import Tokenize
from perseusconverter.traverse.traverser import AbstractTraverser


class AbstractXmlTraverser(AbstractTraverser):

    SKIP_TAGS = tuple()

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        AbstractTraverser.__init__(self, tokenizer, path)
        self._tree = tree
        self._root = self._tree.getroot()
        self._xpath = list()

    @property
    def root(self) -> Element:
        return self._root

    @property
    def hierarchy(self) -> Tuple[str, List[str], Dict[str, str]]:
        return self._hierarchy

    def location(self) -> Tuple:
        return str(self._filename.name), self._xpath[-1]

    @abstractmethod
    def _hierarchy_init(self):
        raise NotImplemented

    @abstractmethod
    def _hierarchy_update(self, xml: Element):
        raise NotImplemented

    def traverse(self):
        self._traverse(self._root[1])

    @abstractmethod
    def general(self, xml: Element, skip: bool):
        return NotImplemented()

    def _do_skip(self, xml: Element) -> bool:
        path = self._tree.getpath(xml).strip()
        skip = xml.tag if xml.tag in self.SKIP_TAGS else ''
        return path.find(skip)

    def _clean_xpath(self, xml: Element) -> str:
        return re.sub(r"\[\d+\]", '', self._tree.getpath(xml))

    def _traverse(self, xml: Element, in_skip: bool = False):
        self._xpath.append(self._tree.getpath(xml))

        self._hierarchy_update(xml)
        self.general(xml, in_skip)
        in_skip = in_skip if not self._do_skip(xml) else True

        for el in xml:
            self._traverse(el, in_skip)

        self._xpath.pop()

