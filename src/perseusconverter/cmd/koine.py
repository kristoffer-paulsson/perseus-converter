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
"""Module containing the LOAD command class."""
import unicodedata
from argparse import Namespace

from bs4 import BeautifulSoup
from lxml.etree import ElementTree, Element, XML, parse, XMLSyntaxError

from . import Command
from ..app import Config
from ..metaiterator import MetaIterator
from ..recursiveiterator import RecursiveIterator
from ..traverse.general import GeneralTraverser


def element_iterator(root: ElementTree, xml: Element):
    print(root.getpath(xml), xml.attrib, xml.text, xml.tail)
    for el in xml:
        element_iterator(root, el)


class KoineCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def __call__(self):
        count = 0
        for filename in RecursiveIterator(self.target):
            if not filename.is_file():
                self.logger.info("Registered but missing file: {}".format(filename))
                continue
            with open(filename) as file:
                self.logger.info("Processing file: {}".format(filename))
                try:
                    xml = GeneralTraverser(parse(file))
                    if xml.root.tag == "TEI.2":
                        print(filename)
                        count += 1
                except XMLSyntaxError as e:
                    self.logger.warn("{}: {}".format(e.__class__, str(e)))

        print(count)
