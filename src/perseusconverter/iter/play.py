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
import csv
from curses.ascii import isalnum
from itertools import permutations
from pathlib import PosixPath
from pprint import pprint
from typing import List, Tuple, Any, Iterable, Callable

from collatex import Collation, collate

from greektextify.text.glyph import GreekGlyph
from greektextify.text.modify import WordModifier
from greektextify.text.word import GreekWord
from perseusconverter.iter.bgtiter import IterBGT
from perseusconverter.iter.catssiter import IterCatSS, CatSSFileIter
from perseusconverter.iter.fileiter import IterNocr, NocrFileIter
from perseusconverter.iter.fixiter import IterFix, FixFileIter
from perseusconverter.iter.openiter import IterOpenGNT
from perseusconverter.iter.rockiter import IterRSGNT
from perseusconverter.util.books import BOOK_ABBR, NEW_ABBR
from perseusconverter.util.emitter import Emitter
from perseusconverter.util.utils import BRef


class Histogram:

    def __init__(self, tokens: List[Tuple[Any, ...] | BRef]):
        self._gram = dict()
        for token in tokens:
            if not isinstance(token, BRef):
                word = WordModifier.stringify(token[2], WordModifier.search_token)
                if word not in self._gram:
                    self._gram[word] = 0
                self._gram[word] += 1

    def distance(self, other: "Histogram") -> float:
        s_keys = frozenset(self._gram.keys())
        o_keys = frozenset(other._gram.keys())
        d = len(o_keys - s_keys)

        for key in frozenset(o_keys.intersection(s_keys)):
            d += abs(self._gram[key] - other._gram[key])

        return d / sum(self._gram.values())


