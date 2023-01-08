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
"""Greek punctuation combining and spacing with conversion built in."""
from typing import Tuple

from greektextify.text.immaterializer import TokenImmaterializableMixin


class GreekPunctuation(TokenImmaterializableMixin):
    """Greek punctuations."""

    FULL_STOP = '\u002E'
    COMMA = '\u002C'
    QUESTION_MARK = '\u037E'
    ANO_TELIA = '\u0387'
    HYPHEN = '\u2010'
    EM_DASH = '\u2014'

    PUNCT_MARKS = frozenset([
        FULL_STOP, COMMA, QUESTION_MARK, ANO_TELIA, HYPHEN, EM_DASH
    ])

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str]:
        if len(text) > 0:
            return tuple(text[0]) if text[0] in cls.PUNCT_MARKS else tuple()
        return tuple()
