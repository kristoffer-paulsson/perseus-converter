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
"""Greek alphabet vowels distinct in lowercase."""
from __future__ import annotations

from enum import Enum

from greektextify.nlp.contextual import NlpWarning
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from greektextify.text.midway import GreekMidway
from parse.chunk import GlyphChunk
from parse.scan import AbstractGlyphSearch


class IPAVowelLength(Enum):
    """IPA Vowel Length enumeration based on
    https://en.wikipedia.org/wiki/Vowel_length"""
    LONG = 0
    LONG_HALF = 1
    SHORT = 2
    SHORT_EXTRA = 3


class IPAVowelBackness(Enum):
    """IPA Vowel Backness enumeration based on
    https://en.wikipedia.org/wiki/Vowel"""
    FRONT = 0
    FRONT_NEAR = 1
    CENTRAL = 2
    BACK_NEAR = 3
    BACK = 4


class IPAVowelHeight(Enum):
    """IPA Vowel Height enumeration based on
    https://en.wikipedia.org/wiki/Vowel"""
    CLOSE = 0
    CLOSE_NEAR = 1
    CLOSE_MID = 2
    MID = 3
    OPEN_MID = 4
    OPEN_NEAR = 5
    OPEN = 6


class GreekVowel(GlyphChunk, AbstractGlyphSearch):
    """Koine vowels described as in Smyth grammar 1.1.2."""

    # Smyth § 4, even vowel length according to IPA.
    L_SHORT = frozenset([
        GreekAlphabet.LOWER_EPSILON,
        GreekAlphabet.LOWER_OMICRON
    ])

    L_LONG = frozenset([
        GreekAlphabet.LOWER_ETA,
        GreekAlphabet.LOWER_OMEGA
    ])

    L_VARIABLE = frozenset([
        GreekAlphabet.LOWER_ALPHA,
        GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_UPSILON
    ])

    L_NOT_SHORT = frozenset(set(L_LONG) | set(L_VARIABLE))
    # Only not short vowels may have a circumflex: https://en.wikipedia.org/wiki/Greek_diacritics

    # Smyth § 7, even vowel height according to IPA.
    H_OPEN = frozenset([
        GreekAlphabet.LOWER_ALPHA
    ])

    H_OPEN_MID = frozenset([
        GreekAlphabet.LOWER_ETA,
        GreekAlphabet.LOWER_OMEGA
    ])

    H_CLOSE_MID = frozenset([
        GreekAlphabet.LOWER_EPSILON,
        GreekAlphabet.LOWER_OMICRON
    ])

    H_CLOSE = frozenset([
        GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_UPSILON
    ])

    #Smyth § 7, even wovel backness according to IPA.

    B_FRONT = frozenset([
        GreekAlphabet.LOWER_ETA,
        GreekAlphabet.LOWER_EPSILON,

    ])

    B_CENTRAL = frozenset([
        GreekAlphabet.LOWER_ALPHA
    ])

    B_BACK = frozenset([
        GreekAlphabet.LOWER_OMEGA,
        GreekAlphabet.LOWER_OMICRON
    ])

    B_VARIABLE = frozenset([
       GreekAlphabet.LOWER_IOTA,
       GreekAlphabet.LOWER_UPSILON
    ])

    VOWELS = frozenset(set(L_SHORT) | set(L_LONG) | set(L_VARIABLE) | {GreekMidway.APOSTROPHE})

    def _get_diacritic_glyph(self) -> GreekGlyph:
        """Gives the current vowel."""
        return self.chunk[0]

    def is_upper(self) -> bool:
        return self.chunk[0].ch.isupper()

    def is_rough(self) -> bool:
        """Tells if said vowel has rough breathing.
        Based on Smyth § 9 and 10."""
        glyph = self._get_diacritic_glyph()
        if self.initial and glyph.lower == GreekAlphabet.LOWER_UPSILON:
            return True
        else:
            return glyph.asper

    def is_smooth(self) -> bool:
        """Tells if said vowel has smooth breathing.
        Based on Smyth § 9 and 10."""
        return self._get_diacritic_glyph().lenis

    def check_diaeresis(self) -> bool:
        """Checks that diaeresis only appear on upsilon and iota, nevertheless others.
        Should be considered a grammatical error, inverted from Smyth § 8."""
        return not (self.chunk[0].lower not in (
            GreekAlphabet.LOWER_IOTA, GreekAlphabet.LOWER_UPSILON) and self.chunk[0].diaeresis)

    def check_asper_lenis(self) -> bool:
        """Checks that asper and lenis doesn't apply on the same time.
        Should be considered a grammatical error, inverted from Smyth § 9."""
        glyph = self._get_diacritic_glyph()
        return not (glyph.asper and glyph.lenis)

    def check_upsilon_lenis(self) -> bool:
        """Checks that initial upsilon doesn't have a lenis.
        Should be considered a grammatical error, inverted from Smyth § 10."""
        return not (self.initial and self.chunk[0].lower == GreekAlphabet.LOWER_UPSILON and self.chunk[0].lenis)

    @staticmethod
    def is_vowel(glyph: GreekGlyph) -> bool:
        """Tells if a glyph is a vowel.
        Based on Smyth § 4."""
        return glyph.lower in GreekVowel.VOWELS

    @classmethod
    def vowel_length(cls, glyph: GreekGlyph) -> IPAVowelLength:
        """Tells if a vowel is short (true) or long (false).
        The glyph is expected to be a verified vowel.
        Based on Smyth § 4 and https://en.wikipedia.org/wiki/Greek_diacritics, § 144 & § 149 Not yet implemented."""
        ch = glyph.ch.lower()
        if ch in cls.L_SHORT:
            return IPAVowelLength.SHORT
        elif ch in cls.L_NOT_SHORT and glyph.perispomeni:
            return IPAVowelLength.LONG
        elif ch in cls.L_VARIABLE:
            return IPAVowelLength.SHORT if not glyph.macron else IPAVowelLength.LONG
        elif ch in cls.L_LONG:
            return IPAVowelLength.LONG
        else:
            raise NlpWarning(*NlpWarning.NOT_VOWEL)

    @classmethod
    def vowel_height(cls, glyph: GreekGlyph) -> IPAVowelHeight:
        """Tells the height of a vowel, based on Smyth § 7 and
        https://en.wikipedia.org/wiki/Vowel_length"""
        ch = glyph.ch.lower()
        if ch in cls.H_OPEN:
            return IPAVowelHeight.OPEN
        elif ch in cls.H_OPEN_MID:
            return IPAVowelHeight.OPEN_MID
        elif ch in cls.H_CLOSE_MID:
            return IPAVowelHeight.CLOSE_MID
        elif ch in cls.H_CLOSE:
            return IPAVowelHeight.CLOSE
        else:
            raise NlpWarning(*NlpWarning.NOT_VOWEL)

    @classmethod
    def vowel_backness(cls, glyph: GreekGlyph) -> IPAVowelBackness:
        """Tells the backness of a vowel, based on Smyth § 7 and
        https://en.wikipedia.org/wiki/Vowel"""
        raise NotImplemented()

    @classmethod
    def valid_diaeresis(cls, glyph: GreekGlyph) -> bool:
        """Presumes that the vowel is not part of a diphthong and applies Smyth § 8."""
        return glyph.lower in (GreekAlphabet.LOWER_IOTA, GreekAlphabet.LOWER_UPSILON) and glyph.dialytika

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        cluster = glyphs[0]
        for vowel in cls.VOWELS:
            if cluster.lower == vowel:
                return cls(glyphs[0:1], initial), 1
        return None, 0
