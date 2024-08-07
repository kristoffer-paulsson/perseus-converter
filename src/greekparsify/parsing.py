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
"""Parsify parses tokenized Koine Greek for advanced processing."""
from pathlib import PosixPath
from typing import Tuple

from regex import regex

from greektextify.nlp.contextual import ContextObject, NlpOperation
from greektextify.text.bracket import Bracketing
from greektextify.text.pdl_standard import PdlUtfStandard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord


class GreekParsing(ContextObject):

    def location(self) -> PosixPath:
        return PosixPath(__file__).parent.joinpath('src')

    def __init__(self, text: str):
        ContextObject.__init__(self)
        self._text = text
        self._tokenizer = Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ], PdlUtfStandard())

    def _parse(self):
        for line in self._text.split('\n'):
            yield ' '.join(regex.split(r"\[\d+\]", line))

    @NlpOperation()
    def tokenize(self):
        tokens = list()
        for text in self._parse():
            text = self._tokenizer.standardize(text)
            for tt, token in self._tokenizer.tokenize(text):
                if tt == 0:
                    tokens.append((tt, GreekWord.glyphen(token)))
                else:
                    tokens.append((tt,token))
        return tokens