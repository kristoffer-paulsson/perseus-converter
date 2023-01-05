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
from unittest import TestCase

from greektextify.text.glyph import GreekGlyph
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord

PARAGRAPH = """
Υἱὸς ὀκτωκαίδεκα ἐτῶν Ιεχονιας ἐν τῷ βασιλεύειν αὐτὸν καὶ τρίμηνον καὶ 
δέκα ἡμέρας ἐβασίλευσεν ἐν Ιερουσαλημ. καὶ ἐποίησεν τὸ πονηρὸν ἐνώπιον κυρίου.
"""


class TestTreeBase(TestCase):

    def test_greek(self):
        tokenizer = Tokenize([
            GreekWord,
            GreekPunctuation,
            Spacing
        ])
        tokens = tokenizer.tokenize(PARAGRAPH)
        for token in tokens:
            print('\n'.join(GreekGlyph.debug(''.join(token))), '\n')
