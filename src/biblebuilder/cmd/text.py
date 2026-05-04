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

from . import Command
from perseusconverter.app import Config
from ..gen.bgm import BGMLexemeGenerator
from ..gen.bgt import BGTCorpusGenerator
from ..gen.ognt import OGNTLexemeGenerator
from ..scan.bgt import BGTScanner

from ..scan.comparator import OGNT2BGMComparator
from ..scan.ognt import OGNTScanner
from ..scan.bgm import BGMScanner
from ..scan.scanner import Reference

class TextCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def __call__(self):
        print(self.target)
        self.logger.info("{} found".format("test"))
        self._gen()

    def _gen(self):
        nt_start = Reference("Matthew", 1, 1)
        BGTCorpusGenerator(BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False), nt_start).generate()
        #OGNTLexemeGenerator(OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv"), nt_start).generate()
        #BGMLexemeGenerator(BGMScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgm.txt"), nt_start).generate()

    def _cmp(self):
        print()
        comparator = OGNT2BGMComparator(
            BGMScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgm.txt"),
            OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv"),
            Reference("Matthew", 1, 1)
        )

        for token in comparator.iter():
            print(token)

        comparator.get_error_cnt()
        comparator.get_errors(0)

