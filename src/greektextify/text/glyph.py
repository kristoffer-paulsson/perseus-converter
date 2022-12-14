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
            raise GlyphWarning("The following characters are not tokens belonging to the Greek word: '{}'".format(chs))
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
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, False, False, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, False, False, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, False, True, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, True, False, False, False),
        GreekGlyph('??', False, False, True, False, True, False, False, False, False),
        GreekGlyph('??', False, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, True, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, True, False, False, False),
        GreekGlyph('??', False, False, True, False, True, False, False, False, False),
        GreekGlyph('??', False, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, False, False, True, False, False),
        GreekGlyph('??', False, False, False, False, False, True, False, False, False),
        GreekGlyph('??', False, False, False, False, False, True, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, True, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, True, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, True),
        GreekGlyph('??', False, False, False, False, False, False, False, True, False),
        GreekGlyph('??', False, False, False, False, False, False, True, False, False),
        GreekGlyph('??', False, False, False, False, False, True, False, False, False),
        GreekGlyph('??', False, False, False, False, False, True, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, True, False, False),
        GreekGlyph('??', False, False, False, False, True, False, True, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, True, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, False, False, False, False),
        GreekGlyph('??', False, False, False, False, False, True, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, False, True, False, False, False, False),
        GreekGlyph('??', False, False, False, True, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, False, False, False, False),
        GreekGlyph('??', False, False, True, False, False, True, False, False, False),
        GreekGlyph('??', False, False, True, False, True, False, False, False, False),
        GreekGlyph('??', False, False, True, True, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, False, False, False, False),
        GreekGlyph('??', False, True, False, False, False, True, False, False, False),
        GreekGlyph('??', False, True, False, False, True, False, False, False, False),
        GreekGlyph('??', False, True, False, True, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, False, False, False, False),
        GreekGlyph('??', False, True, True, False, False, True, False, False, False),
        GreekGlyph('??', False, True, True, False, True, False, False, False, False),
        GreekGlyph('??', False, True, True, True, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, False, False, False, False),
        GreekGlyph('??', True, False, False, False, False, True, False, False, False),
        GreekGlyph('??', True, False, False, False, True, False, False, False, False),
        GreekGlyph('??', True, False, False, True, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, False, False, False, False),
        GreekGlyph('??', True, False, True, False, False, True, False, False, False),
        GreekGlyph('??', True, False, True, False, True, False, False, False, False),
        GreekGlyph('??', True, False, True, True, False, False, False, False, False),
    ])
