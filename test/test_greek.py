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
from abc import ABCMeta
from unittest import TestCase

from greektextify.nlp.debug import Debugger
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord

PARAGRAPH1 = """
Υἱὸς ὀκτωκαίδεκα ἐτῶν Ιεχονιας ἐν τῷ βασιλεύειν αὐτὸν καὶ τρίμηνον καὶ 
δέκα ἡμέρας ἐβασίλευσεν ἐν Ιερουσαλημ. καὶ ἐποίησεν τὸ πονηρὸν ἐνώπιον κυρίου.
"""

PARAGRAPH2 = """ἐκ Διὸς ἀρχώμεσθα, τὸν οὐδέποτʼ ἄνδρες ἐῶμεν"""

PARAGRAPH3 = """καθ᾽"""

PARAGRAPH4 = """᾿Εξαγαγέτω"""  # Academic bible

PARAGRAPH5 = """῾Ο"""  # Academic bible

PARAGRAPH6 = """γʼ"""  # PDL

PARAGRAPH7 = """Ἑλίκῃ"""  # PDL

PARAGRAPH8 = """῞Οτι"""  # Academic bible

PARAGRAPH9 = """ Ὕδρη,"""  # PDL

class TestGreek(TestCase):

    def test_greek(self):
        print(Debugger.glyph(PARAGRAPH3))
        print(Debugger.glyph(PARAGRAPH9))
        tokenizer = Tokenize([
            GreekWord,
            GreekPunctuation,
            Spacing
        ])
        tokens = tokenizer.tokenize(PARAGRAPH4)
        print(tokens)
        # for token in tokens:
        #    print(token)
            # print(GreekGlyph.debug(token), '\n')