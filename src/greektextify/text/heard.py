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


class GreekHeard(TokenImmaterializableMixin):
    """Bracketing parser."""

    BREVE = '\u02D8'
    GREEK_LUNATE_SIGMA_SYMBOL = '\u03F2'
    GREEK_SMALL_LETTER_DIGAMMA = '\u03DD'
    GREEK_SMALL_LETTER_STIGMA = '\u03DB'

    HEARD_OF = frozenset([
        BREVE, GREEK_LUNATE_SIGMA_SYMBOL, GREEK_SMALL_LETTER_DIGAMMA, GREEK_SMALL_LETTER_STIGMA
    ])

    def __init__(self, word: str):
        self._word = word

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str, ...]:
        token = list()
        for ch in text:
            if ch in cls.HEARD_OF:
                token.append(ch)
            else:
                break
        return tuple(token)
