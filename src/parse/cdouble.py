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
"""Double Consonant consonant cluster."""
from __future__ import annotations

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from parse.chunk import GlyphChunk
from parse.consonant import GreekConsonant
from parse.pattern import GlyphPattern


class DoubleConsonant(GreekConsonant):
    SIGMA_DELTA = GreekAlphabet.LOWER_SIGMA + GreekAlphabet.LOWER_DELTA
    DELTA_SIGMA = GreekAlphabet.LOWER_DELTA + GreekAlphabet.LOWER_SIGMA
    DELTA_IOTA = GreekAlphabet.LOWER_DELTA + GreekAlphabet.LOWER_IOTA

    ZETA = frozenset([
        GlyphPattern(SIGMA_DELTA),
        GlyphPattern(DELTA_SIGMA),
        GlyphPattern(DELTA_IOTA)
    ])

    KAPPA_SIGMA = GreekAlphabet.LOWER_KAPPA + GreekAlphabet.LOWER_SIGMA
    GAMMA_SIGMA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_SIGMA
    CHI_SIGMA = GreekAlphabet.LOWER_CHI + GreekAlphabet.LOWER_SIGMA

    XI = frozenset([
        GlyphPattern(KAPPA_SIGMA),
        GlyphPattern(GAMMA_SIGMA),
        GlyphPattern(CHI_SIGMA)
    ])

    PI_SIGMA = GreekAlphabet.LOWER_PI + GreekAlphabet.LOWER_SIGMA
    BETA_SIGMA = GreekAlphabet.LOWER_BETA + GreekAlphabet.LOWER_SIGMA
    PHI_SIGMA = GreekAlphabet.LOWER_PHI + GreekAlphabet.LOWER_SIGMA

    PSI = frozenset([
        GlyphPattern(PI_SIGMA),
        GlyphPattern(BETA_SIGMA),
        GlyphPattern(PHI_SIGMA)
    ])

    DOUBLE_CONSONANT = frozenset(set(ZETA) | set(XI) | set(PSI))

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        cluster = glyphs[0:2]
        for pattern in cls.DOUBLE_CONSONANT:
            if pattern.same_lower(cluster):
                return cls(cluster, initial), 2
        return None, 0
