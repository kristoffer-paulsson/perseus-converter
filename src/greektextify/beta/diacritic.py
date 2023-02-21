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
"""Betacode latin->koine mapping."""
from greektextify.text.diacritic import GreekDiacritic


class BetaDiacritic(GreekDiacritic):

    COMBINING_PSILI = '\u0029'
    COMBINING_DASIA = '\u0028'

    COMBINING_OXIA = '\u002F'
    COMBINING_PERISPOMENI = '\u003D'
    COMBINING_VARIA = '\u005C'
    COMBINING_DIALYTIKA = '\u002B'

    COMBINING_YPOGEGRAMMENI = '\u007C'

    DIACRITICS = frozenset([
        COMBINING_PSILI, COMBINING_DASIA, COMBINING_OXIA, COMBINING_PERISPOMENI, COMBINING_VARIA, COMBINING_DIALYTIKA,
        COMBINING_YPOGEGRAMMENI
    ])

    BETA_DIACRITICS = {
        COMBINING_PSILI: GreekDiacritic.COMBINING_PSILI,
        COMBINING_DASIA: GreekDiacritic.COMBINING_DASIA,
        COMBINING_OXIA: GreekDiacritic.COMBINING_OXIA,
        COMBINING_PERISPOMENI: GreekDiacritic.COMBINING_PERISPOMENI,
        COMBINING_VARIA: GreekDiacritic.COMBINING_VARIA,
        COMBINING_DIALYTIKA: GreekDiacritic.COMBINING_DIALYTIKA,
        COMBINING_YPOGEGRAMMENI: GreekDiacritic.COMBINING_YPOGEGRAMMENI
    }
