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
"""Ancient Greek prepositions."""
from types import MappingProxyType
from typing import Tuple, List

from greekparsify.analyzer import GrammarAnalyzerMixin
from greekparsify.grammar import GreekGrammar
from greekparsify.inflect import Inflect
from greektextify.nlp.contextual import NlpWarning
from greektextify.text.glyph import GreekGlyph
from greektextify.text.midway import GreekMidway
from greektextify.text.prnt import PrintGreek
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.word import GreekWord


class Prepositions(GrammarAnalyzerMixin):
    PART = 'PREP'

    # """ἀπό (ἀπ᾿, ἀφ᾿), gen: (away) from"""
    APO = (
        (
            'ἀπό',
            'ἀπ' + GreekMidway.APOSTROPHE,
            'ἀφ' + GreekMidway.APOSTROPHE
        ), 'GEN',
    )

    # """διά (δι᾿), gen: through; acc: on account of"""
    DIA = (
        (
            'διά',
            'δι' + GreekMidway.APOSTROPHE
        ), 'GEN_ACC',
    )

    # """εἰς, acc: into, in, among"""
    EIS = (
        ('εἰς',), 'ACC'
    )

    # """ἐκ, ἐξ, gen: from, out of"""
    EK = (
        ('ἐκ', 'ἐξ'), 'GEN'
    )

    # """ἐν, dat: in, on, among"""
    EN = (
        ('ἐν',), 'DAT'
    )

    # """ἐπί (ἐπ᾿, ἐφ᾽), gen: on, over, when; dat: on the basis of, at; acc: on, to, against"""
    EPI = (
        (
            'ἐπί',
            'ἐπ' + GreekMidway.APOSTROPHE,
            'ἐφ' + GreekMidway.APOSTROPHE
        ), 'GEN_DAT_ACC'
    )

    # """κατά (κατ᾿, καθ᾽), gen: down from, against; acc: according to, throughout, during"""
    KATA = (
        (
            'κατά',
            'κατ' + GreekMidway.APOSTROPHE,
            'καθ' + GreekMidway.APOSTROPHE
        ), 'GEN_ACC'
    )

    # """μετά (μετ᾿, μεθ᾽) gen: with; acc: after"""
    META = (
        (
            'μετά',
            'μετ' + GreekMidway.APOSTROPHE,
            'μεθ' + GreekMidway.APOSTROPHE
        ), 'GEN_ACC'
    )

    # """παρά, gen: from; dat: beside, in the presence of; acc: alongside of"""
    PARA = (
        ('παρά',), 'GEN_DAT_ACC'
    )

    # """περί, gen: concerning, about; acc: around"""
    PERI = (
        ('περί',), 'GEN_ACC'
    )

    # """πρός, acc: to, toward, with"""
    PROS = (
        ('πρός',), 'ACC'
    )

    # """ὑπέρ, gen: in behalf of; above"""
    HUPER = (
        ('ὑπέρ',), 'GEN'
    )

    # """ὑπό (ὑπ᾿, ὑφ᾽) gen: by; acc: under"""
    HUPO = (
        (
            'ὑπό',
            'ὑπ' + GreekMidway.APOSTROPHE,
            'ὑφ' + GreekMidway.APOSTROPHE
        ), 'GEN_ACC'
    )

    PREP = tuple([
        APO, DIA, EIS, EK,
        EN, EPI, KATA, META,
        PARA, PERI, PROS, HUPER,
        HUPO
    ])

    _build = lambda x: MappingProxyType(
        dict([(GreekWord.glyphen(v), Inflect.analyze(t)) for w, t in list(x) for v in w]))

    PREPOS = _build(PREP)

    STRUCT = frozenset(PREPOS.keys())

    _scan = lambda x: True if x[0] == 2 and x[1] in (
        GreekPunctuation.FULL_STOP, GreekPunctuation.QUESTION_MARK) else False

    @classmethod
    def parse(cls, tokens: List[Tuple[int, ...]]):
        for idx, data in enumerate(tokens):
            if data[0] == 0:
                tt, token, inf = data
                if cls.is_preposition(token):
                    if Inflect.get_inf(inf, Inflect.T_SPEECH) != Inflect.V_UNUSED:
                        raise NlpWarning(*NlpWarning.MISSING, 'n/a')

                    sub_tokens = tokens[idx:cls.scan_ahead(tokens, idx, cls._scan)]

                    inf = Inflect.modify_inf(inf, Inflect.T_SPEECH, Inflect.analyze(cls.PART))
                    for case in Prepositions.have_case(token):
                        sub_copy = sub_tokens.copy()
                        sub_copy[0] = (tt, token, Inflect.modify_inf(inf, Inflect.T_CASE, case))
                        GreekGrammar.print_tok_list(sub_copy, "Prepositions: {}, {}".format(Inflect.CASE[case], idx))

    @classmethod
    def is_preposition(cls, word: Tuple[GreekGlyph]) -> bool:
        for prep in cls.STRUCT:
            if GreekWord.cmp_semi(word, prep):
                return True
        return False

    @classmethod
    def have_case(cls, word: Tuple[GreekGlyph]) -> tuple:
        for prep in cls.STRUCT:
            if GreekWord.cmp_semi(word, prep):
                return cls.PREPOS[prep]
        else:
            return tuple()
