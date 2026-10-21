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
""""""
from typing import NamedTuple


class BRef(NamedTuple):
    book: str
    chapter: int
    verse: int
    sub: int

    def __str__(self) -> str:
        if self.sub > 0:
            return "{} {}:{}({})".format(self.book, self.chapter, self.verse, self.sub)
        else:
            return "{} {}:{}".format(self.book, self.chapter, self.verse)


class Counter:
    def __init__(self, start: int = 0):
        self._start = start
        self._count = self._start

    def increment(self) -> int:
        self._count += 1
        return self._count

    def current(self) -> int:
        return self._count

    def reset(self, start: int = 0) -> None:
        self._start = start
        self._count = start