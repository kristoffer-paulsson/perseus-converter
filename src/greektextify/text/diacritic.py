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
"""The Greek Koine combining diacritics.

See:
https://www.unicode.org/charts/PDF/U0300.pdf
https://www.unicode.org/charts/PDF/U0370.pdf
"""


class GreekDiacritic:
    """Koine combining accent."""

    COMBINING_VARIA = '\u0300'
    COMBINING_OXIA = '\u0301'
    COMBINING_TONOS = COMBINING_OXIA  # Backward compatability
    COMBINING_MACRON = '\u0304'
    COMBINING_VRACHY = '\u0306'
    COMBINING_DIALYTIKA = '\u0308'
    COMBINING_DIAERESIS = COMBINING_DIALYTIKA  # Backwards comaptability

    COMBINING_PSILI = '\u0313'  # Greek psili, smooth breathing mark (spiritus lenis)
    COMBINING_DASIA = '\u0314'  # Greek dasia, rough breathing mark (spiritus asper)

    COMBINING_PERISPOMENI = '\u0342'
    COMBINING_KORONIS = COMBINING_PSILI  # Backward compatability
    COMBINING_DIALYTIKA_TONOS = '\u0344'
    COMBINING_YPOGEGRAMMENI = '\u0345'
    COMBINING_PROSGEGRAMMENI = COMBINING_YPOGEGRAMMENI  # Backward compatibility

    DEBUG_CIRCLE = '\u20DD'  # Symbol for combining unicode character debugging

    DIACRITICS = frozenset([
        COMBINING_VARIA, COMBINING_OXIA, COMBINING_MACRON, COMBINING_VRACHY, COMBINING_DIALYTIKA,
        COMBINING_PSILI, COMBINING_DASIA, COMBINING_PERISPOMENI, COMBINING_DIALYTIKA_TONOS,
        COMBINING_YPOGEGRAMMENI
    ])
