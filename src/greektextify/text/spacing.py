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
"""Class for dealing with expected spaces from a corpora."""
from typing import Tuple

from greektextify.text.immaterializer import TokenImmaterializableMixin


class Spacing(TokenImmaterializableMixin):
    CHARACTER_TABULATION = '\t'
    LINE_FEED = '\n'
    LINE_TABULATION = '\v'
    FORM_FEED = '\f'
    CARRIAGE_RETURN = '\r'
    SPACE = '\x20'

    DEBUG_SPACE = '\u20DF'  # Symbol for invisible space characters

    BLANK_SPACE = frozenset([
        CHARACTER_TABULATION, LINE_FEED, LINE_TABULATION, FORM_FEED, CARRIAGE_RETURN, SPACE
    ])

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str, ...]:
        token = list()
        for ch in text:
            if ch in cls.BLANK_SPACE:
                token.append(ch)
            else:
                break

        return tuple(token)
