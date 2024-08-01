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
"""Class for dealing with midway unicode, nothing else."""
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic


class GreekMidway:

    CAPITAL_ALPHA_TONOS = '\u0386'
    CAPITAL_EPSILON_TONOS = '\u0388'
    CAPITAL_ETA_TONOS = '\u0389'
    CAPITAL_IOTA_TONOS = '\u038A'
    CAPITAL_OMICRON_TONOS = '\u038C'
    CAPITAL_UPSILON_TONOS = '\u038E'
    CAPITAL_OMEGA_TONOS = '\u038F'
    SMALL_IOTA_DIALYTIKA_TONOS = '\u0390'
    CAPITAL_IOTA_DIALYTIKA = '\u03AA'
    CAPITAL_UPSILON_DIALYTIKA = '\u03AB'
    SMALL_ALPHA_TONOS = '\u03AC'
    SMALL_EPSILON_TONOS = '\u03AD'
    SMALL_ETA_TONOS = '\u03AE'
    SMALL_IOTA_TONOS = '\u03AF'
    SMALL_UPSILON_DIALYTIKA_TONOS = '\u03B0'
    SMALL_IOTA_DIALYTIKA = '\u03CA'
    SMALL_UPSILON_DIALYTIKA = '\u03CB'
    SMALL_OMICRON_TONOS = '\u03CC'
    SMALL_UPSILON_TONOS = '\u03CD'
    SMALL_OMEGA_TONOS = '\u03CE'

    EXPANDABLE_LETTERS = {
        CAPITAL_ALPHA_TONOS: GreekAlphabet.UPPER_ALPHA + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_EPSILON_TONOS: GreekAlphabet.UPPER_EPSILON + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_ETA_TONOS: GreekAlphabet.UPPER_ETA + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_IOTA_TONOS: GreekAlphabet.UPPER_IOTA + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_OMICRON_TONOS: GreekAlphabet.UPPER_OMICRON + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_UPSILON_TONOS: GreekAlphabet.UPPER_UPSILON + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_OMEGA_TONOS: GreekAlphabet.UPPER_OMEGA + GreekDiacritic.COMBINING_TONOS,
        SMALL_IOTA_DIALYTIKA_TONOS: GreekAlphabet.LOWER_IOTA + GreekDiacritic.COMBINING_DIALYTIKA + GreekDiacritic.COMBINING_TONOS,
        CAPITAL_IOTA_DIALYTIKA: GreekAlphabet.UPPER_IOTA + GreekDiacritic.COMBINING_DIALYTIKA,
        CAPITAL_UPSILON_DIALYTIKA: GreekAlphabet.UPPER_UPSILON + GreekDiacritic.COMBINING_DIALYTIKA,
        SMALL_ALPHA_TONOS: GreekAlphabet.LOWER_ALPHA + GreekDiacritic.COMBINING_TONOS,
        SMALL_EPSILON_TONOS: GreekAlphabet.LOWER_EPSILON + GreekDiacritic.COMBINING_TONOS,
        SMALL_ETA_TONOS: GreekAlphabet.LOWER_ETA + GreekDiacritic.COMBINING_TONOS,
        SMALL_IOTA_TONOS: GreekAlphabet.LOWER_IOTA + GreekDiacritic.COMBINING_TONOS,
        SMALL_UPSILON_DIALYTIKA_TONOS: GreekAlphabet.LOWER_UPSILON + GreekDiacritic.COMBINING_DIALYTIKA + GreekDiacritic.COMBINING_TONOS,
        SMALL_IOTA_DIALYTIKA: GreekAlphabet.LOWER_IOTA + GreekDiacritic.COMBINING_DIALYTIKA,
        SMALL_UPSILON_DIALYTIKA: GreekAlphabet.LOWER_UPSILON + GreekDiacritic.COMBINING_DIALYTIKA,
        SMALL_OMICRON_TONOS: GreekAlphabet.LOWER_OMICRON + GreekDiacritic.COMBINING_TONOS,
        SMALL_UPSILON_TONOS: GreekAlphabet.LOWER_UPSILON + GreekDiacritic.COMBINING_TONOS,
        SMALL_OMEGA_TONOS: GreekAlphabet.LOWER_OMEGA + GreekDiacritic.COMBINING_TONOS,
    }

    LETTERS = frozenset(EXPANDABLE_LETTERS.keys())

    APOSTROPHE = '\u0027'

    MODIFIERS = frozenset([APOSTROPHE])

