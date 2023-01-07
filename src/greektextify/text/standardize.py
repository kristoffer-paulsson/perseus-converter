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
"""Greek standardization of Koine unicode variants of spelling in the academic."""
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway
from greektextify.text.punctuation import GreekPunctuation


class Standardize:
    MODIFIER_LETTER_APOSTROPHE = '\u02BC'
    MIDDLE_DOT = '\u00B7'
    SEMICOLON = '\u003B'
    MODIFIER_LETTER_REVERSED_COMMA = '\u02BD'
    HYPHEN_MINUS = '\u002D'

    PDL_TRANSFORM = {
        ord(MODIFIER_LETTER_APOSTROPHE): ord(GreekMidway.APOSTROPHE),
        ord(MIDDLE_DOT): ord(GreekPunctuation.ANO_TELIA),
        ord(SEMICOLON): ord(GreekPunctuation.QUESTION_MARK),
        ord(MODIFIER_LETTER_REVERSED_COMMA): ord(GreekExtended.DASIA),
        ord(HYPHEN_MINUS): ord(GreekPunctuation.HYPHEN)
    }

    @classmethod
    def pdl(cls, text: str) -> str:
        return text.translate(cls.PDL_TRANSFORM)
