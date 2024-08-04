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
"""Gamma Nasal consonant cluster."""
from __future__ import annotations

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from parse.alalc import Alalc
from parse.chunk import GlyphChunk
from parse.consonant import GreekConsonant
from parse.pattern import GlyphPattern


class GammaNasal(GreekConsonant):
    GAMMA_KAPPA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_KAPPA
    GAMMA_GAMMA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_GAMMA
    GAMMA_CHI = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_CHI
    GAMMA_XI = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_XI

    GAMMA_NASAL = frozenset([
        GlyphPattern(GAMMA_KAPPA),
        GlyphPattern(GAMMA_GAMMA),
        GlyphPattern(GAMMA_CHI),
        GlyphPattern(GAMMA_XI)
    ])

    ALALC2010 = {
        GAMMA_KAPPA: Alalc.ALALC2010[GreekAlphabet.LOWER_NU] + Alalc.ALALC2010[GreekAlphabet.LOWER_KAPPA],
        GAMMA_GAMMA: Alalc.ALALC2010[GreekAlphabet.LOWER_NU] + Alalc.ALALC2010[GreekAlphabet.LOWER_GAMMA],
        GAMMA_CHI: Alalc.ALALC2010[GreekAlphabet.LOWER_NU] + Alalc.ALALC2010[GreekAlphabet.LOWER_CHI],
        GAMMA_XI: Alalc.ALALC2010[GreekAlphabet.LOWER_NU] + Alalc.ALALC2010[GreekAlphabet.LOWER_XI],
    }

    def __init__(self, chunk: tuple[GreekGlyph], pattern: GlyphPattern, initial: bool = False):
        super().__init__(chunk, initial)
        self._pattern = pattern

    @property
    def pattern(self) -> GlyphPattern:
        return self._pattern

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        cluster = glyphs[0:2]
        for pattern in cls.GAMMA_NASAL:
            if pattern.same_lower(cluster):
                return cls(cluster, pattern, initial), 2
        return None, 0
