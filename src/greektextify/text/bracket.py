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


class Bracketing(TokenImmaterializableMixin):
    """Bracketing parser."""

    LEFT_PARENTHESIS = '\u0028'
    RIGHT_PARENTHESIS = '\u0029'
    LEFT_SQUARE_BRACKET = '\u005B'
    RIGHT_SQUARE_BRACKET = '\u005D'
    LEFT_CURLY_BRACKET = '\u007B'
    LEFT_ANGLE_BRACKET = '\u3008'
    RIGHT_ANGLE_BRACKET = '\u3009'

    BRACKETS = frozenset([
        LEFT_PARENTHESIS, RIGHT_PARENTHESIS, LEFT_SQUARE_BRACKET, RIGHT_SQUARE_BRACKET, LEFT_CURLY_BRACKET,
        LEFT_ANGLE_BRACKET, RIGHT_ANGLE_BRACKET
    ])

    def __init__(self, word: str):
        self._word = word

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str]:
        if len(text) > 0:
            return tuple(text[0]) if text[0] in cls.BRACKETS else tuple()
        return tuple()
