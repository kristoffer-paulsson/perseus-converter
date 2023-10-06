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
"""Betacode decoder into greek glyphs.

Following for standard: http://stephanus.tlg.uci.edu/encoding/BCM.pdf
"""
from typing import Tuple, List

from greektextify.beta.alphabet import BetaAlphabet
from greektextify.beta.diacritic import BetaDiacritic
from greektextify.nlp.contextual import NlpWarning
from greektextify.text.glyph import GreekGlyph


class BetaGlyph(GreekGlyph):

    @classmethod
    def combine(cls, chs: List["GreekGlyph"]) -> "GreekGlyph":
        ch = None
        psili = False
        dasia = False
        ypogegrammeni = False
        varia = False
        oxia = False
        perispomeni = False
        dialytika = False
        vrachy = False
        macron = False

        for gl in chs:
            if ch and gl.ch:
                raise NlpWarning(*NlpWarning.COMBINE_ERROR, {"chars": (ch, gl.ch)})

            ch = gl.ch if gl.ch else ch
            psili = True if gl.psili else psili
            dasia = True if gl.dasia else dasia
            ypogegrammeni = True if gl.ypogegrammeni else ypogegrammeni
            varia = True if gl.varia else varia
            oxia = True if gl.oxia else oxia
            perispomeni = True if gl.perispomeni else perispomeni
            dialytika = True if gl.dialytika else dialytika
            vrachy = True if gl.vrachy else vrachy
            macron = True if gl.macron else macron

        return GreekGlyph(ch, psili, dasia, ypogegrammeni, varia, oxia, perispomeni, dialytika, vrachy, macron)

    @classmethod
    def glyphen(cls, chs: str) -> Tuple["GreekGlyph", int]:
        position = 0
        combine = list()
        letter = ''
        upper = False

        if chs[position] == BetaAlphabet.UPPER_CASE:
            upper = True
            position += 1

            for ch in chs[position:]:
                if ch in BetaDiacritic.DIACRITICS:
                    combine.append(cls.diacritic(BetaDiacritic.BETA_DIACRITICS[ch]))
                    position += 1
                else:
                    break

        if chs[position] in BetaAlphabet.LATIN_CHARS:
            letter += chs[position]
            position += 1

        if position < len(chs):
            if chs[position] in BetaAlphabet.LATIN_NUMBERS:
                letter += chs[position]
                position += 1

        if letter in BetaAlphabet.BETA_LETTERS:
            combine.append(cls.diacritic(BetaAlphabet.BETA_LETTERS[letter][0 if upper else 1]))

        for ch in chs[position:]:
            if ch in BetaDiacritic.DIACRITICS:
                combine.append(cls.diacritic(BetaDiacritic.BETA_DIACRITICS[ch]))
                position += 1
            else:
                break

        if position == 0:
            raise NlpWarning(*NlpWarning.NON_GREEK_GLYPH, {"char": chs})
        return cls.combine(combine), position
