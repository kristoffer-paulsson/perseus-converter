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
"""Greek detokenizer. A builder to standardized reconstruct Greek sentences, words and punctuation."""
from typing import Tuple

from greektextify.beta.pdl_standard import PdlBetaStandard
from greektextify.beta.punctuation import BetaPunctuation
from greektextify.beta.word import BetaWord
from greektextify.text.bracket import Bracketing
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.glyph import GreekGlyph
from greektextify.text.pdl_standard import PdlUtfStandard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord


class Detokenizer:

    @staticmethod
    def build_word(glyphs: Tuple[GreekGlyph]) -> str:
        word = ''

        for glyph in glyphs:
            if glyph.ch is None:
                raise ValueError("Empty glyph, must be set, exchange for NLP exception to throw.")

            word += glyph.ch
            word += GreekDiacritic.COMBINING_PSILI if glyph.psili else ''
            word += GreekDiacritic.COMBINING_DASIA if glyph.dasia else ''
            word += GreekDiacritic.COMBINING_YPOGEGRAMMENI if glyph.ypogegrammeni else ''
            word += GreekDiacritic.COMBINING_VARIA if glyph.varia else ''
            word += GreekDiacritic.COMBINING_OXIA if glyph.oxia else ''
            word += GreekDiacritic.COMBINING_PERISPOMENI if glyph.perispomeni else ''
            word += GreekDiacritic.COMBINING_DIALYTIKA if glyph.dialytika else ''
            word += GreekDiacritic.COMBINING_VRACHY if glyph.vrachy else ''
            word += GreekDiacritic.COMBINING_MACRON if glyph.macron else ''

        return word


class Tokenizer:

    def __init__(self):
        pass

    @staticmethod
    def utf_tokenizer():
        return Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ], PdlUtfStandard())

    @staticmethod
    def beta_tokenizer():
        return Tokenize([
            BetaWord,  # GreekWord,
            Bracketing,
            BetaPunctuation,  # GreekPunctuation,
            GreekQuotation,
            Spacing,
        ], PdlBetaStandard())
