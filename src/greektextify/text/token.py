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
"""Greek tokenization."""
from typing import List, Tuple, Type

from greektextify.nlp.contextual import NlpWarning
from greektextify.text.immaterializer import TokenImmaterializableMixin
from greektextify.text.standardizer import TokenStandardizerMixin


class Tokenize:

    def __init__(self, token_types: List[Type[TokenImmaterializableMixin]], standardizer: TokenStandardizerMixin):
        self._token_type = token_types
        self._standardizer = standardizer

    def span_tokenize(self, text: str) -> Tuple[int, int]:
        position = 0
        tt = -1

        while len(text) > position:
            current = start_i = position
            tt = 0
            for immaterializer in self._token_type:
                token = immaterializer.immaterialize(text[position:])
                if len(token) > 0:
                    end_i = start_i + len(token)
                    yield tt, start_i, end_i
                    position = end_i
                    break
                tt += 1

            if current == position:
                print(tt, position, text)
                raise NlpWarning(*NlpWarning.TOKENIZE_ERROR, {"pos": position, "line": text})

    def tokenize(self, text: str) -> List[Tuple[int, str]]:
        tokens = list()

        for tt, start, end in self.span_tokenize(text):
            token = (tt, text[start:end])
            if len(token[1]) > 0:
                tokens.append(token)

        return tokens

    def standardize(self, text: str) -> str:
        return self._standardizer.standardize(text)