class Player:

    def __init__(self, target: PosixPath, rec: "Recorder"):
        self.target = target
        self._bgtext_filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgt.txt")
        self._fix_filename = self.target.joinpath("bible-analyzer-corpora/corpora/rhlxx")
        self._rec = rec

    def _bgtext(self, fd, test, t_filter):
        bgtext_e = Emitter(IterBGT(fd, test), test, t_filter)
        bgtext_e.fast_forward()
        return bgtext_e

    def _nocr(self, filename, test, t_filter):
        nocr_e = Emitter(IterNocr(NocrFileIter(filename)), test, t_filter)
        nocr_e.fast_forward()
        return nocr_e

    def _catss(self, filename, test, t_filter):
        catss_e = Emitter(IterCatSS(CatSSFileIter(filename)), test, t_filter)
        catss_e.fast_forward()
        return catss_e

    def _lxxrh(self, test, t_filter):
        fix_e = Emitter(IterFix(FixFileIter(self._fix_filename)), test, t_filter)
        fix_e.fast_forward()
        return fix_e

    def _until(self, b: BRef, e: Tuple[Emitter, Emitter, Emitter]) -> bool:
        return  not ((b.book == e[0].book and b.chapter == e[0].chapter and e[0].valid
                ) or (b.book == e[1].book and b.chapter == e[1].chapter and e[1].valid
                      ) or (b.book == e[2].book and b.chapter == e[2].chapter and e[2].valid))

    def _sync(self, e: Tuple[Emitter, ...]) -> bool:
        book = e[0].book
        chapter = e[0].chapter
        return all([b.valid for b in e]) and all([b.book == book for b in e]) and all([b.chapter == chapter for b in e])

    def _break(self, b: BRef, e: Tuple[Emitter, ...]) -> bool:
        return b.book == e[0].book and b.chapter == e[0].chapter

    def print(self):
        nocr_filename = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")
        catss_filename = self.target.joinpath("bible-analyzer-corpora/corpora/catss")

        with self._bgtext_filename.open('r') as bgt:
            efilter = lambda x: x == 0
            test = BRef('Psa', 9, -1, -1)
            #test = OLD_ABBR[:5]
            #for test in OLD_ABBR:
                #test = [test]
            bgtext_e = self._bgtext(bgt, test, efilter)
            nocr_e = self._nocr(nocr_filename, test, efilter)
            catss_e = self._catss(catss_filename, test, efilter)
            # fix_e = self._lxxrh(test, efilter)

            #while all((bgtext_e.valid, nocr_e.valid, catss_e.valid)):
            #first = (bgtext_e.get_chapter(), nocr_e.get_chapter(), catss_e.get_chapter(), fix_e.get_chapter())
            first = (bgtext_e.get_chapter(), nocr_e.get_chapter(), catss_e.get_chapter())
            #first = (bgtext_e.get_chapter(), catss_e.get_chapter(), fix_e.get_chapter())
            #first = (bgtext_e.get_chapter(), nocr_e.get_chapter(), fix_e.get_chapter())

            all_max = list()
            for i in first:
                all_max.append(len(i))
            max_len = max(all_max)
            #for idx in range(0, max_len):
            #    print(
            #        first[0][idx] if idx < all_max[0] else 'n/a',
            #        first[1][idx]  if idx < all_max[1] else 'n/a',
            #        first[2][idx] if idx < all_max[2] else 'n/a'
            #    )
            histo = list()
            for h in first:
                histo.append(Histogram(h))
            print(str(first[0][0]),
                (histo[0].distance(histo[1]), histo[0].distance(histo[2])),
                (histo[1].distance(histo[0]), histo[1].distance(histo[2])),
                (histo[2].distance(histo[0]), histo[2].distance(histo[1])),
            )
            self.one_chapter(test, first)

    def one_chapter(self, bref: BRef, e: Tuple[List[BRef | Tuple[int, int, str]], ...]):
        def _print(num: int, c: List[BRef | Tuple[int, int, str]]):
            with open("out/{}_test.{}.txt".format(bref, num), 'w') as f:
                for token in c:
                    if isinstance(token, BRef):
                        f.write("\n{}".format(token))
                    else:
                        f.write(" {}".format(WordModifier.stringify(token[2], WordModifier.search_token)))
        for idx, _e in enumerate(e):
            _print(idx, _e)

    def normal(self, bgt: Iterable, refs: BRef | Tuple[str, ...], token_filter: Callable[[int], bool] = lambda x: True) ->  Tuple[Emitter, ...]:
        nocr_filename = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")
        catss_filename = self.target.joinpath("bible-analyzer-corpora/corpora/catss")
        return (
            self._bgtext(bgt, refs, token_filter),
            self._nocr(nocr_filename, refs, token_filter),
            self._catss(catss_filename, refs, token_filter)
        )

    def _emitter_status(self, e: Tuple[Emitter, ...]):
        for e_ in e:
            print(e_.valid, e_.book, e_.chapter)

    def print_book(self):
        with self._bgtext_filename.open('r') as bgt:
            token_filter = lambda x: x == 0
            e = self.normal(bgt, BOOK_ABBR, token_filter)
            self.book_loop(e, BRef('1Ki', 2, -1, -1))

            fix_e = self._lxxrh(BRef('1Ki', 2, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.book_loop(f, BRef('1Ki', 3, -1, -1))

            self.book_loop(e, BRef('Est', 1, -1, -1))
            self.chapter_loop(e, (False, False, True))
            self.book_loop(e, BRef('2Ma', 13, -1, -1))

            fix_e = self._lxxrh(BRef('2Ma', 13, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.chapter_loop(f, (False, False, False))

            self.book_loop(e, None)

            fix_e = self._lxxrh(BRef('Pro', 24, -1, -1), token_filter)
            f = (e[0], e[1], fix_e)
            self.book_loop(f, BRef('Ecc', 1, -1, -1))

            self.book_loop(e, BRef('Mic', 1, -1, -1))

            fix_e = self._lxxrh(BRef('Mic', 1, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.book_loop(f, BRef('Joe', 1, -1, -1))

            self.book_loop(e, BRef('Sut', 1, -1, -1))

            fix_e = self._lxxrh(BRef('Sut', 1, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.chapter_loop(f, (False, False, False))

            self.book_loop(e, None)

            filename = self.target.joinpath("bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv")
            with filename.open('r') as f1:
                ognt_e = Emitter(IterOpenGNT(csv.reader(f1, delimiter='\t')), NEW_ABBR, token_filter)
                ognt_e.fast_forward()

                filename = self.target.joinpath("bible-analyzer-corpora/corpora/rock-solid-gnt.txt")
                with filename.open('r') as f2:
                    rsgnt_e = Emitter(IterRSGNT(f2), NEW_ABBR, token_filter)
                    rsgnt_e.fast_forward()

                    g = (e[0], ognt_e, rsgnt_e)
                    self.book_loop(g, None)

    def book_loop(self, e: Tuple[Emitter, ...], b_at: BRef | None = None):
        while self._sync(e):
            if b_at is not None and self._break(b_at, e):
                break
            first = tuple([e_.get_chapter() for e_ in e])
            self._rec.rec(first)

            histo = [Histogram(h) for h in first]
            all_distances = [h1.distance(h2) for h1, h2 in permutations(histo, 2)]
            print(str(first[0][0]), all_distances)
            if max(all_distances) > 0.01:
                self.one_chapter(first[0][0], first)

    def chapter_loop(self, e: Tuple[Emitter, ...], extra: Tuple[bool, ...]):
        first = tuple([e_.get_chapter() + e_.get_chapter() if extra[i] else e_.get_chapter() for i, e_ in enumerate(e)])
        self._rec.rec(first)

        histo = [Histogram(h) for h in first]
        all_distances = [h1.distance(h2) for h1, h2 in permutations(histo, 2)]
        print(str(first[0][0]), all_distances)
        if max(all_distances) > 0.01:
            self.one_chapter(first[0][0], first)


class Recorder:
    def __init__(self):
        pass

    @classmethod
    def _cmp(cls, token1, token2) -> bool:
        return False if '_' in (token1, token2) else GreekWord.cmp_semi(GreekWord.glyphen(token1), GreekWord.glyphen(token2), True)

    @classmethod
    def _all_same(cls, g: List[GreekWord], op: Callable[[Tuple[GreekGlyph]], Tuple[GreekGlyph]] = WordModifier.search_token) -> bool:
        return all(WordModifier.stringify(x[2][2], op) for x in g)

    def rec(self, e: Tuple[List[BRef | Tuple[int, int, str]], ...]):
        c = Collation()
        for idx, e_ in enumerate(e):
            c.add_witness({"id": str(idx), "tokens": [{"t": x[2], "data": x} if not isinstance(x, BRef) else {"t": '_', "data": x} for x in e_]})
        table = collate(c, segmentation=False, properties_filter=lambda t1, t2: Recorder._cmp(t1['t'], t2['t']))

        all_sigla = [row.header for row in table.rows]
        sigla_len = len(all_sigla)
        for col_idx, column in enumerate(table.columns):
            # print("col: " + str(col_idx))
            # Grouping of witnesses
            grouping = list()
            for sigil, tokens in column.tokens_per_witness.items():
                grouping.append((sigil, tokens[0].token_data['t'], tokens[0].token_data['data']))
                t = tokens[0].token_data['t']
                data = tokens[0].token_data['data']
            # print(grouping)

            if len(grouping) >= 2:
                if grouping[0][1] == '_':
                    print('\n' + str(grouping[0][2]), end=' ')
                else:
                    if self._all_same(grouping):
                        print(WordModifier.stringify(grouping[0][2][2], op=WordModifier.lower), end=' ')
                    else:
                        raise ValueError("Weird grouping, all are excepted the same")
            else:
                print('Skipping: ' + str(grouping))


