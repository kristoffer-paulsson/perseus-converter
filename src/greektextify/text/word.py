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
"""Greek word class segment."""
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic


class GreekWord:
    """Greek word analyzer and parsers."""

    # Smyth grammar 1.1.2 *6 -> ei and ou counts as genuine if having diaresis, else if without as spurious.
    # Smyth grammar 1.1.2 *6 + *7 -> learn
    # Smyth grammar 1.1.2 *8 -> dipthongs ending in iota or upsilon with diaeresis are not diphtongs!
    DIPHTHONGS_PROPER = (
        GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_ETA + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_UPSILON + GreekAlphabet.LOWER_IOTA
    )

    DIPHTHONGS_IMPROPER = (
        GreekAlphabet.LOWER_ALPHA + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
        GreekAlphabet.LOWER_ETA + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
        GreekAlphabet.LOWER_OMICRON + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
    )

    DIPHTHONGS = DIPHTHONGS_IMPROPER + DIPHTHONGS_IMPROPER

    DIPHTHONG_IONIC = (GreekAlphabet.LOWER_OMEGA + GreekAlphabet.LOWER_UPSILON,)

    # Smyth grammar 1.1.3 *9 -> All initial vowels and diphthongs must have any breathing mark.

    def __init__(self, word: str):
        self._word = word
