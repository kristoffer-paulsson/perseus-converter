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
"""Greek word alteration and analyzation."""
from greektextify.text.glyph import GreekGlyph
from parse.chunk import GlyphChunk
from parse.cluster import GlyphCluster
from parse.consonant import GreekConsonant
from parse.diphtong import GreekDiphthong
from parse.ngamma import GammaNasal
from parse.rmedial import MedialRho
from parse.vowel import GreekVowel


class GreekWord(GlyphCluster):

    SCAN_ANALYZER = (
        (GreekDiphthong, 1),
        (GreekVowel, 1),
        (GammaNasal, 2),
        (MedialRho, 2),
        (GreekConsonant, 1),
    )

    def __init__(self, syllables: tuple[GlyphCluster]):
        GlyphCluster.__init__(self, syllables)

    @classmethod
    def analyze(cls, glyphs: tuple[GreekGlyph, ...]) -> tuple[GlyphChunk, ...]:
        initial = True
        chunks = list()
        subject = glyphs

        while subject:
            for scanner, min_req in cls.SCAN_ANALYZER:
                if len(subject) < min_req:
                    continue

                chunk, size = scanner.scan(subject, initial)
                if chunk is not None:
                    chunks.append(chunk)
                    initial = False
                    subject = subject[size:]
                    break
            # if tmp == length:
            #    raise NlpWarning(*NlpWarning.PROCESS_ERROR, info={'subject': subject})
        return tuple(chunks)

    @classmethod
    def syllabify(cls, chunks: tuple[GlyphChunk]) -> tuple[GlyphCluster]:
        pass
