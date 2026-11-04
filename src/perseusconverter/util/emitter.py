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

from perseusconverter.util.collector import BaseCollector
from perseusconverter.util.utils import BRef, Counter


class Emitter(BaseCollector):

    def __init__(self, iterator, start_ref: BRef | Tuple[str, ...] = BRef('n/a', -1, -1, -1), token_filter: Callable[[int], bool] = lambda x: True):
        super().__init__(iterator.__iter__())
        self._filter = token_filter
        self._last = None
        self._ref = start_ref if isinstance(start_ref, BRef) else BRef(start_ref[0], -1, -1, -1)
        self._book_list = start_ref if isinstance(start_ref, Tuple) else tuple()
        self._token_counter = Counter()
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

    def fast_forward(self):
        cur_book = self._ref.book
        for token in self._iterator:
            if isinstance(token, BRef):
                if cur_book != token.book:
                    cur_book = token.book
                    self._token_counter.reset()
                if token.book == self._ref.book and (token.chapter == self._ref.chapter or self._ref.chapter == -1):
                    self._update_model(self._model, token, self._chapter_cnt, self._verse_cnt)
                    self._last = token
                    break
            elif isinstance(token, Tuple):
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
                if self._update_model(self._model, token, self._chapter_cnt, self._verse_cnt):
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
