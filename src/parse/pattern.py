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
"""Glyph pattern classes."""
from greektextify.text.glyph import GreekGlyph
from greektextify.text.word import GreekWord as GW1


class GlyphPattern:

    def __init__(self, pattern: str):
        self._raw = pattern
        self._glyphs = GW1.glyphen(pattern)

    @property
    def raw(self) -> str:
        return self._raw

    @property
    def glyphs(self) -> tuple[GreekGlyph]:
        return self._glyphs

    def same(self, glyphs: tuple[GreekGlyph]) -> bool:
        return self._glyphs == glyphs

    def same_lower(self, glyphs: tuple[GreekGlyph]) -> bool:
        if len(self._glyphs) != len(glyphs):
            return False

        for s, g in zip(self._glyphs, glyphs):
            if not s.same(g):
                return False

        return True
