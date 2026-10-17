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
"""Plain text BGT traverser."""
from pathlib import PurePath
from typing import List, Tuple

import regex
from bs4 import BeautifulSoup

from greektextify.text.bracket import Bracketing
from greektextify.text.dbg_standard import DbgUtfStandard
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.quotation import GreekQuotation
from greektextify.text.spacing import Spacing
from greektextify.text.token import Tokenize
from greektextify.text.word import GreekWord
from perseusconverter.traverse.bibbgt import INDEX
from perseusconverter.traverse.traverser import AbstractTraverser


class NocrTraverser(AbstractTraverser):

    BOOKS = [
        'Mat', 'Mar', 'Luk', 'Joh', 'Act', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Phi', 'Col', '1Th', '2Th',
        '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jam', '1Pe', '2Pe', '1Jo', '2Jo', '3Jo', 'Jud', 'Rev'
    ]

    def hierarchy(self):
        pass

    def __init__(self, path: PurePath, book: str = None, chapter: int = None):
        AbstractTraverser.__init__(self, self.utf_tokenizer(), path)
        self._book = book
        self._chapter = chapter

    def traverse(self):
        nocr_path = self._filename.joinpath("abcom")
        filename = "{0}.{1}.txt".format(self._book.lower(), str(self._chapter).zfill(3))
        path = nocr_path.joinpath(filename)
        if path.exists():
            with path.open("r") as txt:
                text = txt.read()
                for line in text.split('\n'):
                    for token in  self._traverse(line, True):
                        yield token
        else:
            nocr_path = self._filename.joinpath("nocr")
            filename = "{0}.{1}.html".format(self._book.lower(), str(self._chapter).zfill(3))
            path = nocr_path.joinpath(filename)
            with path.open("r") as xml:
                text = xml.read()
                chapter = int(BeautifulSoup(text, "html.parser").find('h2').text.split(' ')[-1])
                if chapter == self._chapter:
                    print(chapter, self._chapter, path)
                text = text.split(
                    '<div align="center"><p><table width="75%" border="0"><tr><td align="left" valign="middle">'
                )[1].split('</td></tr></table></div>')[0]
                html = BeautifulSoup(text, "html.parser")
                for line in html.text.split('\n'):
                    if line.strip() != '':
                        for token in  self._traverse(line, False):
                            if token is None:
                                continue
                            yield token

    def _traverse(self, line: str, wbook: bool):
        line = line.strip()
        if line == '':
            yield
        if wbook:
            _, self._chapter, self._verse, text = regex.search(r"(.*) (\d+):(\d+)?(.*)$", line.strip()).groups()
        else:
            self._chapter, self._verse, text = regex.search(r"(\d+):(\d+)?(.*)$", line.strip()).groups()
        std = DbgUtfStandard.standardize(text.strip())

        for idx, line in self._sub_verses(std):
            self._verse = idx
            yield 5, "{} {}:{}".format(self._book, self._chapter, self._verse)
            for token in  self.general(line):
                yield token

    def _sub_verses(self, line: str) -> List[Tuple[str, str]]:
        indicies = regex.findall(r"(\[\d+\]|\d+[a-z])", line)
        verses = regex.split(r"\[\d+\]|\d+[a-z]", line)
        text = [(self._verse, verses[0])]

        if len(verses) > 1:
            for cnt in range(0, len(indicies)):
                idx = indicies[cnt]
                verse = verses[cnt + 1]
                idx = self._verse + INDEX[idx[1:-1]] if idx[0] == '[' else idx
                text.append((idx, verse))

        return text

    def general(self, text: str):
        tokens = self._tokenizer.tokenize(text)
        for token in tokens:
            if token[0] != 4:
                yield token

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
        ], DbgUtfStandard())
