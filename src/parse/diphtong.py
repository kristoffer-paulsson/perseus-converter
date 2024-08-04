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
"""Greek diphthongs representing two vowels or more."""
from __future__ import annotations

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.glyph import GreekGlyph
from .alalc import Alalc
from .chunk import GlyphChunk
from .pattern import GlyphPattern
from .vowel import GreekVowel


class GreekDiphthong(GreekVowel):

    ALPHA_IOTA = GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_IOTA
    EPSILON_IOTA = GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_IOTA
    OMICRON_IOTA = GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_IOTA
    # Should ALPHA_MACRON_SUBSCRIPT exist, different from Smyth § 5, ALPHA_SUBSCRIPT is indicated.
    ALPHA_SUBSCRIPT = GreekAlphabet.LOWER_ALPHA + GreekDiacritic.COMBINING_MACRON + GreekDiacritic.COMBINING_YPOGEGRAMMENI
    ETA_SUBSCRIPT = GreekAlphabet.LOWER_ETA + GreekDiacritic.COMBINING_YPOGEGRAMMENI
    OMEGA_SUBSCRIPT = GreekAlphabet.LOWER_OMEGA + GreekDiacritic.COMBINING_YPOGEGRAMMENI

    ALPHA_UPSILON = GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_UPSILON
    EPSILON_UPSILON = GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_UPSILON
    OMICRON_UPSILON = GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_UPSILON
    ETA_UPSILON = GreekAlphabet.LOWER_ETA + GreekAlphabet.LOWER_UPSILON

    UPSILON_IOTA = GreekAlphabet.LOWER_UPSILON + GreekAlphabet.LOWER_IOTA

    # Not mentioned in Smyth until found
    # OMEGA_UPSILON = GreekAlphabet.LOWER_OMEGA + GreekAlphabet.LOWER_UPSILON

    IMPROPER = frozenset([
        GlyphPattern(ALPHA_SUBSCRIPT),
        GlyphPattern(ETA_SUBSCRIPT),
        GlyphPattern(OMEGA_SUBSCRIPT),
    ])

    PROPER = frozenset([
        GlyphPattern(ALPHA_IOTA),
        GlyphPattern(EPSILON_IOTA),
        GlyphPattern(OMICRON_IOTA),
        GlyphPattern(ALPHA_UPSILON),
        GlyphPattern(EPSILON_UPSILON),
        GlyphPattern(OMICRON_UPSILON),
        GlyphPattern(ETA_UPSILON),
        GlyphPattern(UPSILON_IOTA),
        # GlyphPattern(OMEGA_UPSILON)
    ])

    ALALC2010 = {
        ALPHA_IOTA: Alalc.ALALC2010[GreekAlphabet.LOWER_ALPHA] + Alalc.ALALC2010[GreekAlphabet.LOWER_IOTA],
        EPSILON_IOTA: Alalc.ALALC2010[GreekAlphabet.LOWER_EPSILON] + Alalc.ALALC2010[GreekAlphabet.LOWER_IOTA],
        OMICRON_IOTA: Alalc.ALALC2010[GreekAlphabet.LOWER_OMICRON] + Alalc.ALALC2010[GreekAlphabet.LOWER_IOTA],
        ALPHA_SUBSCRIPT: Alalc.ALALC2010[GreekAlphabet.LOWER_ALPHA],
        ETA_SUBSCRIPT: Alalc.ALALC2010[GreekAlphabet.LOWER_ETA],
        OMEGA_SUBSCRIPT: Alalc.ALALC2010[GreekAlphabet.LOWER_OMEGA],
        ALPHA_UPSILON: Alalc.ALALC2010[GreekAlphabet.LOWER_ALPHA] + 'u',
        EPSILON_UPSILON: Alalc.ALALC2010[GreekAlphabet.LOWER_EPSILON] + 'u',
        OMICRON_UPSILON: Alalc.ALALC2010[GreekAlphabet.LOWER_OMICRON] + 'u',
        ETA_UPSILON: Alalc.ALALC2010[GreekAlphabet.LOWER_ETA] + 'u',
        UPSILON_IOTA: 'u' + Alalc.ALALC2010[GreekAlphabet.LOWER_IOTA],
        # OMEGA_UPSILON: GreekAlphabet.ALALC2010[GreekAlphabet.LOWER_OMEGA] + 'u',
    }

    def __init__(self, chunk: tuple[GreekGlyph], pattern: GlyphPattern, initial: bool = False):
        super().__init__(chunk, initial)
        self._pattern = pattern

    @property
    def pattern(self) -> GlyphPattern:
        return self._pattern

    def _get_diacritic_glyph(self) -> GreekGlyph:
        """Gives the glyph which should have the diacritics.
        Based in Smyth § 11 and 152."""
        if self._pattern.raw == self.ALPHA_IOTA and self.chunk[0].ch == GreekAlphabet.UPPER_ALPHA:
            return self.chunk[0]
        elif self.is_proper():
            return self.chunk[1]
        else:
            return self.chunk[0]

    def is_rough(self) -> bool:
        """Tells if said vowel has rough breathing.
        Based on Smyth § 9 and 11."""
        return self._get_diacritic_glyph().asper

    def is_smooth(self) -> bool:
        """Tells if said vowel has rough breathing.
        Based on Smyth § 9 and 11."""
        return self._get_diacritic_glyph().lenis

    def is_genuine(self) -> bool:
        """Tells whether EPSILON_IOTA or OMICRON_UPSILON are genuine or spurious, based on Smyth § 6."""
        return True

    def is_spurious(self) -> bool:
        """Tells whether EPSILON_IOTA or OMICRON_UPSILON are genuine or spurious, based on Smyth § 6."""
        return False

    def is_proper(self) -> bool:
        """Tells if a diphthong is inverted improper, based on Smyth § 5."""
        return not self._chunk[0].subscript

    def is_short(self) -> bool:
        """Tells if a diphthong is short (a property of vowels), based on Smyth § 5."""
        return False

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        cluster = glyphs[0:1]
        for pattern in cls.IMPROPER:
            if pattern.same(cluster):
                return cls(glyphs[0:1], pattern, initial), 1

        if len(glyphs) <= 1:
            return None, 0

        # According to Smyth § 8, if a diphthong has diaeresis over iota or upsilon, those are distinguished vowels.
        if glyphs[1].diaeresis:
            return None, 0

        cluster = glyphs[0:2]
        for pattern in cls.PROPER:
            if pattern.same_lower(cluster):
                return cls(cluster, pattern, initial), 2

        return None, 0




