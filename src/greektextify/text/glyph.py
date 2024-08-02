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
"""Greek glyph representing main letter plus diacritics."""
from typing import Tuple, NamedTuple, List

from greektextify.nlp.contextual import NlpWarning
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway


class GlyphWarning(RuntimeWarning):
    """Warning regarding glyph."""
    pass


class GreekGlyph(NamedTuple):
    ch: str
    psili: bool
    dasia: bool
    ypogegrammeni: bool
    varia: bool
    oxia: bool
    perispomeni: bool
    dialytika: bool
    vrachy: bool
    macron: bool

    @property
    def valid(self) -> bool:
        return self in GREEK_GLYPH_COMBO

    @classmethod
    def glyphen(cls, chs: str) -> Tuple["GreekGlyph", int]:
        position = 0
        combine = list()

        for ch in chs:
            if ch in GreekExtended.DIACRITICS:
                combine.append(cls.diacritic(GreekExtended.EXPANDABLE_DIACRITICS[ch]))
            else:
                break
        position += len(combine)

        ch = chs[position] if position < len(chs) else None
        if ch in GreekAlphabet.ALPHABET:
            combine.append(cls.diacritic(ch))
        elif ch in GreekExtended.LETTERS:
            combine.append(cls.diacritic(GreekExtended.EXPANDABLE_LETTERS[ch]))
        elif ch in GreekMidway.LETTERS:
            combine.append(cls.diacritic(GreekMidway.EXPANDABLE_LETTERS[ch]))
        position = len(combine)

        for ch in chs[position:]:
            if ch in GreekDiacritic.DIACRITICS:
                combine.append(cls.diacritic(ch))
            else:
                break

        position = len(combine)
        if position == 0:
            raise NlpWarning(*NlpWarning.NON_GREEK_GLYPH, {"char": chs})
        return cls.combine(combine), position

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
            ch = gl.ch
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
    def diacritic(cls, ch: str) -> "GreekGlyph":
        return GreekGlyph(
            ch[0] if ch[0] in GreekAlphabet.ALPHABET else None,
            True if GreekDiacritic.COMBINING_PSILI in ch else False,
            True if GreekDiacritic.COMBINING_DASIA in ch else False,
            True if GreekDiacritic.COMBINING_YPOGEGRAMMENI in ch else False,
            True if GreekDiacritic.COMBINING_VARIA in ch else False,
            True if GreekDiacritic.COMBINING_OXIA in ch else False,
            True if GreekDiacritic.COMBINING_PERISPOMENI in ch else False,
            True if GreekDiacritic.COMBINING_DIALYTIKA in ch else False,
            True if GreekDiacritic.COMBINING_VRACHY in ch else False,
            True if GreekDiacritic.COMBINING_MACRON in ch else False,
        )


