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
"""Ancient Greek inflections."""
from types import MappingProxyType
from typing import Tuple


class Inflect:

    T_SPEECH = 0
    T_CASE = 1
    T_NUMBER = 2
    T_GENDER = 3

    V_UNUSED = 0

    SPEECH = MappingProxyType(dict(list(enumerate((
        '-',     # Implicit zero
        'ART',   # article
        'PREP',  # preposition
    )))))

    CASE = MappingProxyType(dict(list(enumerate((
        '-',    # Implicit zero
        'VOC',  # Vocative
        'NOM',  # Nominative case
        'ACC',  # accusative case
        'DAT',  # Dative
        'GEN',  # genitive
    )))))

    NUMBER = MappingProxyType(dict(list(enumerate((
        '-',   # Implicit zero
        'SG',  # singular
        'DU',  # dual
        'PL',  # plural
    )))))

    GENDER = MappingProxyType(dict(list(enumerate((
        '-',     # Implicit zero
        'MASC',  # masculine
        'FEM',   # feminine
        'NEU',   # neuter
    )))))

    STRUCT = MappingProxyType(dict(list(
        map(lambda x: list(reversed(x)),
            set(SPEECH.items()) |
            set(CASE.items()) |
            set(GENDER.items()) |
            set(NUMBER.items())
            ))))

    @classmethod
    def analyze(cls, morph: str) -> tuple:
        return tuple([cls.STRUCT[t] if t in cls.STRUCT else 0 for t in morph.split('_')])

    @classmethod
    def empty_inf(cls) -> tuple:
        return 0, 0, 0, 0

    @classmethod
    def modify_inf(cls, inf: tuple, t: int, v) -> tuple:
        inf2 = list(inf)
        if type(v) == int:
            inf2[t] = v
        elif len(v) == 1:
            inf2[t] = v[0]
        else:
            inf2[t] = v
        return tuple(inf2)

    @classmethod
    def get_inf(cls, inf: tuple, t: int) -> int:
        return inf[t]

    @classmethod
    def read_inf(cls, inf: tuple, t: int) -> int:
        if len(inf[t]) > 1:
            for v in list(inf[t]):
                yield v
        else:
            yield inf[t]

    @classmethod
    def format_inf(cls, inf: tuple) -> str:
        return "({}, {}, {}, {})".format(
            cls.SPEECH[inf[cls.T_SPEECH]],
            cls.CASE[inf[cls.T_CASE]],
            cls.GENDER[inf[cls.T_GENDER]],
            cls.NUMBER[inf[cls.T_NUMBER]],
        )

    @classmethod
    def tex_format_inf(cls, inf: tuple) -> Tuple[str, ...]:
        inflex = list()
        if inf[cls.T_SPEECH] != cls.V_UNUSED: inflex.append(cls.SPEECH[inf[cls.T_SPEECH]])
        if inf[cls.T_CASE] != cls.V_UNUSED: inflex.append(cls.CASE[inf[cls.T_CASE]])
        if inf[cls.T_GENDER] != cls.V_UNUSED: inflex.append(cls.GENDER[inf[cls.T_GENDER]])
        if inf[cls.T_NUMBER] != cls.V_UNUSED: inflex.append(cls.NUMBER[inf[cls.T_NUMBER]])
        return tuple(inflex)
