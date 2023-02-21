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

from lxml.etree import XMLSyntaxError

from greektextify.nlp.contextual import NlpContext
from . import Command
from ..app import Config
from ..recursiveiterator import RecursiveIterator
from ..traverse.bibbgt import BgtTraverser
from ..traverse.general import AbstractTeiTraverser, Tei2Traverser

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
    'tlg2003.tlg007.perseus-grc1.xml',
    'tlg2040.tlg002.perseus-grc1.xml',
)


class KoineCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def _pdl(self):
        count = 0
        for filename in RecursiveIterator(self.target.joinpath("canonical-greekLit/data/")):
            if not filename.is_file() or not filename.name[23:].startswith('grc') or not filename.name.endswith('.xml'):
                self.logger.warn("Registered but missing file: {}".format(filename))
                continue
            self.logger.info("Processing file: {}".format(filename))
            try:
                with NlpContext(AbstractTeiTraverser.open(filename), self.logger) as xml:
                    if isinstance(xml, AbstractTeiTraverser):
                        if filename.name in BETACODE:
                            self.logger.info("Traversing file {}".format(filename.name))
                            xml.traverse()
                        count += 1
            except XMLSyntaxError as e:
                self.logger.warn("{}: {}".format(e.__class__, str(e)))

        print(count)

    def _bib(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgt.txt")
        txt = BgtTraverser(filename)
        txt.traverse()
        for filename in RecursiveIterator(self.target.joinpath("bible-analyzer-corpora/corpora/abcom/")):
            if not filename.is_file():
                self.logger.warn("Registered but missing file: {}".format(filename))
                continue
            self.logger.info("Processing file: {}".format(filename))
            txt = BgtTraverser(filename)
            txt.traverse()

    def __call__(self):
        if self._args.corpora == 'bib':
            self._bib()
        elif self._args.corpora == 'pdl':
            self._pdl()
        else:
            pass