GREEK_GLYPH_COMBO = frozenset([
    GreekGlyph(GreekAlphabet.HYPHEN_MINUS, False, False, False, False, False, False, False, False, False),
    GreekGlyph(GreekMidway.APOSTROPHE, False, False, False, False, False, False, False, False, False),


    GreekGlyph('Α', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Α', False, False, False, False, False, False, False, False, True),
    GreekGlyph('Α', False, False, False, False, False, False, False, True, False),
    GreekGlyph('Α', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Α', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Α', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Α', False, False, True, False, False, False, False, False, False),
    GreekGlyph('Α', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Α', False, True, False, False, False, True, False, False, False),
    GreekGlyph('Α', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Α', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Α', False, True, True, False, False, False, False, False, False),
    GreekGlyph('Α', False, True, True, False, False, True, False, False, False),
    GreekGlyph('Α', False, True, True, False, True, False, False, False, False),
    GreekGlyph('Α', False, True, True, True, False, False, False, False, False),
    GreekGlyph('Α', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Α', True, False, False, False, False, True, False, False, False),
    GreekGlyph('Α', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Α', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Α', True, False, True, False, False, False, False, False, False),
    GreekGlyph('Α', True, False, True, False, False, True, False, False, False),
    GreekGlyph('Α', True, False, True, False, True, False, False, False, False),
    GreekGlyph('Α', True, False, True, True, False, False, False, False, False),
    GreekGlyph('Β', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Γ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Δ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ε', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ε', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ε', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ε', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Ε', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Ε', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Ε', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Ε', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Ε', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Ε', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Ζ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Η', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Η', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Η', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Η', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Η', False, False, True, False, False, False, False, False, False),
    GreekGlyph('Η', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Η', False, True, False, False, False, True, False, False, False),
    GreekGlyph('Η', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Η', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Η', False, True, True, False, False, False, False, False, False),
    GreekGlyph('Η', False, True, True, False, False, True, False, False, False),
    GreekGlyph('Η', False, True, True, False, True, False, False, False, False),
    GreekGlyph('Η', False, True, True, True, False, False, False, False, False),
    GreekGlyph('Η', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Η', True, False, False, False, False, True, False, False, False),
    GreekGlyph('Η', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Η', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Η', True, False, True, False, False, False, False, False, False),
    GreekGlyph('Η', True, False, True, False, False, True, False, False, False),
    GreekGlyph('Η', True, False, True, False, True, False, False, False, False),
    GreekGlyph('Η', True, False, True, True, False, False, False, False, False),
    GreekGlyph('Θ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ι', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ι', False, False, False, False, False, False, False, False, True),
    GreekGlyph('Ι', False, False, False, False, False, False, False, True, False),
    GreekGlyph('Ι', False, False, False, False, False, False, True, False, False),
    GreekGlyph('Ι', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ι', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ι', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Ι', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Ι', False, True, False, False, False, True, False, False, False),
    GreekGlyph('Ι', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Ι', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Ι', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Ι', True, False, False, False, False, True, False, False, False),
    GreekGlyph('Ι', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Ι', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Κ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Λ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Μ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ν', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ξ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ο', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ο', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ο', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ο', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Ο', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Ο', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Ο', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Ο', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Ο', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Ο', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Π', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ρ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ρ', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Σ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Τ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Υ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Υ', False, False, False, False, False, False, False, False, True),
    GreekGlyph('Υ', False, False, False, False, False, False, False, True, False),
    GreekGlyph('Υ', False, False, False, False, False, False, True, False, False),
    GreekGlyph('Υ', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Υ', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Υ', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Υ', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Υ', False, True, False, False, False, True, False, False, False),
    GreekGlyph('Υ', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Υ', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Φ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Χ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ψ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ω', False, False, False, False, False, False, False, False, False),
    GreekGlyph('Ω', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ω', False, False, False, False, True, False, False, False, False),
    GreekGlyph('Ω', False, False, False, True, False, False, False, False, False),
    GreekGlyph('Ω', False, False, True, False, False, False, False, False, False),
    GreekGlyph('Ω', False, True, False, False, False, False, False, False, False),
    GreekGlyph('Ω', False, True, False, False, False, True, False, False, False),
    GreekGlyph('Ω', False, True, False, False, True, False, False, False, False),
    GreekGlyph('Ω', False, True, False, True, False, False, False, False, False),
    GreekGlyph('Ω', False, True, True, False, False, False, False, False, False),
    GreekGlyph('Ω', False, True, True, False, False, True, False, False, False),
    GreekGlyph('Ω', False, True, True, False, True, False, False, False, False),
    GreekGlyph('Ω', False, True, True, True, False, False, False, False, False),
    GreekGlyph('Ω', True, False, False, False, False, False, False, False, False),
    GreekGlyph('Ω', True, False, False, False, False, True, False, False, False),
    GreekGlyph('Ω', True, False, False, False, True, False, False, False, False),
    GreekGlyph('Ω', True, False, False, True, False, False, False, False, False),
    GreekGlyph('Ω', True, False, True, False, False, False, False, False, False),
    GreekGlyph('Ω', True, False, True, False, False, True, False, False, False),
    GreekGlyph('Ω', True, False, True, False, True, False, False, False, False),
    GreekGlyph('Ω', True, False, True, True, False, False, False, False, False),
    GreekGlyph('α', False, False, False, False, False, False, False, False, False),
    GreekGlyph('α', False, False, False, False, False, False, False, False, True),
    GreekGlyph('α', False, False, False, False, False, False, False, True, False),
    GreekGlyph('α', False, False, False, False, False, True, False, False, False),
    GreekGlyph('α', False, False, False, False, True, False, False, False, False),
    GreekGlyph('α', False, False, False, False, True, False, False, False, False),
    GreekGlyph('α', False, False, False, True, False, False, False, False, False),
    GreekGlyph('α', False, False, True, False, False, False, False, False, False),
    GreekGlyph('α', False, False, True, False, False, True, False, False, False),
    GreekGlyph('α', False, False, True, False, True, False, False, False, False),
    GreekGlyph('α', False, False, True, True, False, False, False, False, False),
    GreekGlyph('α', False, True, False, False, False, False, False, False, False),
    GreekGlyph('α', False, True, False, False, False, True, False, False, False),
    GreekGlyph('α', False, True, False, False, True, False, False, False, False),
    GreekGlyph('α', False, True, False, True, False, False, False, False, False),
    GreekGlyph('α', False, True, True, False, False, False, False, False, False),
    GreekGlyph('α', False, True, True, False, False, True, False, False, False),
    GreekGlyph('α', False, True, True, False, True, False, False, False, False),
    GreekGlyph('α', False, True, True, True, False, False, False, False, False),
    GreekGlyph('α', True, False, False, False, False, False, False, False, False),
    GreekGlyph('α', True, False, False, False, False, True, False, False, False),
    GreekGlyph('α', True, False, False, False, True, False, False, False, False),
    GreekGlyph('α', True, False, False, True, False, False, False, False, False),
    GreekGlyph('α', True, False, True, False, False, False, False, False, False),
    GreekGlyph('α', True, False, True, False, False, True, False, False, False),
    GreekGlyph('α', True, False, True, False, True, False, False, False, False),
    GreekGlyph('α', True, False, True, True, False, False, False, False, False),
    GreekGlyph('β', False, False, False, False, False, False, False, False, False),
    GreekGlyph('γ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('δ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ε', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ε', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ε', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ε', False, False, False, True, False, False, False, False, False),
    GreekGlyph('ε', False, True, False, False, False, False, False, False, False),
    GreekGlyph('ε', False, True, False, False, True, False, False, False, False),
    GreekGlyph('ε', False, True, False, True, False, False, False, False, False),
    GreekGlyph('ε', True, False, False, False, False, False, False, False, False),
    GreekGlyph('ε', True, False, False, False, True, False, False, False, False),
    GreekGlyph('ε', True, False, False, True, False, False, False, False, False),
    GreekGlyph('ζ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('η', False, False, False, False, False, False, False, False, False),
    GreekGlyph('η', False, False, False, False, False, True, False, False, False),
    GreekGlyph('η', False, False, False, False, True, False, False, False, False),
    GreekGlyph('η', False, False, False, False, True, False, False, False, False),
    GreekGlyph('η', False, False, False, True, False, False, False, False, False),
    GreekGlyph('η', False, False, True, False, False, False, False, False, False),
    GreekGlyph('η', False, False, True, False, False, True, False, False, False),
    GreekGlyph('η', False, False, True, False, True, False, False, False, False),
    GreekGlyph('η', False, False, True, True, False, False, False, False, False),
    GreekGlyph('η', False, True, False, False, False, False, False, False, False),
    GreekGlyph('η', False, True, False, False, False, True, False, False, False),
    GreekGlyph('η', False, True, False, False, True, False, False, False, False),
    GreekGlyph('η', False, True, False, True, False, False, False, False, False),
    GreekGlyph('η', False, True, True, False, False, False, False, False, False),
    GreekGlyph('η', False, True, True, False, False, True, False, False, False),
    GreekGlyph('η', False, True, True, False, True, False, False, False, False),
    GreekGlyph('η', False, True, True, True, False, False, False, False, False),
    GreekGlyph('η', True, False, False, False, False, False, False, False, False),
    GreekGlyph('η', True, False, False, False, False, True, False, False, False),
    GreekGlyph('η', True, False, False, False, True, False, False, False, False),
    GreekGlyph('η', True, False, False, True, False, False, False, False, False),
    GreekGlyph('η', True, False, True, False, False, False, False, False, False),
    GreekGlyph('η', True, False, True, False, False, True, False, False, False),
    GreekGlyph('η', True, False, True, False, True, False, False, False, False),
    GreekGlyph('η', True, False, True, True, False, False, False, False, False),
    GreekGlyph('θ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ι', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ι', False, False, False, False, False, False, False, False, True),
    GreekGlyph('ι', False, False, False, False, False, False, False, True, False),
    GreekGlyph('ι', False, False, False, False, False, False, True, False, False),
    GreekGlyph('ι', False, False, False, False, False, True, False, False, False),
    GreekGlyph('ι', False, False, False, False, False, True, True, False, False),
    GreekGlyph('ι', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ι', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ι', False, False, False, False, True, False, True, False, False),
    GreekGlyph('ι', False, False, False, False, True, False, True, False, False),
    GreekGlyph('ι', False, False, False, True, False, False, False, False, False),
    GreekGlyph('ι', False, False, False, True, False, False, True, False, False),
    GreekGlyph('ι', False, True, False, False, False, False, False, False, False),
    GreekGlyph('ι', False, True, False, False, False, True, False, False, False),
    GreekGlyph('ι', False, True, False, False, True, False, False, False, False),
    GreekGlyph('ι', False, True, False, True, False, False, False, False, False),
    GreekGlyph('ι', True, False, False, False, False, False, False, False, False),
    GreekGlyph('ι', True, False, False, False, False, True, False, False, False),
    GreekGlyph('ι', True, False, False, False, True, False, False, False, False),
    GreekGlyph('ι', True, False, False, True, False, False, False, False, False),
    GreekGlyph('κ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('λ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('μ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ν', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ξ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ο', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ο', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ο', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ο', False, False, False, True, False, False, False, False, False),
    GreekGlyph('ο', False, True, False, False, False, False, False, False, False),
    GreekGlyph('ο', False, True, False, False, True, False, False, False, False),
    GreekGlyph('ο', False, True, False, True, False, False, False, False, False),
    GreekGlyph('ο', True, False, False, False, False, False, False, False, False),
    GreekGlyph('ο', True, False, False, False, True, False, False, False, False),
    GreekGlyph('ο', True, False, False, True, False, False, False, False, False),
    GreekGlyph('π', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ρ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ρ', False, True, False, False, False, False, False, False, False),
    GreekGlyph('ρ', True, False, False, False, False, False, False, False, False),
    GreekGlyph('ς', False, False, False, False, False, False, False, False, False),
    GreekGlyph('σ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('τ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('υ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('υ', False, False, False, False, False, False, False, False, True),
    GreekGlyph('υ', False, False, False, False, False, False, False, True, False),
    GreekGlyph('υ', False, False, False, False, False, False, True, False, False),
    GreekGlyph('υ', False, False, False, False, False, True, False, False, False),
    GreekGlyph('υ', False, False, False, False, False, True, True, False, False),
    GreekGlyph('υ', False, False, False, False, True, False, False, False, False),
    GreekGlyph('υ', False, False, False, False, True, False, False, False, False),
    GreekGlyph('υ', False, False, False, False, True, False, True, False, False),
    GreekGlyph('υ', False, False, False, False, True, False, True, False, False),
    GreekGlyph('υ', False, False, False, True, False, False, False, False, False),
    GreekGlyph('υ', False, False, False, True, False, False, True, False, False),
    GreekGlyph('υ', False, True, False, False, False, False, False, False, False),
    GreekGlyph('υ', False, True, False, False, False, True, False, False, False),
    GreekGlyph('υ', False, True, False, False, True, False, False, False, False),
    GreekGlyph('υ', False, True, False, True, False, False, False, False, False),
    GreekGlyph('υ', True, False, False, False, False, False, False, False, False),
    GreekGlyph('υ', True, False, False, False, False, True, False, False, False),
    GreekGlyph('υ', True, False, False, False, True, False, False, False, False),
    GreekGlyph('υ', True, False, False, True, False, False, False, False, False),
    GreekGlyph('φ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('χ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ψ', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ω', False, False, False, False, False, False, False, False, False),
    GreekGlyph('ω', False, False, False, False, False, True, False, False, False),
    GreekGlyph('ω', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ω', False, False, False, False, True, False, False, False, False),
    GreekGlyph('ω', False, False, False, True, False, False, False, False, False),
    GreekGlyph('ω', False, False, True, False, False, False, False, False, False),
    GreekGlyph('ω', False, False, True, False, False, True, False, False, False),
    GreekGlyph('ω', False, False, True, False, True, False, False, False, False),
    GreekGlyph('ω', False, False, True, True, False, False, False, False, False),
    GreekGlyph('ω', False, True, False, False, False, False, False, False, False),
    GreekGlyph('ω', False, True, False, False, False, True, False, False, False),
    GreekGlyph('ω', False, True, False, False, True, False, False, False, False),
    GreekGlyph('ω', False, True, False, True, False, False, False, False, False),
    GreekGlyph('ω', False, True, True, False, False, False, False, False, False),
    GreekGlyph('ω', False, True, True, False, False, True, False, False, False),
    GreekGlyph('ω', False, True, True, False, True, False, False, False, False),
    GreekGlyph('ω', False, True, True, True, False, False, False, False, False),
    GreekGlyph('ω', True, False, False, False, False, False, False, False, False),
    GreekGlyph('ω', True, False, False, False, False, True, False, False, False),
    GreekGlyph('ω', True, False, False, False, True, False, False, False, False),
    GreekGlyph('ω', True, False, False, True, False, False, False, False, False),
    GreekGlyph('ω', True, False, True, False, False, False, False, False, False),
    GreekGlyph('ω', True, False, True, False, False, True, False, False, False),
    GreekGlyph('ω', True, False, True, False, True, False, False, False, False),
    GreekGlyph('ω', True, False, True, True, False, False, False, False, False),
])

