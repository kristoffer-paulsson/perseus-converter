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
from curses.ascii import isdigit, isalpha
from io import TextIOWrapper
from typing import Tuple

from greektextify.nlp.contextual import ContextObject, NlpOperation, NlpContext
from greektextify.nlp.detoken import Tokenizer
from perseusconverter.iter.bgtiter import BgtUtfStandard
from perseusconverter.util.books import NEW_ABBR
from perseusconverter.util.utils import BRef


class IterRSGNT(ContextObject):
    ABBR = (
        'Mt', 'Mk', 'Lk', 'Jn', 'Ac', 'Ro', '1Co', '2Co', 'Ga', 'Eph', 'Php', 'Col', '1Th', '2Th', '1Ti', '2Ti',
        'Tit', 'Phm', 'Heb', 'Jas', '1Pe', '2Pe', '1Jn', '2Jn', '3Jn', 'Jud', 'Re'
    )

    def __init__(self, stream: TextIOWrapper):
        super().__init__()
        self._stream = stream
        self._tokenizer = Tokenizer.utf_tokenizer(BgtUtfStandard())
        self._current = 'n/a'

    def __iter__(self):
        return self.iter_verse()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), ''

    @classmethod
    def _find_digit(cls, text: str, position: int = 0):
        if position < 0 or position >= len(text):
            raise IndexError()

        pos = position
        while not isdigit(text[pos]):
            if pos < len(text)-1:
                pos += 1
            else:
                return -1
        return pos

    @classmethod
    def _find_eo_ref(cls, text: str, position: int = 0):
        if position < 0 or position >= len(text):
            raise IndexError()

        pos = position
        while isalpha(text[pos]) or isdigit(text[pos]) or text[pos] == ':':
            if pos < len(text)-1:
                pos += 1
            else:
                return -1
        return pos

    @classmethod
    def _find_ref(cls, text: str):
        el = list()
        sdx = 0
        idl = sdx
        while (s := cls._find_digit(text, idl)) != -1:
            e = cls._find_eo_ref(text, s)
            if e == -1:
                break
            el.append(text[sdx:s])
            el.append(text[s :e])
            sdx = e # + 1
            idl = sdx

        el.append(text[sdx:])
        return el

    def _iterator(self):
        book_abbr = 'n/a'
        chapter_cnt = 0
        verse_cnt = 0
        vchange = False
        for line in self._stream:
            line2 = line.strip()
            if line2 in self.ABBR:
                book_abbr = NEW_ABBR[self.ABBR.index(line2)]
            else:
                for e in self._find_ref(line):
                    if e == '':
                        continue
                    elif isdigit(e[0]):
                        if ':' in e:
                            chapter_num, verse_num = e.split(':')
                            chapter_cnt = int(chapter_num)
                            verse_cnt = int(verse_num)
                        else:
                            verse_cnt = int(e)
                        vchange = True
                    elif e.strip() != '':
                        yield vchange, book_abbr, chapter_cnt, verse_cnt, e
                        vchange = False
                    else:
                        continue

    def iter_verse(self):
        for change, book_abbr, chapter, verse, text in self._iterator():
            if change:
                bref = BRef(book_abbr, chapter, verse, -1)
                self._current = str(bref)
                yield bref

    def iter_sub(self):
        pass

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text)

    def iter(self):
        book_abbr = 'n/a'
        chapter_cnt = 0
        verse_cnt = 0
        vchange = False
        for line in self._stream:
            with NlpContext(self):
                line2 = line.strip()
                if line2 in self.ABBR:
                    book_abbr = NEW_ABBR[self.ABBR.index(line2)]
                else:
                    for e in self._find_ref(line):
                        if e == '':
                            continue
                        elif isdigit(e[0]):
                            if ':' in e:
                                chapter_num, verse_num = e.split(':')
                                chapter_cnt = int(chapter_num)
                                verse_cnt = int(verse_num)
                            else:
                                verse_cnt = int(e)
                            vchange = True
                        elif e.strip() != '':
                            if vchange:
                                vchange = False
                                bref = BRef(book_abbr, chapter_cnt, verse_cnt, -1)
                                self._current = str(bref)
                                yield bref
                            for token in self._tokenize(e):
                                yield token
                        else:
                            continue
