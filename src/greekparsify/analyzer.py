#
# Copyright (c) 2024 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Greek Grammar Analyzer mixin base class."""
from types import FunctionType
from typing import List, Tuple


class GrammarAnalyzerMixin:

    @classmethod
    def scan_ahead(cls, tokens: List[Tuple[int, ...]], start: int, scan: FunctionType) -> int:
        for idx in range(start+1, len(tokens)):
            if scan(tokens[idx]):
                return idx

    @classmethod
    def scan_next(cls, tokens: List[Tuple[int, ...]], start: int, tt) -> int:
        if type(tt) == int:
            tt = (tt,)
        for idx in range(start, len(tokens)):
            if tokens[idx][0] in tt:
                return idx

    @classmethod
    def parse(cls, tokens: List[Tuple[int, ...]]):
        return NotImplemented