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
"""Module containing the LOAD command class."""
from io import TextIOWrapper
import regex

from perseusconverter.util.books import BOOK_ABBR, BOOK_NAME
from perseusconverter.util.utils import BRef


class IterBGM:

    def __init__(self, stream: TextIOWrapper):
        self._stream = stream

    def __iter__(self):
        return self.iter_sub()

    def _line(self):
        while (line := self._stream.readline()):
            line = line.strip()
            yield line

    def _extract(self, line: str):
        fst = line.find(' ') + 1
        idx = line.find(':')
        idy = line.find(' ', idx)
        idv = line.rfind(' ', fst, idx)
        book_abbr = BOOK_ABBR[BOOK_NAME.index(line[fst:idv])]
        text = line[idy:].strip()
        cont = True if not text or idy == -1 else False
        if cont:
            return cont, fst, idx, idy, idv, book_abbr, '', '', ''
        else:
            chapter_num, verse_num = line[idv:idy].split(':')
            return cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text

    def iter_verse(self):
        for line in self._line():
            cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text = self._extract(line)
            if cont:
                continue
            yield BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), -1)

    def iter_sub(self):
        for line in self._line():
            cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text = self._extract(line)
            if cont:
                continue

            refs = list()
            refs.append(BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), -1))

            matches = regex.findall(r"(\[\d+\])", line[idy:])
            indices = [int(i[1:-1]) for i in matches]
            for i in frozenset(indices):
                refs.append(BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), i))

            for r in refs:
                yield r

    def iter(self):
        for line in self._line():
            cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text = self._extract(line)
            if cont:
                continue
            bref = BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), -1)
            yield bref

            for t in text.split(' '):
                svs = t.find('[')
                if svs != -1:
                    sve = t.find(']')
                    sub_verse = int(t[(svs + 1):(sve)])
                    yield BRef(bref.book, bref.chapter, bref.verse, sub_verse)
                else:
                    tag = t.split('@')[0]
                    yield tag


