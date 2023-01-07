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
from argparse import Namespace

from lxml.etree import parse, XMLSyntaxError

from . import Command
from ..app import Config
from ..metaiterator import MetaIterator
from ..recursiveiterator import RecursiveIterator
from ..traverse.general import GeneralTraverser, EXCEPTIONS


BETACODE = (
    'tlg2003.tlg008.perseus-grc1.xml',
    'tlg2003.tlg002.perseus-grc1.xml',
    'tlg2003.tlg011.perseus-grc1.xml',
    'tlg2003.tlg005.perseus-grc1.xml',
    'tlg2003.tlg001.perseus-grc1.xml',
    'tlg2003.tlg012.perseus-grc1.xml',
    'tlg2003.tlg006.perseus-grc1.xml',
    'tlg2003.tlg004.perseus-grc1.xml',
    'tlg2003.tlg010.perseus-grc1.xml',
    'tlg2003.tlg003.perseus-grc1.xml',
    'tlg2003.tlg009.perseus-grc1.xml',
    'tlg2003.tlg007.perseus-grc1.xml'
)


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
                    xml = GeneralTraverser(parse(file), EXCEPTIONS[filename.name] if filename.name in EXCEPTIONS.keys() else tuple())
                    if xml.format == "TEI.2":
                        print(filename.name)
                        if filename.name not in BETACODE:
                            xml.traverse()
                        count += 1
                except XMLSyntaxError as e:
                    self.logger.warn("{}: {}".format(e.__class__, str(e)))

        print(count)
