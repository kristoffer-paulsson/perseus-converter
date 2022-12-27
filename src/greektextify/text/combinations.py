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
"""The combinations of diacritics and letters allowed."""
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic


class GreekCombinations:

    VALID = frozenset((
        ('Α', False, False, False, False, False, False, False, False, False),
        ('Α', False, False, False, False, False, False, False, False, True),
        ('Α', False, False, False, False, False, False, False, True, False),
        ('Α', False, False, False, False, True, False, False, False, False),
        ('Α', False, False, False, False, True, False, False, False, False),
        ('Α', False, False, False, True, False, False, False, False, False),
        ('Α', False, False, True, False, False, False, False, False, False),
        ('Α', False, True, False, False, False, False, False, False, False),
        ('Α', False, True, False, False, False, True, False, False, False),
        ('Α', False, True, False, False, True, False, False, False, False),
        ('Α', False, True, False, True, False, False, False, False, False),
        ('Α', False, True, True, False, False, False, False, False, False),
        ('Α', False, True, True, False, False, True, False, False, False),
        ('Α', False, True, True, False, True, False, False, False, False),
        ('Α', False, True, True, True, False, False, False, False, False),
        ('Α', True, False, False, False, False, False, False, False, False),
        ('Α', True, False, False, False, False, True, False, False, False),
        ('Α', True, False, False, False, True, False, False, False, False),
        ('Α', True, False, False, True, False, False, False, False, False),
        ('Α', True, False, True, False, False, False, False, False, False),
        ('Α', True, False, True, False, False, True, False, False, False),
        ('Α', True, False, True, False, True, False, False, False, False),
        ('Α', True, False, True, True, False, False, False, False, False),
        ('Β', False, False, False, False, False, False, False, False, False),
        ('Γ', False, False, False, False, False, False, False, False, False),
        ('Δ', False, False, False, False, False, False, False, False, False),
        ('Ε', False, False, False, False, False, False, False, False, False),
        ('Ε', False, False, False, False, True, False, False, False, False),
        ('Ε', False, False, False, False, True, False, False, False, False),
        ('Ε', False, False, False, True, False, False, False, False, False),
        ('Ε', False, True, False, False, False, False, False, False, False),
        ('Ε', False, True, False, False, True, False, False, False, False),
        ('Ε', False, True, False, True, False, False, False, False, False),
        ('Ε', True, False, False, False, False, False, False, False, False),
        ('Ε', True, False, False, False, True, False, False, False, False),
        ('Ε', True, False, False, True, False, False, False, False, False),
        ('Ζ', False, False, False, False, False, False, False, False, False),
        ('Η', False, False, False, False, False, False, False, False, False),
        ('Η', False, False, False, False, True, False, False, False, False),
        ('Η', False, False, False, False, True, False, False, False, False),
        ('Η', False, False, False, True, False, False, False, False, False),
        ('Η', False, False, True, False, False, False, False, False, False),
        ('Η', False, True, False, False, False, False, False, False, False),
        ('Η', False, True, False, False, False, True, False, False, False),
        ('Η', False, True, False, False, True, False, False, False, False),
        ('Η', False, True, False, True, False, False, False, False, False),
        ('Η', False, True, True, False, False, False, False, False, False),
        ('Η', False, True, True, False, False, True, False, False, False),
        ('Η', False, True, True, False, True, False, False, False, False),
        ('Η', False, True, True, True, False, False, False, False, False),
        ('Η', True, False, False, False, False, False, False, False, False),
        ('Η', True, False, False, False, False, True, False, False, False),
        ('Η', True, False, False, False, True, False, False, False, False),
        ('Η', True, False, False, True, False, False, False, False, False),
        ('Η', True, False, True, False, False, False, False, False, False),
        ('Η', True, False, True, False, False, True, False, False, False),
        ('Η', True, False, True, False, True, False, False, False, False),
        ('Η', True, False, True, True, False, False, False, False, False),
        ('Θ', False, False, False, False, False, False, False, False, False),
        ('Ι', False, False, False, False, False, False, False, False, False),
        ('Ι', False, False, False, False, False, False, False, False, True),
        ('Ι', False, False, False, False, False, False, False, True, False),
        ('Ι', False, False, False, False, False, False, True, False, False),
        ('Ι', False, False, False, False, True, False, False, False, False),
        ('Ι', False, False, False, False, True, False, False, False, False),
        ('Ι', False, False, False, True, False, False, False, False, False),
        ('Ι', False, True, False, False, False, False, False, False, False),
        ('Ι', False, True, False, False, False, True, False, False, False),
        ('Ι', False, True, False, False, True, False, False, False, False),
        ('Ι', False, True, False, True, False, False, False, False, False),
        ('Ι', True, False, False, False, False, False, False, False, False),
        ('Ι', True, False, False, False, False, True, False, False, False),
        ('Ι', True, False, False, False, True, False, False, False, False),
        ('Ι', True, False, False, True, False, False, False, False, False),
        ('Κ', False, False, False, False, False, False, False, False, False),
        ('Λ', False, False, False, False, False, False, False, False, False),
        ('Μ', False, False, False, False, False, False, False, False, False),
        ('Ν', False, False, False, False, False, False, False, False, False),
        ('Ξ', False, False, False, False, False, False, False, False, False),
        ('Ο', False, False, False, False, False, False, False, False, False),
        ('Ο', False, False, False, False, True, False, False, False, False),
        ('Ο', False, False, False, False, True, False, False, False, False),
        ('Ο', False, False, False, True, False, False, False, False, False),
        ('Ο', False, True, False, False, False, False, False, False, False),
        ('Ο', False, True, False, False, True, False, False, False, False),
        ('Ο', False, True, False, True, False, False, False, False, False),
        ('Ο', True, False, False, False, False, False, False, False, False),
        ('Ο', True, False, False, False, True, False, False, False, False),
        ('Ο', True, False, False, True, False, False, False, False, False),
        ('Π', False, False, False, False, False, False, False, False, False),
        ('Ρ', False, False, False, False, False, False, False, False, False),
        ('Ρ', False, True, False, False, False, False, False, False, False),
        ('Σ', False, False, False, False, False, False, False, False, False),
        ('Τ', False, False, False, False, False, False, False, False, False),
        ('Υ', False, False, False, False, False, False, False, False, False),
        ('Υ', False, False, False, False, False, False, False, False, True),
        ('Υ', False, False, False, False, False, False, False, True, False),
        ('Υ', False, False, False, False, False, False, True, False, False),
        ('Υ', False, False, False, False, True, False, False, False, False),
        ('Υ', False, False, False, False, True, False, False, False, False),
        ('Υ', False, False, False, True, False, False, False, False, False),
        ('Υ', False, True, False, False, False, False, False, False, False),
        ('Υ', False, True, False, False, False, True, False, False, False),
        ('Υ', False, True, False, False, True, False, False, False, False),
        ('Υ', False, True, False, True, False, False, False, False, False),
        ('Φ', False, False, False, False, False, False, False, False, False),
        ('Χ', False, False, False, False, False, False, False, False, False),
        ('Ψ', False, False, False, False, False, False, False, False, False),
        ('Ω', False, False, False, False, False, False, False, False, False),
        ('Ω', False, False, False, False, True, False, False, False, False),
        ('Ω', False, False, False, False, True, False, False, False, False),
        ('Ω', False, False, False, True, False, False, False, False, False),
        ('Ω', False, False, True, False, False, False, False, False, False),
        ('Ω', False, True, False, False, False, False, False, False, False),
        ('Ω', False, True, False, False, False, True, False, False, False),
        ('Ω', False, True, False, False, True, False, False, False, False),
        ('Ω', False, True, False, True, False, False, False, False, False),
        ('Ω', False, True, True, False, False, False, False, False, False),
        ('Ω', False, True, True, False, False, True, False, False, False),
        ('Ω', False, True, True, False, True, False, False, False, False),
        ('Ω', False, True, True, True, False, False, False, False, False),
        ('Ω', True, False, False, False, False, False, False, False, False),
        ('Ω', True, False, False, False, False, True, False, False, False),
        ('Ω', True, False, False, False, True, False, False, False, False),
        ('Ω', True, False, False, True, False, False, False, False, False),
        ('Ω', True, False, True, False, False, False, False, False, False),
        ('Ω', True, False, True, False, False, True, False, False, False),
        ('Ω', True, False, True, False, True, False, False, False, False),
        ('Ω', True, False, True, True, False, False, False, False, False),
        ('α', False, False, False, False, False, False, False, False, False),
        ('α', False, False, False, False, False, False, False, False, True),
        ('α', False, False, False, False, False, False, False, True, False),
        ('α', False, False, False, False, False, True, False, False, False),
        ('α', False, False, False, False, True, False, False, False, False),
        ('α', False, False, False, False, True, False, False, False, False),
        ('α', False, False, False, True, False, False, False, False, False),
        ('α', False, False, True, False, False, False, False, False, False),
        ('α', False, False, True, False, False, True, False, False, False),
        ('α', False, False, True, False, True, False, False, False, False),
        ('α', False, False, True, True, False, False, False, False, False),
        ('α', False, True, False, False, False, False, False, False, False),
        ('α', False, True, False, False, False, True, False, False, False),
        ('α', False, True, False, False, True, False, False, False, False),
        ('α', False, True, False, True, False, False, False, False, False),
        ('α', False, True, True, False, False, False, False, False, False),
        ('α', False, True, True, False, False, True, False, False, False),
        ('α', False, True, True, False, True, False, False, False, False),
        ('α', False, True, True, True, False, False, False, False, False),
        ('α', True, False, False, False, False, False, False, False, False),
        ('α', True, False, False, False, False, True, False, False, False),
        ('α', True, False, False, False, True, False, False, False, False),
        ('α', True, False, False, True, False, False, False, False, False),
        ('α', True, False, True, False, False, False, False, False, False),
        ('α', True, False, True, False, False, True, False, False, False),
        ('α', True, False, True, False, True, False, False, False, False),
        ('α', True, False, True, True, False, False, False, False, False),
        ('β', False, False, False, False, False, False, False, False, False),
        ('γ', False, False, False, False, False, False, False, False, False),
        ('δ', False, False, False, False, False, False, False, False, False),
        ('ε', False, False, False, False, False, False, False, False, False),
        ('ε', False, False, False, False, True, False, False, False, False),
        ('ε', False, False, False, False, True, False, False, False, False),
        ('ε', False, False, False, True, False, False, False, False, False),
        ('ε', False, True, False, False, False, False, False, False, False),
        ('ε', False, True, False, False, True, False, False, False, False),
        ('ε', False, True, False, True, False, False, False, False, False),
        ('ε', True, False, False, False, False, False, False, False, False),
        ('ε', True, False, False, False, True, False, False, False, False),
        ('ε', True, False, False, True, False, False, False, False, False),
        ('ζ', False, False, False, False, False, False, False, False, False),
        ('η', False, False, False, False, False, False, False, False, False),
        ('η', False, False, False, False, False, True, False, False, False),
        ('η', False, False, False, False, True, False, False, False, False),
        ('η', False, False, False, False, True, False, False, False, False),
        ('η', False, False, False, True, False, False, False, False, False),
        ('η', False, False, True, False, False, False, False, False, False),
        ('η', False, False, True, False, False, True, False, False, False),
        ('η', False, False, True, False, True, False, False, False, False),
        ('η', False, False, True, True, False, False, False, False, False),
        ('η', False, True, False, False, False, False, False, False, False),
        ('η', False, True, False, False, False, True, False, False, False),
        ('η', False, True, False, False, True, False, False, False, False),
        ('η', False, True, False, True, False, False, False, False, False),
        ('η', False, True, True, False, False, False, False, False, False),
        ('η', False, True, True, False, False, True, False, False, False),
        ('η', False, True, True, False, True, False, False, False, False),
        ('η', False, True, True, True, False, False, False, False, False),
        ('η', True, False, False, False, False, False, False, False, False),
        ('η', True, False, False, False, False, True, False, False, False),
        ('η', True, False, False, False, True, False, False, False, False),
        ('η', True, False, False, True, False, False, False, False, False),
        ('η', True, False, True, False, False, False, False, False, False),
        ('η', True, False, True, False, False, True, False, False, False),
        ('η', True, False, True, False, True, False, False, False, False),
        ('η', True, False, True, True, False, False, False, False, False),
        ('θ', False, False, False, False, False, False, False, False, False),
        ('ι', False, False, False, False, False, False, False, False, False),
        ('ι', False, False, False, False, False, False, False, False, True),
        ('ι', False, False, False, False, False, False, False, True, False),
        ('ι', False, False, False, False, False, False, True, False, False),
        ('ι', False, False, False, False, False, True, False, False, False),
        ('ι', False, False, False, False, False, True, True, False, False),
        ('ι', False, False, False, False, True, False, False, False, False),
        ('ι', False, False, False, False, True, False, False, False, False),
        ('ι', False, False, False, False, True, False, True, False, False),
        ('ι', False, False, False, False, True, False, True, False, False),
        ('ι', False, False, False, True, False, False, False, False, False),
        ('ι', False, False, False, True, False, False, True, False, False),
        ('ι', False, True, False, False, False, False, False, False, False),
        ('ι', False, True, False, False, False, True, False, False, False),
        ('ι', False, True, False, False, True, False, False, False, False),
        ('ι', False, True, False, True, False, False, False, False, False),
        ('ι', True, False, False, False, False, False, False, False, False),
        ('ι', True, False, False, False, False, True, False, False, False),
        ('ι', True, False, False, False, True, False, False, False, False),
        ('ι', True, False, False, True, False, False, False, False, False),
        ('κ', False, False, False, False, False, False, False, False, False),
        ('λ', False, False, False, False, False, False, False, False, False),
        ('μ', False, False, False, False, False, False, False, False, False),
        ('ν', False, False, False, False, False, False, False, False, False),
        ('ξ', False, False, False, False, False, False, False, False, False),
        ('ο', False, False, False, False, False, False, False, False, False),
        ('ο', False, False, False, False, True, False, False, False, False),
        ('ο', False, False, False, False, True, False, False, False, False),
        ('ο', False, False, False, True, False, False, False, False, False),
        ('ο', False, True, False, False, False, False, False, False, False),
        ('ο', False, True, False, False, True, False, False, False, False),
        ('ο', False, True, False, True, False, False, False, False, False),
        ('ο', True, False, False, False, False, False, False, False, False),
        ('ο', True, False, False, False, True, False, False, False, False),
        ('ο', True, False, False, True, False, False, False, False, False),
        ('π', False, False, False, False, False, False, False, False, False),
        ('ρ', False, False, False, False, False, False, False, False, False),
        ('ρ', False, True, False, False, False, False, False, False, False),
        ('ρ', True, False, False, False, False, False, False, False, False),
        ('ς', False, False, False, False, False, False, False, False, False),
        ('σ', False, False, False, False, False, False, False, False, False),
        ('τ', False, False, False, False, False, False, False, False, False),
        ('υ', False, False, False, False, False, False, False, False, False),
        ('υ', False, False, False, False, False, False, False, False, True),
        ('υ', False, False, False, False, False, False, False, True, False),
        ('υ', False, False, False, False, False, False, True, False, False),
        ('υ', False, False, False, False, False, True, False, False, False),
        ('υ', False, False, False, False, False, True, True, False, False),
        ('υ', False, False, False, False, True, False, False, False, False),
        ('υ', False, False, False, False, True, False, False, False, False),
        ('υ', False, False, False, False, True, False, True, False, False),
        ('υ', False, False, False, False, True, False, True, False, False),
        ('υ', False, False, False, True, False, False, False, False, False),
        ('υ', False, False, False, True, False, False, True, False, False),
        ('υ', False, True, False, False, False, False, False, False, False),
        ('υ', False, True, False, False, False, True, False, False, False),
        ('υ', False, True, False, False, True, False, False, False, False),
        ('υ', False, True, False, True, False, False, False, False, False),
        ('υ', True, False, False, False, False, False, False, False, False),
        ('υ', True, False, False, False, False, True, False, False, False),
        ('υ', True, False, False, False, True, False, False, False, False),
        ('υ', True, False, False, True, False, False, False, False, False),
        ('φ', False, False, False, False, False, False, False, False, False),
        ('χ', False, False, False, False, False, False, False, False, False),
        ('ψ', False, False, False, False, False, False, False, False, False),
        ('ω', False, False, False, False, False, False, False, False, False),
        ('ω', False, False, False, False, False, True, False, False, False),
        ('ω', False, False, False, False, True, False, False, False, False),
        ('ω', False, False, False, False, True, False, False, False, False),
        ('ω', False, False, False, True, False, False, False, False, False),
        ('ω', False, False, True, False, False, False, False, False, False),
        ('ω', False, False, True, False, False, True, False, False, False),
        ('ω', False, False, True, False, True, False, False, False, False),
        ('ω', False, False, True, True, False, False, False, False, False),
        ('ω', False, True, False, False, False, False, False, False, False),
        ('ω', False, True, False, False, False, True, False, False, False),
        ('ω', False, True, False, False, True, False, False, False, False),
        ('ω', False, True, False, True, False, False, False, False, False),
        ('ω', False, True, True, False, False, False, False, False, False),
        ('ω', False, True, True, False, False, True, False, False, False),
        ('ω', False, True, True, False, True, False, False, False, False),
        ('ω', False, True, True, True, False, False, False, False, False),
        ('ω', True, False, False, False, False, False, False, False, False),
        ('ω', True, False, False, False, False, True, False, False, False),
        ('ω', True, False, False, False, True, False, False, False, False),
        ('ω', True, False, False, True, False, False, False, False, False),
        ('ω', True, False, True, False, False, False, False, False, False),
        ('ω', True, False, True, False, False, True, False, False, False),
        ('ω', True, False, True, False, True, False, False, False, False),
        ('ω', True, False, True, True, False, False, False, False, False),
    ))

    @classmethod
    def set_diacritics(cls, ch: str) -> tuple:
        return (
            ch[0] if ch[0] in GreekAlphabet.CASE_LOWER or ch[0] in GreekAlphabet.CASE_UPPER else None,
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

    @classmethod
    def is_valid(cls, ch: tuple) -> bool:
        return ch in cls.VALID

    @classmethod
    def has_psili(cls, ch: tuple) -> bool:
        return bool(ch[1])

    @classmethod
    def has_dasia(cls, ch: tuple) -> bool:
        return bool(ch[2])

    @classmethod
    def has_ypogegrammeni(cls, ch: tuple) -> bool:
        return bool(ch[3])

    @classmethod
    def has_varia(cls, ch: tuple) -> bool:
        return bool(ch[4])

    @classmethod
    def has_oxia(cls, ch: tuple) -> bool:
        return bool(ch[5])

    @classmethod
    def has_perispomeni(cls, ch: tuple) -> bool:
        return bool(ch[6])

    @classmethod
    def has_dialytika(cls, ch: tuple) -> bool:
        return bool(ch[7])

    @classmethod
    def has_vrachy(cls, ch: tuple) -> bool:
        return bool(ch[8])

    @classmethod
    def has_macron(cls, ch: tuple) -> bool:
        return bool(ch[9])
