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
"""Greek qoutation marks."""
from typing import Tuple

from greektextify.text.immaterializer import TokenImmaterializableMixin


class GreekQuotation(TokenImmaterializableMixin):
    """Greek quotation parser."""

    QUOTATION_MARK = '\u0022'
    LEFT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK = '\u00AB'
    RIGHT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK = '\u00BB'
    LEFT_SINGLE_QUOTATION_MARK = '\u2018'
    RIGHT_SINGLE_QUOTATION_MARK = '\u2019'
    LEFT_DOUBLE_QUOTATION_MARK = '\u201C'
    RIGHT_DOUBLE_QUOTATION_MARK = '\u201D'

    QUOTE_MARKS = frozenset([
        QUOTATION_MARK, LEFT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK, RIGHT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK,
        LEFT_SINGLE_QUOTATION_MARK, RIGHT_SINGLE_QUOTATION_MARK, LEFT_DOUBLE_QUOTATION_MARK,
        RIGHT_DOUBLE_QUOTATION_MARK
    ])

    def __init__(self, word: str):
        self._word = word

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str]:
        token = list()
        for ch in text:
            if ch in cls.QUOTE_MARKS:
                token.append(ch)
            else:
                break
        return tuple(token)
