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
from lxml.builder import unicode

from . import Command
from perseusconverter.app import Config
from ..gen.bgm import BGMLexemeGenerator
from ..gen.bgt import BGTCorpusGenerator
from ..gen.ognt import OGNTLexemeGenerator, OGNTCorpusGenerator
from ..gen.rsgnt import RSGNTCorpusGenerator
from ..scan.bgt import BGTScanner

from ..scan.comparator import OGNT2BGMComparator, MultiComparator, BookChapterComparator
from ..scan.ognt import OGNTScanner
from ..scan.bgm import BGMScanner
from ..scan.rsgnt import RSGNTScanner
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
        #BGTCorpusGenerator(BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False), nt_start).generate()
        #RSGNTCorpusGenerator(RSGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/rock-solid-gnt.txt", False), nt_start).generate()
        #OGNTCorpusGenerator(OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv", False), nt_start).generate()

        scanners = iter(MultiComparator(
            ref = Reference("Matthew", 1, 1),
            bgt = BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False),
            rsgnt = RSGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/rock-solid-gnt.txt", False),
            ognt = OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv", False)
        ))

        missing = 0
        for tokens in filter.compare(scanners):
            words = [unicodedata.normalize('NFD', v.token.lower()) for k, v in tokens.items()]
            variants = len(set(words))
            if variants>1:
                missing += 1
            print(str(variants) + ': ' + ', '.join(words))
            if missing > 2:
                print("Too many missing variants, stopping.")
                break

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

    def _merge_streams(self):
        nt_start = Reference("Revelation", 22, 20)
        scanners = MultiComparator(
            ref=nt_start,
            bgt=BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False),
            rsgnt=RSGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/rock-solid-gnt.txt", False),
            ognt=OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv", False)
        )

        merged_tokens = []
        for tokens in scanners:
            token_counts = {}
            for name, token in tokens.items():
                if token is not None:
                    normalized_token = unicodedata.normalize('NFD', token.token.lower())
                    token_counts[normalized_token] = token_counts.get(normalized_token, 0) + 1
                else:
                    token_counts["null"] = token_counts.get("null", 0) + 1

            if token_counts:
                # Choose the most elected token
                most_elected = max(token_counts, key=token_counts.get)
                merged_tokens.append(most_elected)

        print("Merged Tokens:")
        print(merged_tokens)
