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
from typing import Tuple

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.database import GreekDatabase
from greektextify.text.glyph import GreekGlyph


class WordModifier:

    @staticmethod
    def lunate(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Modifying glyphs from lunate to sigma"""
        out = list()

        for glyph in token:
            if glyph.ch == GreekAlphabet.LOWER_LUNATE:
                out.append(GreekDatabase.LOWER_SIGMA)
            elif glyph.ch == GreekAlphabet.UPPER_LUNATE:
                out.append(GreekDatabase.UPPER_SIGMA)
            else:
                out.append(glyph)

        if out[-1].ch == GreekAlphabet.LOWER_SIGMA:
            out[-1] = GreekDatabase.LOWER_FINAL_SIGMA

        return tuple(out)

    @staticmethod
    def final(token: Tuple[GreekGlyph]) -> Tuple[GreekGlyph]:
        """Fixing last sigma to final sigma"""
        out = list(token.__iter__())

        if out[-1].ch == GreekAlphabet.LOWER_SIGMA:
            out[-1] = GreekDatabase.LOWER_FINAL_SIGMA[1]

        return tuple(out)