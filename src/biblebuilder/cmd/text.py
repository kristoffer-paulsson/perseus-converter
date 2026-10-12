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
from typing import List

from collatex import Collation, collate

from greektextify.text.word import GreekWord
from ..scan.scanner import ChapterExtractor
from ..scan.scanner import WideToken, ScanIter
from . import Command
from perseusconverter.app import Config
from ..scan.bgt import BGTScanner

from ..scan.comparator import MultiComparator
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

    def _build(self, token_list: List):
        words = list()
        for token in token_list:
            if token is not None:
                if type(token) is WideToken:
                    w = token.word
                else:
                    w = token.token
                normalized_token = unicodedata.normalize('NFD', w.lower())
                words.append(normalized_token.strip())
        return ' '.join(words)

    def _gen(self):
        nt_start = Reference("Revelation", 1, 1)
        bgt = ChapterExtractor(ScanIter(
            BGTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/bgt.txt", False),
            nt_start,
        )).get_chapter()
        rsgnt = ChapterExtractor(ScanIter(
            RSGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/rock-solid-gnt.txt", False),
            nt_start
        )).get_chapter()
        ognt = ChapterExtractor(ScanIter(
            OGNTScanner(str(self.target) + "/bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv", False),
            nt_start
        )).get_chapter()

        c = Collation()
        c.add_witness({"id": 'bgt', "tokens": [{"t": x.token, "data": x} for x in bgt]})
        c.add_witness({"id": 'rsgnt', "tokens": [{"t": x.token, "data": x} for x in rsgnt]})
        c.add_witness({"id": 'ognt', "tokens": [{"t": x.word, "data": x} for x in ognt]})
        table = collate(c, segmentation=False, properties_filter=lambda t1, t2: TextCommand._cmp(t1['t'], t2['t']))

        all_sigla = [row.header for row in table.rows]
        sigla_len = len(all_sigla)
        for col_idx, column in enumerate(table.columns):
            print("col: " + str(col_idx))
            # Grouping of witnesses
            grouping = dict()
            for sigil, tokens in column.tokens_per_witness.items():
                t = tokens[0].token_data['t']
                data = tokens[0].token_data['data']
                for k in grouping.keys():
                    print(sigil, t, type(t), k, type(k))
                    if TextCommand._cmp(t, k):
                        grouping[k].append((sigil, data))
                        break
                else:
                    grouping[t] = list()
                    grouping[t].append((sigil, data))
            # Majority consideration
            #for v in sorted(grouping.values()):
            #    print(len(v))

    @classmethod
    def _cmp(cls, token1, token2) -> bool:
        return GreekWord.cmp_semi(GreekWord.glyphen(token1), GreekWord.glyphen(token2), True)

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
