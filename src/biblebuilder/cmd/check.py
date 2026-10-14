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
from argparse import Namespace

import unicodedata

from . import Command
from perseusconverter.app import Config

from ..scan.scanner import JointScanner, Reference, ScanIter
from ..scan.ognt import OGNTScanner
from ..scan.bgm import BGMScanner
from ..scan.bgt import BGTScanner
from ..scan.rsgnt import RSGNTScanner
from ..scan.jgvt import JGVTScanner


class CheckCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def __call__(self):
        print(self.target)
        self.logger.info("{} found".format("test"))
        self._gen()

    def _gen(self):
        self.logger.info("Checking OpenGNT")
        ognt = ScanIter(OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv", True))
        self._check(ognt)
        self.logger.info("Finished OpenGNT")

        self.logger.info("Checking Rock Solid GNT")
        rsgnt = ScanIter(RSGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/rock-solid-gnt.txt", False))
        self._check(rsgnt)
        self.logger.info("Finished Rock Solid GNT")

        self.logger.info("Checking Vetus JG")
        jgvt = ScanIter(JGVTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/septuagint3/", True, False))
        self._check(jgvt)
        self.logger.info("Finished Vetus JG")

        self.logger.info("Checking BGT/BGM")
        bgt = ScanIter(JointScanner(
            BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False),
            BGMScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgm.txt")
        ))
        self._check(bgt)
        self.logger.info("Finished BGT/BGM")

    def _check(self, scanner):
        for token in scanner:
            print(token.word)
            for glyph in token.word_gl:
                if glyph.ch is None:
                    print(token.book, token.chapter, token.verse, token.sub_verse, token.index, token.word, unicodedata.name(token.word[-1]))
                    break

