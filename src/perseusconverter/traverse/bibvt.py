#
# Copyright (c) 2026 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Common traverser interface.
The purpose of a traverser is to traverse a Greek PDL TEI2 file in an ordered manner."""
import re
from abc import ABC
from pathlib import PurePath
from typing import Tuple, Dict

from bs4 import BeautifulSoup
from lxml.etree import Element, ElementTree, QName, parse

from greektextify.nlp.contextual import ContextObject
from greektextify.text.bracket import Bracketing
from greektextify.text.pdl_standard import PdlUtfStandard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord
from perseusconverter.traverse.traverser import AbstractTraverser


class VetusTraverser(AbstractTraverser):

    SKIP_TAGS = tuple()

    def __init__(self, path: PurePath, book: str = None, chapter: int = None):
        AbstractTraverser.__init__(self, self.utf_tokenizer(), path)
        self._book = book
        self._chapter = chapter

    @property
    def hierarchy(self) -> Dict[str, str]:
        return {k: v for k, v in self._hierarchy[2] if v != 'n/a'}

    def traverse(self):
        tokenizer = self.utf_tokenizer()
        html = self.get_lxml()

        #book_ = html.find("span", attrs={"id": "h2"})
        #if book_ is not None:
            #chapter: = html.find("span", attrs={"id": "h3"}).text.split(' ')[1].strip()
        #    print(book_.text.split(' ')[1].strip())
        #    print(self._chapter)
        #return

        if self._book is not None:
            book = self._book
        else:
            book = html.find("span", attrs={"id": "h2"}).text.split(' ')[1].strip()[:-1]

        if self._chapter is not None:
            chapter = self._chapter
        else:
            chapter = html.find("span", attrs={"id": "h3"}).text.split(' ')[1].strip()

        verses = list()
        for child in html.find_all("span", attrs={"id": "h4"}):
            verses.append(child.text.split(' ')[1].strip())

        texts = list()
        for child in html.find_all("span", attrs={"id": "gr16"}):
            texts.append(child.text.strip())

        for verse, text in zip(verses, texts):
            yield 5, f"{book} {chapter}:{verse}"
            #for token in tokenizer.tokenize(tokenizer.standardize(text)):
            #    yield token

    def general(self):
        return NotImplemented

    def get_lxml(self) -> BeautifulSoup:
        if self._filename is not None:
            with open(self._filename) as html:
                text = html.read()
                self.xml = BeautifulSoup(text, "lxml")
        return self.xml

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

