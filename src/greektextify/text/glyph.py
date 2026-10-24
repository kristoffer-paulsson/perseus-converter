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
    ch: int
    psili: bool = False             # smooth breathing / spiritus lenis
    dasia: bool = False             # rough breathing / spiritus asper / coronis
    ypogegrammeni: bool = False     # iota subscript
    varia: bool = False             # grave
    oxia: bool = False              # acute
    perispomeni: bool = False       # circumflex
    dialytika: bool = False         # diaresis / trema
    vrachy: bool = False            # breve
    macron: bool = False            # macron

    @property
    def smooth(self) -> bool:
        """Another name for psili."""
        return self.psili

    @property
    def lenis(self) -> bool:
        """Another name for psili."""
        return self.psili

    @property
    def rough(self) -> bool:
        """Another name for dasia."""
        return self.dasia

    @property
    def asper(self) -> bool:
        """Another name for dasia."""
        return self.dasia

    @property
    def coronis(self) -> bool:
        """Another name for dasia."""
        return self.dasia

    @property
    def subscript(self) -> bool:
        """Another name for ypogegrammeni."""
        return self.ypogegrammeni

    @property
    def grave(self) -> bool:
        """Another name for varia."""
        return self.varia

    @property
    def acute(self) -> bool:
        """Another name for oxia."""
        return self.oxia

    @property
    def circumflex(self) -> bool:
        """Another name for perispomeni."""
        return self.perispomeni

    @property
    def diaeresis(self) -> bool:
        """Another name for dialytika."""
        return self.dialytika

    @property
    def trema(self) -> bool:
        """Another name for dialytika."""
        return self.dialytika

    @property
    def breve(self) -> bool:
        """Another name for vrachy."""
        return self.vrachy

    @property
    def lower(self) -> str:
        return chr(self.ch).lower()

    def same(self, other: 'GreekGlyph') -> bool:
        return self.lower == other.lower

    @classmethod
    def glyphen(cls, chs: str) -> Tuple["GreekGlyph", int]:
        position = 0
        combine = list()

        for ch in chs:
            cp = ord(ch)
            if cp in GreekExtended.DIACRITICS:
                combine.append(cls.diacritic(GreekExtended.EXPANDABLE_DIACRITICS[cp]))
            else:
                break
        position += len(combine)

        cp = ord(chs[position]) if position < len(chs) else None
        if cp in GreekAlphabet.ALPHABET:
            combine.append(cls.diacritic((cp,)))
        elif cp in GreekExtended.LETTERS:
            combine.append(cls.diacritic(GreekExtended.EXPANDABLE_LETTERS[cp]))
        elif cp in GreekMidway.LETTERS:
            combine.append(cls.diacritic(GreekMidway.EXPANDABLE_LETTERS[cp]))
        position = len(combine)

        for ch in chs[position:]:
            cp = ord(ch)
            if cp in GreekDiacritic.DIACRITICS:
                combine.append(cls.diacritic((cp,)))
            else:
                break

        position = len(combine)
        if position == 0:
            raise NlpWarning(*NlpWarning.NON_GREEK_GLYPH, info = {"char": chs})
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
    def diacritic(cls, cps: Tuple[int, ...]) -> "GreekGlyph":
        return GreekGlyph(
            cps[0] if cps[0] in GreekAlphabet.ALPHABET else None,
            True if GreekDiacritic.COMBINING_PSILI in cps else False,
            True if GreekDiacritic.COMBINING_DASIA in cps else False,
            True if GreekDiacritic.COMBINING_YPOGEGRAMMENI in cps else False,
            True if GreekDiacritic.COMBINING_VARIA in cps else False,
            True if GreekDiacritic.COMBINING_OXIA in cps else False,
            True if GreekDiacritic.COMBINING_PERISPOMENI in cps else False,
            True if GreekDiacritic.COMBINING_DIALYTIKA in cps else False,
            True if GreekDiacritic.COMBINING_VRACHY in cps else False,
            True if GreekDiacritic.COMBINING_MACRON in cps else False,
        )

    def cmp_all(self, other: "GreekGlyph", ignore_case: bool = False) -> bool:
        same = self.cmp_semi(other, ignore_case)
        same = same if self.varia == other.varia else False
        same = same if self.oxia == other.oxia else False
        same = same if self.perispomeni == other.perispomeni else False
        same = same if self.vrachy == other.vrachy else False
        same = same if self.macron == other.macron else False

        return same

    def cmp_semi(self, other: "GreekGlyph", ignore_case: bool = False) -> bool:
        same = self.cmp_case(other, ignore_case)
        same = same if self.psili == other.psili else False
        same = same if self.dasia == other.dasia else False
        same = same if self.ypogegrammeni == other.ypogegrammeni else False
        same = same if self.dialytika == other.dialytika else False

        return same

    def cmp_case(self, other: "GreekGlyph", ignore_case: bool = False) -> bool:
        if ignore_case:
            return self.lower == other.lower
        else:
            return self.ch == other.ch