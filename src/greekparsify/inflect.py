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


class Inflect:

    SPEECH = MappingProxyType(dict(list(enumerate((
        '-',     # Implicit zero
        'ART',   # article
        'PREP',  # preposition
    )))))

    CASE = MappingProxyType(dict(list(enumerate((
        '-',    # Implicit zero
        'NOM',  # Nominative case
        'GEN',  # genitive
        'DAT',  # Dative
        'ACC',  # accusative case
        'VOC',  # Vocative
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
            set(CASE.items()) |
            set(GENDER.items()) |
            set(NUMBER.items())
            ))))

    @classmethod
    def analyze(cls, morph: str) -> tuple:
        return tuple([cls.STRUCT[t] if t in cls.STRUCT else 0 for t in morph.split('_')])

