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
from abc import ABCMeta, abstractmethod

from lxml.etree import ElementTree, Element, XML, parse, XMLSyntaxError


class AbstractTraverser(metaclass=ABCMeta):

    _root: Element

    def __init__(self, tree: ElementTree):
        self._tree = tree
        self._root = tree.getroot()
        self._id = list
        self._primary = None
        self._hierarchies = list()
        self._get_id()

    @property
    def root(self) -> Element:
        return self._root

    def traverse(self):
        self._traverse(self._root)

    @abstractmethod
    def general(self, xml: Element):
        return NotImplemented()

    def _clean_xpath(self, xml: Element) -> str:
        return re.sub(r"\[\d+\]", '', self._tree.getpath(xml))

    def _get_id(self):
        for tid in self._tree.getroot().find("text[1]"):
            if "id" in tid.attrib.keys():
                self._id = tid.attrib["id"]

    def _build_hier(self):
        for refs in self._tree.getroot().iterfind("teiHeader/encodingDesc/refsDecl"):
            units = list()
            for state in refs.iterfind("state"):
                units.append(state.attrib['unit'])
            hierarchy = "-".join(units)
            if not self._primary:
                self._primary = hierarchy
            self._hierarchies.add(hierarchy)

    def _traverse(self, xml: Element):
        self.general(xml)
        for el in xml:
            self._traverse(el)
