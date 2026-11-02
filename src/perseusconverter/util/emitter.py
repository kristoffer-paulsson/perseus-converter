#
# Copyright (c) 2026 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
""""""
from typing import Callable, Tuple

from perseusconverter.util.utils import BRef, Counter


class Emitter:

    def __init__(self, iterator, start_ref: BRef | Tuple[str, ...] = BRef('n/a', -1, -1, -1), token_filter: Callable[[int], bool] = lambda x: True):
        self._iterator = iterator.__iter__()
        self._filter = token_filter
        self._last = None
        self._ref = start_ref if isinstance(start_ref, BRef) else BRef(start_ref[0], -1, -1, -1)
        self._book_list = start_ref if isinstance(start_ref, Tuple) else tuple()
        self._token_counter = Counter()
        self._bible = dict()
        self._chapter_cnt = Counter()
        self._verse_cnt = Counter()

    @property
    def same(self) -> bool:
        return self._last is not None and self._last.book == self._ref.book

    @property
    def valid(self) -> bool:
        return self.same or self._last.book in self._book_list if self._last is not None else False

    @property
    def book(self) -> str:
        return self._last.book if self._last is not None else self._ref.book

    @property
    def chapter(self) -> int:
        return self._last.chapter if self._last is not None else self._ref.chapter

    def _update_model(self, bref: BRef, chapter_cnt, verse_cnt, bible) -> bool:
        br = False
        if bref.book not in bible:
            bible[bref.book] = dict()
            chapter_cnt.reset()
        if chapter_cnt.current() < bref.chapter:
            while bref.chapter - chapter_cnt.current() > 1:
                chapter_cnt.increment()
                #self._add_missing(BRef(bref.book, chapter_cnt.current(), -1, -1))
            chapter_cnt.increment()
            if chapter_cnt.current() != bref.chapter:
                raise RuntimeError("Chapter mismatch {} / {}".format(chapter_cnt.current(), bref.chapter))
            verse_cnt.reset()
            br = True
        if bref.sub != -1:
            pass
            # self._add_subverse(bref)
        elif bref.verse == 0:
            if bref.chapter not in bible[bref.book]:
                bible[bref.book][bref.chapter] = list()
                br = True
            bible[bref.book][bref.chapter].append(bref.verse)
        elif verse_cnt.current() < bref.verse:
            while bref.verse - verse_cnt.current() > 1:
                verse_cnt.increment()
                # self._add_missing(BRef(bref.book, bref.chapter, verse_cnt.current(), -1))
            if bref.chapter not in bible[bref.book]:
                bible[bref.book][bref.chapter] = list()
                br = True
            else:
                bible[bref.book][bref.chapter].append(bref.verse)
            verse_cnt.increment()
        elif bref.verse in bible[bref.book][bref.chapter]:
            pass
            # self._add_duplicate(bref)
        else:
            pass
            # self._add_malplaced(bref)
        return br

    def fast_forward(self):
        for token in self._iterator:
            if isinstance(token, BRef):
                if token.book == self._ref.book and (token.chapter == self._ref.chapter or self._ref.chapter == -1):
                    self._update_model(token, self._chapter_cnt, self._verse_cnt, self._bible)
                    self._last = token
                    break
            elif isinstance(token, Tuple):
                if self.same:
                    if self._filter(token[0]):
                        self._token_counter.increment()
            else:
                raise TypeError("Token type {} not supported".format(type(token)))
        else:
            raise RuntimeError("No match found")

    def get_chapter(self)-> Tuple[BRef | Tuple[int, int, str], ...]:
        if not self.valid:
            return tuple()

        tokens = list()
        tokens.append(self._last)
        for token in self._iterator:
            if isinstance(token, BRef):
                if self._update_model(token, self._chapter_cnt, self._verse_cnt, self._bible):
                    if self._last.book != token.book:
                        self._token_counter.reset()
                    self._last = token
                    break
                tokens.append(token)
            elif isinstance(token, Tuple):
                if self._filter(token[0]):
                    self._token_counter.increment()
                    tokens.append((token[0], self._token_counter.current(), token[1]))
            else:
                raise TypeError("Token type {} not supported".format(type(token)))
        else:
            self._last = None

        return tuple(tokens)
