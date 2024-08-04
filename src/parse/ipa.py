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
"""Phonetic IPA key constants and numbers."""

from ipapy import UNICODE_TO_IPA


# https://en.wikipedia.org/wiki/Ancient_Greek_phonology
# https://en.wikipedia.org/wiki/Phonetic_symbols_in_Unicode
# https://github.com/pettarin/ipapy/blob/master/ipapy/data/ipa.dat

class IPA:
    """All IPA phonetic sounds used in Greek phonemes."""
    LONG = UNICODE_TO_IPA["\u02D0"]
    NON_SYBALLIC = UNICODE_TO_IPA["\u032F"]
    ASPIRATED = UNICODE_TO_IPA["\u02B0"]

    E = UNICODE_TO_IPA["\u0065"]
    O = UNICODE_TO_IPA["\u006F"]
    E2 = UNICODE_TO_IPA["\u025B"]
    O2 = UNICODE_TO_IPA["\u0254"]
    A = UNICODE_TO_IPA["\u0061"]
    I = UNICODE_TO_IPA["\u0069"]
    Y = UNICODE_TO_IPA["\u0079"]
    U = UNICODE_TO_IPA["\u0075"]
    D = UNICODE_TO_IPA["\u0064"]
    S = UNICODE_TO_IPA["\u0073"]
    K = UNICODE_TO_IPA["\u006B"]
    P = UNICODE_TO_IPA["\u0070"]
    L = UNICODE_TO_IPA["\u006C"]
    M = UNICODE_TO_IPA["\u006D"]
    N = UNICODE_TO_IPA["\u006E"]
    R = UNICODE_TO_IPA["\u0072"]
    T = UNICODE_TO_IPA["\u0074"]
    B = UNICODE_TO_IPA["\u0062"]
    G = UNICODE_TO_IPA["\u0261"]
    H = UNICODE_TO_IPA["\u0068"]
    W = UNICODE_TO_IPA["\u0077"]
