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
"""Ancient Greek Grammar annalyzer which holds a set of parsed tokens and analyses them in layers."""
from typing import Tuple, List

from greekparsify.analyzer import GrammarAnalyzerMixin
from greekparsify.inflect import Inflect
from greektextify.text.prnt import PrintGreek


class GreekGrammar:

    def __init__(self, tokens: List[Tuple[int, ...]]):
        self._tokens = tokens
        for i, t in enumerate(tokens):
            if t[0] == 0:
                self._tokens[i] = t + (Inflect.empty_inf(),)

    def analyze(self, analyzer: GrammarAnalyzerMixin):
        analyzer.parse(self._tokens)

    @classmethod
    def print_tok_list(cls, tokens: List[Tuple[int, ...]], header: str = ''):
        print("==== start ({}) ====".format(header))
        for idx, data in enumerate(tokens):
            if data[0] == 0:
                tt, token, inf = data
                print(idx, tt, PrintGreek.format(token), Inflect.format_inf(inf))
            elif data[0] == 2:
                tt, token = data
                print(idx, tt, token)
        print("==== end   ({}) ====".format(header))

    @classmethod
    def print_tok_list(cls, tokens: List[Tuple[int, ...]], header: str = ''):
        print("==== start ({}) ====".format(header))
        for idx, data in enumerate(tokens):
            if data[0] == 0:
                tt, token, inf = data
                print(idx, tt, PrintGreek.format(token), Inflect.format_inf(inf))
            elif data[0] == 2:
                tt, token = data
                print(idx, tt, token)
        print("==== end   ({}) ====".format(header))

#\underset{i=1}{max}}