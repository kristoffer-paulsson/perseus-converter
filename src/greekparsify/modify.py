#
# Copyright (c) 2024 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Ancient Greek modifiers."""
from types import MappingProxyType
from typing import Tuple

from greekparsify.inflect import Inflect
from greektextify.text.glyph import GreekGlyph
from greektextify.text.word import GreekWord


class Articles:
    """"""

    # Case - Gender - Number

    # NOM - Nominative case
    # GEN - genitive
    # DAT - Dative
    # ACC - accusative case
    # VOC - Vocative

    # MASC - masculine
    # FEM - feminine
    # NEU - neuter

    # SG - singular
    # DU - dual
    # PL - plural

    NOM_MASC_SG = 'ὁ'
    GEN_MASC_SG = 'τοῦ'
    DAT_MASC_SG = 'τῷ'
    ACC_MASC_SG = 'τόν'

    NOM_MASC_DU = 'τώ'  # Wikipedia unchecked
    GEN_MASC_DU = 'τοῖν'  # Wikipedia unchecked
    DAT_MASC_DU = 'τοῖν'  # Wikipedia unchecked
    ACC_MASC_DU = 'τώ'  # Wikipedia unchecked

    VOC_MASC_PL = 'οἱ'
    NOM_MASC_PL = 'οἱ'
    GEN_MASC_PL = 'τῶν'
    DAT_MASC_PL = 'τοῖς'
    ACC_MASC_PL = 'τούς'

    NOM_FEM_SG = 'ἡ'
    GEN_FEM_SG = 'τῆς'
    DAT_FEM_SG = 'τῇ'
    ACC_FEM_SG = 'τήν'

    NOM_FEM_DU = 'τώ'  # Wikipedia unchecked
    GEN_FEM_DU = 'τοῖν'  # Wikipedia unchecked
    DAT_FEM_DU = 'τοῖν'  # Wikipedia unchecked
    ACC_FEM_DU = 'τώ'  # Wikipedia unchecked

    VOC_FEM_PL = 'αἱ'
    NOM_FEM_PL = 'αἱ'
    GEN_FEM_PL = 'τῶν'
    DAT_FEM_PL = 'ταῖς'
    ACC_FEM_PL = 'τάς'  # 'τᾱς'  # error from wikipedia, checked against Mounce 13.1

    NOM_NEU_SG = 'τό'
    GEN_NEU_SG = 'τοῦ'
    DAT_NEU_SG = 'τῷ'
    ACC_NEU_SG = 'τό'

    NOM_NEU_DU = 'τώ'  # Wikipedia unchecked
    GEN_NEU_DU = 'τοῖν'  # Wikipedia unchecked
    DAT_NEU_DU = 'τοῖν'  # Wikipedia unchecked
    ACC_NEU_DU = 'τώ'  # Wikipedia unchecked

    VOC_NEU_PL = 'τά'
    NOM_NEU_PL = 'τά'
    GEN_NEU_PL = 'τῶν'
    DAT_NEU_PL = 'τοῖς'
    ACC_NEU_PL = 'τά'

    MODIFIERS = MappingProxyType({
        'NOM_MASC_SG': 'ὁ',
        'GEN_MASC_SG': 'τοῦ',
        'DAT_MASC_SG': 'τῷ',
        'ACC_MASC_SG': 'τόν',

        'NOM_MASC_DU': 'τώ',  # Wikipedia unchecked
        'GEN_MASC_DU': 'τοῖν',  # Wikipedia unchecked
        'DAT_MASC_DU': 'τοῖν',  # Wikipedia unchecked
        'ACC_MASC_DU': 'τώ',  # Wikipedia unchecked

        'VOC_MASC_PL': 'οἱ',
        'NOM_MASC_PL': 'οἱ',
        'GEN_MASC_PL': 'τῶν',
        'DAT_MASC_PL': 'τοῖς',
        'ACC_MASC_PL': 'τούς',

        'NOM_FEM_SG': 'ἡ',
        'GEN_FEM_SG': 'τῆς',
        'DAT_FEM_SG': 'τῇ',
        'ACC_FEM_SG': 'τήν',

        'NOM_FEM_DU': 'τώ',  # Wikipedia unchecked
        'GEN_FEM_DU': 'τοῖν',  # Wikipedia unchecked
        'DAT_FEM_DU': 'τοῖν',  # Wikipedia unchecked
        'ACC_FEM_DU': 'τώ',  # Wikipedia unchecked

        'VOC_FEM_PL': 'αἱ',
        'NOM_FEM_PL': 'αἱ',
        'GEN_FEM_PL': 'τῶν',
        'DAT_FEM_PL': 'ταῖς',
        'ACC_FEM_PL': 'τάς',  # 'τᾱς'  # error from wikipedia, checked against Mounce 13.1

        'NOM_NEU_SG': 'τό',
        'GEN_NEU_SG': 'τοῦ',
        'DAT_NEU_SG': 'τῷ',
        'ACC_NEU_SG': 'τό',

        'NOM_NEU_DU': 'τώ',  # Wikipedia unchecked
        'GEN_NEU_DU': 'τοῖν',  # Wikipedia unchecked
        'DAT_NEU_DU': 'τοῖν',  # Wikipedia unchecked
        'ACC_NEU_DU': 'τώ',  # Wikipedia unchecked

        'VOC_NEU_PL': 'τά',
        'NOM_NEU_PL': 'τά',
        'GEN_NEU_PL': 'τῶν',
        'DAT_NEU_PL': 'τοῖς',
        'ACC_NEU_PL': 'τά',
    })

    _build = lambda x: MappingProxyType(dict([(GreekWord.glyphen(w), tuple([Inflect.analyze(t) for t, w2 in x.items() if w2 == w])) for w in set(x.values())]))

    STRUCTS = _build(MODIFIERS)

    WORDS = frozenset(STRUCTS.keys())

    @classmethod
    def analyze(cls, word: Tuple[GreekGlyph]) -> tuple:
        return cls.STRUCTS[word] if word in cls.WORDS else tuple()