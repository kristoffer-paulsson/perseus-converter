#
# Copyright (c) 2023 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Brackets handling for tokenizer."""
from typing import Tuple

from greektextify.text.immaterializer import TokenImmaterializableMixin


class GreekUnheard(TokenImmaterializableMixin):
    """Bracketing parser."""

    DIGIT_ZERO = '\u0030'
    DIGIT_ONE = '\u0031'
    DIGIT_TWO = '\u0032'
    DIGIT_THREE = '\u0033'
    DIGIT_FOUR = '\u0034'
    DIGIT_FIVE = '\u0035'
    DIGIT_SIX = '\u0036'
    DIGIT_SEVEN = '\u0037'
    DIGIT_EIGHT = '\u0038'
    DIGIT_NINE = '\u0039'
    PERCENT_SIGN = '\u0025'
    DAGGER = '\u2020'
    MACRON = '\u00AF'
    QUESTION_MARK = '\u003F'
    COMBINING_DOT_BELOW = '\u0323'
    ZERO_WIDTH_NO_BREAK_SPACE = '\uFEFF'
    ASTERISK = '\u002A'
    COMMERCIAL_AT = '\u0040'
    NUMBER_SIGN = '\u0023'
    LATIN_SMALL_LETTER_I = '\u0069'

    UNHEARD = frozenset([
        DIGIT_ZERO, DIGIT_ONE, DIGIT_TWO, DIGIT_THREE, DIGIT_FOUR, DIGIT_FIVE, DIGIT_SIX, DIGIT_SEVEN, DIGIT_EIGHT,
        DIGIT_NINE, PERCENT_SIGN, DAGGER, MACRON, QUESTION_MARK, COMBINING_DOT_BELOW, ZERO_WIDTH_NO_BREAK_SPACE,
        ASTERISK, COMMERCIAL_AT, NUMBER_SIGN, LATIN_SMALL_LETTER_I
    ])

    def __init__(self, word: str):
        self._word = word

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str, ...]:
        token = list()

        for ch in text:
            if ch in cls.UNHEARD:
                token.append(ch)
            else:
                break

        return tuple(token)
