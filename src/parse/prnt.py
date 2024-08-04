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
"""The Greek Koine combining diacritics."""
from typing import Tuple

from greektextify.nlp.contextual import NlpWarning
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from parse.alalc import Alalc
from parse.consonant import GreekConsonant
from parse.diphtong import GreekDiphthong
from parse.ngamma import GammaNasal
from parse.rmedial import MedialRho
from parse.vowel import GreekVowel
from parse.word import GreekWord


class PrintGreekRoman:

    @classmethod
    def format(cls, word: Tuple[GreekGlyph]) -> str:
        out = ""
        upper = False
        for chunk in GreekWord.analyze(word):
            if chunk.initial:
                upper = chunk.is_upper()
                if isinstance(chunk, GreekDiphthong):
                    out += Alalc.ALALC2010[Alalc.ROUGH] if chunk.is_rough() else ''
                    out += chunk.ALALC2010[chunk.pattern.raw]
                    if not chunk.is_proper(): out += 'i'
                elif isinstance(chunk, GreekVowel):
                    glyph = chunk.chunk[0]
                    out += Alalc.ALALC2010[Alalc.ROUGH] if glyph.rough else ''
                    out += Alalc.ALALC2010[glyph.lower]
                    if chunk.chunk[0].subscript: out += 'i'
                elif isinstance(chunk, GreekConsonant):
                    glyph = chunk.chunk[0]
                    if glyph.lower == GreekAlphabet.LOWER_RHO:
                        out += Alalc.ALALC2010[glyph.lower] + Alalc.ALALC2010[Alalc.ROUGH]
                    else:
                        out += Alalc.ALALC2010[glyph.lower]
                else:
                    raise NlpWarning(*NlpWarning.PROCESS_ERROR)
            else:
                if isinstance(chunk, GreekDiphthong):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                    if not chunk.is_proper(): out += 'i'
                elif isinstance(chunk, GreekVowel):
                    out += Alalc.ALALC2010[chunk.chunk[0].lower]
                    if chunk.chunk[0].subscript: out += 'i'
                elif isinstance(chunk, GammaNasal):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, MedialRho):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, GreekConsonant):
                    out += Alalc.ALALC2010[chunk.chunk[0].lower]
                else:
                    raise NlpWarning(*NlpWarning.PROCESS_ERROR)

        return out.title() if upper else out
