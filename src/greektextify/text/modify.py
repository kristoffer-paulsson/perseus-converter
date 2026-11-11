#
# Copyright (c) 2026 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Modification of spelling and glyphs for ancient Greek."""
from typing import Tuple, List, Callable

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.database import GreekDatabase
from greektextify.text.glyph import GreekGlyph
from greektextify.text.midway import GreekMidway
from greektextify.text.prnt import PrintGreek
from greektextify.text.word import GreekWord


class WordModifier:

    EXTRAS = (
        GreekMidway.APOSTROPHE,
        GreekMidway.MODIFIER_PRIME,
        GreekAlphabet.HYPHEN_MINUS
    )

    @staticmethod
    def stringify(token: str, op: Callable[[Tuple[GreekGlyph]], Tuple[GreekGlyph]]) -> str:
        return PrintGreek.format(op(GreekWord.glyphen(token)))

    @staticmethod
    def _fix_final(token: List[GreekGlyph]) -> List[GreekGlyph]:
        """In place modification, fixes final sigma"""
        if token[-1].ch == GreekAlphabet.LOWER_SIGMA:
            token[-1] = GreekDatabase.LOWER_FINAL_SIGMA[1]

        return token

    @staticmethod
    def lunate(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Modifying glyphs from lunate to sigma"""
        out = list()

        for glyph in token:
            if glyph.ch == GreekAlphabet.LOWER_LUNATE:
                out.append(GreekDatabase.LOWER_SIGMA[1])
            elif glyph.ch == GreekAlphabet.UPPER_LUNATE:
                out.append(GreekDatabase.UPPER_SIGMA[1])
            else:
                out.append(glyph)

        return tuple(WordModifier._fix_final(out))

    @staticmethod
    def final(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Fixing last sigma to final sigma"""
        return tuple(WordModifier._fix_final(list(token.__iter__())))

    @staticmethod
    def deaccent(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Remove accentuation but preserves other diacritics"""
        out = list()

        for glyph in token.__iter__():
            out.append(GreekGlyph(
                glyph.ch, psili=glyph.psili, dasia=glyph.dasia,
                ypogegrammeni=glyph.ypogegrammeni, dialytika=glyph.dialytika
            ))

        return tuple(out)

    @staticmethod
    def _to_lower(ch: int) -> int:
        """Internally lowercases with respect for special characters"""
        return ch if ch in GreekAlphabet.CASE_LOWER or ch in WordModifier.EXTRAS else GreekAlphabet.to_lower(ch)

    @staticmethod
    def search_token(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Strips all diacritics and lowercasing"""
        out = list()

        for glyph in token.__iter__():
            out.append(GreekGlyph(WordModifier._to_lower(glyph.ch)))

        return tuple(WordModifier._fix_final(out))

    @staticmethod
    def _merge(ch: int, diacritics: GreekGlyph) -> GreekGlyph:
        """Merges a Unicode codepoint with diacritics from given glyph"""
        return GreekGlyph(
            ch,
            psili=diacritics.psili,
            dasia=diacritics.dasia,
            ypogegrammeni=diacritics.ypogegrammeni,
            varia=diacritics.varia,
            oxia=diacritics.oxia,
            perispomeni=diacritics.perispomeni,
            dialytika=diacritics.dialytika,
            vrachy=diacritics.vrachy,
            macron=diacritics.macron
        )

    @staticmethod
    def lower(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Lowercases a word and fixes final sigma"""
        out = list()

        for glyph in token.__iter__():
            out.append(WordModifier._merge(WordModifier._to_lower(glyph.ch), glyph))

        return tuple(WordModifier._fix_final(out))

    @staticmethod
    def _to_upper(ch: int) -> int:
        """Internally uppercases with respect for special characters"""
        return ch if ch in GreekAlphabet.CASE_UPPER or ch in WordModifier.EXTRAS else GreekAlphabet.to_upper(ch)

    @staticmethod
    def upper(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Uppercases a word"""
        out = list()

        for glyph in token.__iter__():
            out.append(WordModifier._merge(WordModifier._to_upper(glyph.ch), glyph))

        return tuple(out)

    @staticmethod
    def capitalize(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Uppercasing initial letter and lowercasing the rest"""
        out = list()
        initial = True

        for glyph in token.__iter__():
            if initial:
                out.append(WordModifier._merge(WordModifier._to_upper(glyph.ch), glyph))
                initial = False
            else:
                out.append(WordModifier._merge(WordModifier._to_lower(glyph.ch), glyph))

        return tuple(WordModifier._fix_final(out))