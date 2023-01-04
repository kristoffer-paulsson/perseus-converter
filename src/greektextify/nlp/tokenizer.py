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
"""Koine tokenizer for NLTK based on greek-textify."""
from typing import Iterator, Tuple, List

import nltk

from ..text.alphabet import GreekAlphabet
from ..text.extended import GreekExtended
from ..text.midway import GreekMidway
from ..text.spacing import Spacing


class KoineTokenizer(nltk.tokenize.api.TokenizerI):

    LETTERS = frozenset(
        set(GreekAlphabet.CASE_UPPER) |
        set(GreekAlphabet.CASE_LOWER) |
        set(GreekMidway.LETTERS.keys()) |
        set(GreekExtended.LETTERS.keys())
    )

    def __init__(self, encoding: str = 'utf8', options: dict = None, verbose: bool = False):
        self._encoding = encoding
        self._options = options
        self._verbose = verbose

    def tokenize(self, s: str) -> List[str]:
        if nltk.tokenize.internals.overridden(self.tokenize_sents):
            return self.tokenize_sents([s])[0]

    def span_tokenize(self, s: str) -> Iterator[Tuple[int, int]]:
        chgen = enumerate(s)
        for index, ch in chgen:
            if ch in self.LETTERS:
                start = index
                end = self._word_scan(chgen)
                yield start, end

    def _word_scan(self, chgen) -> int:
        for index, ch in chgen:
            if ch in Spacing.BLANKS:
                return index
            elif ch not in self.LETTERS:
                raise RuntimeWarning("Unknown character '{}' as {}.".format(hex(ch), index))