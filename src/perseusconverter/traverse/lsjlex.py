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
"""TEI2 Traverser and processor for Liddell & Scott."""
import re
from pathlib import PurePath

from greektextify.beta.word import BetaWord
from greektextify.nlp.contextual import NlpWarning
from greektextify.nlp.detoken import Detokenizer
from greektextify.text.token import Tokenize
from perseusconverter.traverse.general import Tei2Traverser, AbstractTeiTraverser
from lxml.etree import Element, parse, ElementTree, QName


class LsjTraverser(Tei2Traverser):
    """"""

    def __init__(self, path: PurePath, tree: ElementTree, tokenizer: Tokenize):
        Tei2Traverser.__init__(self, path, tree, tokenizer)
        self._counter = 0
        self._error = 0

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def error(self) -> int:
        return self._error

    def _decode(self, betacode: str) -> str:
        text = betacode.replace('-', '').replace('^', '').replace('<', '').replace('>', '').replace('[', '').replace(']', '')
        if text[-1] == '*':
            text = text[:-1]
        std = self._tokenizer.standardize(text.strip())
        tokens = self._tokenizer.tokenize(std)
        return Detokenizer.build_word(BetaWord.glyphen(tokens[0]))

    def _etym(self, xml: Element) -> tuple:
        e = list()
        for etym in xml.getiterator("etym"):
            if etym.text:
                e.append(self._decode(etym.text))
        return tuple(e)

    def _orth(self, xml: Element) -> tuple:
        o = list()
        el = xml.findall("orth")
        for orth in el:
            if orth.text:
                o.append(self._decode(orth.text))
        return tuple(o)

    def _senses(self, xml: Element) -> tuple:
        s = list()
        for sense in xml.getiterator("sense"):
            tr = self._tr(sense)
            if tr:
                s.append(tr)
            ref = self._ref(sense)
            if ref:
                s.append(ref)
        return tuple(s)

    def _tr(self, xml: Element) -> list:
        t = list()
        for translation in xml.getiterator("tr"):
            if translation.text:
                for tr in translation.text.split(','):
                    tr = tr.strip()
                    if tr:
                        t.append(tr)
        return t

    def _ref(self, xml: Element) -> list:
        refs = list()
        for ref in xml.getiterator("ref"):
            refs.append(self._decode(ref.text))

        if refs:
            refs.insert(0, "See:")
        return refs

    def _e(self, text: str) -> tuple:
        count = 0
        for chr in reversed(text):
            if chr.isdigit():
                count += 1
            else:
                break

        pos = len(text) - count
        idx = int(text[pos:]) if text[pos:] else 0
        word = self._decode(text[:pos])

        return word, idx

    def _traverse(self, xml: Element):
        for entry in xml.getiterator("entryFree"):
            # text = entry.attrib["key"]
            try:
                print(self._e(entry.attrib["key"]))
                print(self._orth(entry))
                print(self._etym(entry))
                print(self._senses(entry))
                self._counter += 1
            except (NlpWarning, ValueError, TypeError, IndexError) as e:
                self._error += 1
            # print(BetaWord.glyphen(tokens[0]))

    @staticmethod
    def open(filename: PurePath) -> "AbstractTeiTraverser":
        tree = None
        with open(str(filename)) as fd:
            tree = parse(fd)

        root = tree.getroot()
        tokenizer = AbstractTeiTraverser.beta_tokenizer()

        tag = QName(root).localname
        if tag == "TEI.2":
            return LsjTraverser(filename, tree, tokenizer)
        else:
            raise ValueError("Xml is not a valid TEI format! {}".format(tag))
