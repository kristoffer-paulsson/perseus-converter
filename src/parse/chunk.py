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
"""Chunk of glyphs from a technical perspective."""
from greektextify.text.glyph import GreekGlyph


class GlyphChunk:

    def __init__(self, chunk: tuple[GreekGlyph], initial: bool = False):
        self._chunk = chunk
        self._initial = initial

    @property
    def chunk(self) -> tuple[GreekGlyph]:
        return self._chunk

    @property
    def initial(self) -> bool:
        return self._initial

    def is_upper(self) -> bool:
        return self._chunk[0].ch.isupper()

    def __repr__(self) -> str:
        return str("".join(str(x) for x in self._chunk))

