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
"""Plain text BGT traverser."""
from pathlib import PurePath
from typing import List, Tuple

from regex import regex

from greektextify.text.standardize import Standardize
from perseusconverter.traverse.plain import AbstractPlainTraverser

INDEX = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '10': 'j',
    '11': 'k',
    '12': 'l',
    '13': 'm',
    '14': 'n',
    '15': 'o',
    '16': 'p',
    '17': 'q',
    '18': 'r',
    '19': 's',
    '20': 't',
    '21': 'u',
    '22': 'v',
    '23': 'w',
    '24': 'x',
    '25': 'y',
    '26': 'z',
}


class BgtTraverser(AbstractPlainTraverser):

    def __init__(self, path: PurePath):
        AbstractPlainTraverser.__init__(self, path)
        self._hierarchy = 'book-chapter-verse'
        self._book = None
        self._chapter = None
        self._verse = None

    def _traverse(self, line: str):
        self._book, self._chapter, self._verse, text = regex.search(r"(.*) (\d+):(\d+)?(.*)$", line.strip()).groups()
        std = Standardize.pdl(text.strip())

        for idx, line in self._sub_verses(std):
            self._verse = idx
            print("{} {}:{}".format(self._book, self._chapter, self._verse))
            self.general(line)

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
