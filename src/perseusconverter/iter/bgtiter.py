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
"""Module containing the LOAD command class."""
from curses.ascii import isdigit
from io import TextIOWrapper
from typing import Tuple

import regex

from greektextify.nlp.contextual import ContextObject, NlpOperation, NlpContext
from greektextify.nlp.detoken import Tokenizer
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.standardizer import TokenStandardizerMixin
from perseusconverter.util.books import BOOK_ABBR
from perseusconverter.util.utils import BRef


class BgtUtfStandard(TokenStandardizerMixin):
    MIDDLE_DOT = ord('\u00B7')
    SEMICOLON = ord('\u003B')
    EM_DASH = ord('\u2014')

    TRANSFORM = {
        MIDDLE_DOT: GreekPunctuation.ANO_TELEIA,
        SEMICOLON: GreekPunctuation.QUESTION_MARK,
        GreekExtended.KORONIS: GreekMidway.APOSTROPHE,
    }

    @classmethod
    def standardize(cls, text: str) -> str:
        text = regex.sub(r'-(?!\S)|(?<!\S)-', chr(cls.EM_DASH), text)  # Translates HYPHEN MINUS not between two words as EM DASH
        return text.translate(cls.TRANSFORM)  # Translates the rest


class IterBGT(ContextObject):

    def __init__(self, stream: TextIOWrapper, part: Tuple[str, ...] = BOOK_ABBR):
        super().__init__()
        self._part = part
        self._stream = stream
        self._tokenizer = Tokenizer.utf_tokenizer(BgtUtfStandard())
        self._current = 'n/a'

    def __iter__(self):
        return self.iter()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), ''

    def _line(self):
        while (line := self._stream.readline()):
            line = line.strip()
            yield line

    def _extract(self, line: str):
        fst = 0 #line.find(' ') + 1
        idx = line.find(':')
        idy = line.find(' ', idx)
        idv = line.rfind(' ', fst, idx)
        book_abbr = line[fst:idv]
        text = line[idy:].strip()
        cont = True if not text or idy == -1 else False
        cont = True if book_abbr not in self._part else cont
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

    def _sub(self, text: str):
        el = list()
        sdx = 0
        idl = sdx
        while (s := text.find('[', idl)) != -1:
            e = text.find(']', s)
            if e == -1:
                break
            if not all(isdigit(l) for l in text[s + 1:e]):
                idl = e
                continue
            el.append(text[sdx:s])
            el.append(int(text[s + 1:e]))
            sdx = e + 1
            idl = sdx

        el.append(text[sdx:])
        return el

    def iter_sub(self):
        for line in self._line():
            cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text = self._extract(line)
            if cont:
                continue

            bref = BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), -1)
            yield bref

            for e in filter(lambda x: isinstance(x, int), self._sub(text)):
                yield BRef(bref.book, bref.chapter, bref.verse, e)

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text)

    def iter(self):
        for line in self._line():
            with NlpContext(self):
                cont, fst, idx, idy, idv, book_abbr, chapter_num, verse_num, text = self._extract(line)
                if cont:
                    continue

                bref = BRef(book_abbr, int(chapter_num.strip()), int(verse_num.strip()), -1)
                yield bref

                for e in self._sub(text):
                    if isinstance(e, int):
                        yield BRef(bref.book, bref.chapter, bref.verse, e)
                    elif isinstance(e, str):
                        for token in self._tokenize(e):
                            yield token
                    else:
                        raise TypeError("Unexpected type")
