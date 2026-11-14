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
import itertools
import pprint
from itertools import permutations
from pathlib import PosixPath
from typing import List, Tuple, Any, Iterable, Callable, Dict, NamedTuple, Set

from collatex import Collation, collate

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from greektextify.text.modify import WordModifier
from greektextify.text.word import GreekWord
from perseusconverter.iter.bgmiter import IterBGM
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
        self._bgmorph_filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgm.txt")
        self._bgtext_filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgt.txt")
        self._fix_filename = self.target.joinpath("bible-analyzer-corpora/corpora/rhlxx")
        self._nocr_filename = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")
        self._rec = rec

    def _bgmorph(self, fd, test, t_filter):
        bgmorph_e = Emitter(IterBGM(fd), test, t_filter)
        bgmorph_e.fast_forward()
        return bgmorph_e

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
        x = set()
        with self._bgmorph_filename.open('r') as morph, self._bgtext_filename.open('r') as bgt:
            token_filter = lambda x: x == 0
            m = self._bgmorph(morph, BOOK_ABBR, token_filter)
            t = self._bgtext(bgt, BOOK_ABBR, token_filter)

            while m.valid and t.valid:
                for r in zip(m.get_chapter(), t.get_chapter()):
                    if isinstance(r[0], BRef) or isinstance(r[1], BRef):
                        if str(r[0]) != str(r[1]):
                            # print(r)
                            pass
                        continue
                    if r[0][1] != r[1][1]:
                        #raise ValueError("Morph and text not in order")
                        continue
                    s = r[0][3]
                    if len(s) == 5 and s.startswith('n') and s.endswith('p'):
                        if GreekWord.glyphen(r[1][2])[0].ch in GreekAlphabet.CASE_UPPER:
                            x.add(WordModifier.stringify(r[1][2], False, WordModifier.deaccent))

            filename = self.target.joinpath("bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv")
            with filename.open('r') as f1:
                ognt_e = Emitter(IterOpenGNT(csv.reader(f1, delimiter='\t')), NEW_ABBR, token_filter)
                ognt_e.fast_forward()
                while ognt_e.valid:
                    for r in ognt_e.get_chapter():
                        if isinstance(r, BRef):
                            continue
                        s = r[3]
                        if len(s) == 7 and s.startswith('N-') and s[-2] == '-' and s[-1] in 'PTL':
                            if GreekWord.glyphen(r[2])[0].ch in GreekAlphabet.CASE_UPPER:
                                x.add(WordModifier.stringify(r[2], False, WordModifier.deaccent))
        for q in sorted(x):
            print(q, end=' ')
        return frozenset(x)

    def one_chapter(self, bref: BRef, e: Tuple[List[BRef | Tuple[int, int, str]], ...]):
        def _print(num: int, c: List[BRef | Tuple[int, int, str]]):
            with open("out/{}_test.{}.txt".format(bref, num), 'w') as f:
                for token in c:
                    if isinstance(token, BRef):
                        f.write("\n{}".format(token))
                    else:
                        f.write(" {}".format(WordModifier.stringify(token[2], False, WordModifier.search_token)))
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

    def print_book(self, m: Set[str] = frozenset([''])):
        with self._bgtext_filename.open('r') as bgt:
            token_filter = lambda x: x == 0
            e = self.normal(bgt, BOOK_ABBR, token_filter)
            self.book_loop(e, m, BRef('1Ki', 2, -1, -1))

            fix_e = self._lxxrh(BRef('1Ki', 2, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.book_loop(f, m, BRef('1Ki', 3, -1, -1))

            self.book_loop(e, m, BRef('Est', 1, -1, -1))
            self.chapter_loop(e, m, (False, False, True))
            self.book_loop(e, m, BRef('2Ma', 13, -1, -1))

            fix_e = self._lxxrh(BRef('2Ma', 13, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.chapter_loop(f, m, (False, False, False))

            self.book_loop(e, m,None)

            fix_e = self._lxxrh(BRef('Pro', 24, -1, -1), token_filter)
            f = (e[0], e[1], fix_e)
            self.book_loop(f, m, BRef('Ecc', 1, -1, -1))

            self.book_loop(e, m, BRef('Mic', 1, -1, -1))

            fix_e = self._lxxrh(BRef('Mic', 1, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.book_loop(f, m, BRef('Joe', 1, -1, -1))

            self.book_loop(e, m, BRef('Sut', 1, -1, -1))

            fix_e = self._lxxrh(BRef('Sut', 1, -1, -1), token_filter)
            f = (e[0], fix_e, e[2])
            self.chapter_loop(f, m, (False, False, False))

            self.book_loop(e, m,None)

            filename = self.target.joinpath("bible-analyzer-corpora/corpora/OpenGNT_version3_3.csv")
            with filename.open('r') as f1:
                ognt_e = Emitter(IterOpenGNT(csv.reader(f1, delimiter='\t')), NEW_ABBR, token_filter)
                ognt_e.fast_forward()

                filename = self.target.joinpath("bible-analyzer-corpora/corpora/rock-solid-gnt.txt")
                with filename.open('r') as f2:
                    rsgnt_e = Emitter(IterRSGNT(f2), NEW_ABBR, token_filter)
                    rsgnt_e.fast_forward()

                    g = (e[0], ognt_e, rsgnt_e)
                    self.book_loop(g, m, None)

    def _proper_noun(self, m: Emitter):
        x = set()
        for t in list(m.get_chapter()):
            if not isinstance(t, BRef):
                morph: str = t[3]
                if len(morph) == 5 and morph.startswith('n') and morph.endswith('p'):
                    x.add(t[1])
        return frozenset(x)

    def book_loop(self, e: Tuple[Emitter, ...], m: Set[str],  b_at: BRef | None = None):
        while self._sync(e):
            if b_at is not None and self._break(b_at, e):
                break
            c_book = e[0].book
            first = tuple([e_.get_chapter() for e_ in e])
            self._rec.rec(first, c_book != e[0].book, m)

            histo = [Histogram(h) for h in first]
            all_distances = [h1.distance(h2) for h1, h2 in permutations(histo, 2)]
            print(str(first[0][0]), all_distances)
            if max(all_distances) > 0.01:
                self.one_chapter(first[0][0], first)

    def chapter_loop(self, e: Tuple[Emitter, ...], m: Set[str], extra: Tuple[bool, ...]):
        c_book = e[0].book
        first = tuple([e_.get_chapter() + e_.get_chapter() if extra[i] else e_.get_chapter() for i, e_ in enumerate(e)])
        self._rec.rec(first, c_book != e[0].book, m)

        histo = [Histogram(h) for h in first]
        all_distances = [h1.distance(h2) for h1, h2 in permutations(histo, 2)]
        print(str(first[0][0]), all_distances)
        if max(all_distances) > 0.01:
            self.one_chapter(first[0][0], first)


class Recorder:
    def __init__(self, filename: PosixPath):
        self._file = filename
        self._tail = dict()
        self._last = BRef('n/a', -1, -1, -1)

    def _tailing(self, columns) -> Dict[str, List[BRef | Tuple[int, int, str]]]:
        tail = dict()
        for column in columns:
            grouping = dict(column.tokens_per_witness.items())
            for key, tokens in grouping.items():
                if key not in tail:
                    tail[key] = list()
                l = tail[key]
                for token in tokens:
                    l.append(token.token_data['data'])
        return tail

    def _tail_idx(self, columns):
        """Scans large column bottom up for 10 straight agreements one row at a time"""
        for idx in range(len(columns) - 1, -1, -1):
            for idc in range(idx, idx - 10, -1):
                if not self._flat_same(self._flat_col(columns, idc)):
                    break
            else:
                return idx + 1
        return -1

    @classmethod
    def _cmp(cls, token1, token2) -> bool:
        b1 = '_' in token1
        b2 = '_' in token2
        if b1 and b2:
            return token1 == token2
        elif b1 or b2:
            return False
        else:
            return GreekWord.cmp_semi(GreekWord.glyphen(token1), GreekWord.glyphen(token2), True)

    def rec(self, e: Tuple[List[BRef | Tuple[int, int, str]], ...], last_chapter: bool = False, nouns: Set[str] = set()):

        c = Collation()
        for idx, e_ in enumerate(e):
            s = str(idx)
            if s in self._tail:
                e_ = self._tail[s] + e_
                del self._tail[s]
            c.add_witness({"id": str(idx), "tokens": [{"t": x[2], "data": x} if not isinstance(x, BRef) else {"t": str(x).replace(' ', '_'), "data": x} for x in e_]})
        table = collate(c, segmentation=False, properties_filter=lambda t1, t2: Recorder._cmp(t1['t'], t2['t']))

        if not last_chapter:
            tail_idx = self._tail_idx(table.columns)
            if tail_idx < len(table.columns):
                tail = self._tailing(table.columns[tail_idx:])
                e2 = dict(enumerate(e))
                for k, v in tail.items():
                    self._tail[str(k)] = e2[int(k)][:len(v)]
        else:
            tail_idx = len(table.columns)

        with self._file.open('a') as out:
            for col_idx, column in enumerate(table.columns[:tail_idx]):
                grouping = dict(column.tokens_per_witness.items())
                fcol = self._flat_col(table.columns, col_idx)

                if len(grouping) >= 2:
                    token = grouping['0'][0].token_data['data']
                    if '_' in fcol[0]:
                        out.write("\n{}".format(str(token)))
                    else:
                        if self._flat_same(fcol):
                            test = WordModifier.stringify(token[2], op=WordModifier.deaccent)
                            if test in nouns:
                                out.write(" {}".format(WordModifier.stringify(token[2], op=WordModifier.capitalize)))
                            else:
                                out.write(" {}".format(WordModifier.stringify(token[2], op=WordModifier.lower)))

                        else:
                            raise ValueError("Weird grouping, all are excepted the same")
                else:
                    print('Skipping: ' + str(grouping))

    def _flat_col(self, columns, col_idx) -> List[str]:
        col = columns[col_idx]
        row = list(str(x) for x in itertools.chain.from_iterable(col.tokens_per_witness.values()))
        return row

    @classmethod
    def _flat_same(cls, g: List[str], op: Callable[[Tuple[GreekGlyph]], Tuple[GreekGlyph]] = WordModifier.search_token) -> bool:
        return all(WordModifier.stringify(x, False, op) for x in g)


