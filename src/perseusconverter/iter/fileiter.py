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
import re
from abc import abstractmethod, ABC
from pathlib import PosixPath
from typing import Tuple

from bs4 import BeautifulSoup
import regex

from greektextify.nlp.contextual import NlpOperation, NlpContext, ContextObject
from greektextify.nlp.detoken import Tokenizer, Detokenizer
from greektextify.text import immaterializer
from greektextify.text.dbg_standard import DbgUtfStandard
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway
from greektextify.text.prnt import PrintGreek
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.standardizer import TokenStandardizerMixin
from greektextify.text.word import GreekWord
from perseusconverter.recursiveiterator import RecursiveIterator
from perseusconverter.util.books import BOOK_ABBR
from perseusconverter.util.utils import CountVerify, BRef


class BasicIterFile(ABC):

    def __init__(self, path: PosixPath):
        if not path.is_dir():
            raise NotADirectoryError()

        self._path = path
        self._file_index = None
        self._filename_indexer()
        self._current = 'n/a'

    def __iter__(self):
        return self._filename_emitter()

    @property
    def current(self) -> str:
        return self._current

    @abstractmethod
    def _filename_indexer(self):
        pass

    @abstractmethod
    def _filename_emitter(self):
        pass


class NocrFileIter(BasicIterFile):

    OMITTED = ('1ki.002', '2ma.013', 'mic.007')

    BOOK_LEN = (61, )

    LOWER = [x.lower() for x in BOOK_ABBR[:BOOK_LEN[0]]]

    MAP = dict(zip(LOWER, BOOK_ABBR[:BOOK_LEN[0]]))

    def _filename_emitter(self):
        abbr_set = set([x.lower() for x in BOOK_ABBR[:self.BOOK_LEN[0]]])

        if set(self._file_index.keys()) != abbr_set:
            raise RuntimeError("Book OT abbreviations not valid: {}".format(self._file_index))

        for book, chapters in self._file_index.items():
            chapter_index = set(chapters.keys())
            chapter_set = set(range(1, len(chapters) + 1))

            if chapter_index != chapter_set:
                raise RuntimeError("Chapter OT index not valid: {}".format(chapter_set))

        for book, chapters in sorted(self._file_index.items(), key=lambda x: self.LOWER.index(x[0])):
            #chapter_verify = CountVerify(len(chapters))
            for chapter_num, filename in sorted(chapters.items(), key=lambda x: x[0]):
                #chapter_verify.verify(chapter_num)
                self._current = filename.stem
                if filename.stem in self.OMITTED:
                    continue
                yield filename, book, chapter_num

    def _filename_indexer(self):
        self._file_index = dict()
        files = [filename for filename in RecursiveIterator(self._path)]

        for filename in sorted(files, key=lambda x: x.stem):
            parts = filename.stem.split('.')
            book = parts[0]
            chapter = int(parts[1])
            if book not in self._file_index:
                self._file_index[book] = dict()
            self._file_index[book][chapter] = filename


class NocrUtfStandard(TokenStandardizerMixin):
    MIDDLE_DOT = ord('\u00B7')
    SEMICOLON = ord('\u003B')
    EM_DASH = ord('\u2014')

    TRANSFORM = {
        MIDDLE_DOT: GreekPunctuation.ANO_TELEIA,
        GreekExtended.KORONIS: GreekMidway.APOSTROPHE,
        SEMICOLON: GreekPunctuation.QUESTION_MARK,
    }

    @classmethod
    def standardize(cls, text: str) -> str:
        return text.translate(cls.TRANSFORM)  # Translates the rest


class IterNocr(ContextObject):

    def __init__(self, file_iter: NocrFileIter):
        super().__init__()
        self._file_iter = file_iter
        self._tokenizer = Tokenizer.utf_tokenizer(NocrUtfStandard())
        self._current = 'n/a'

    def __iter__(self):
        return self.iter()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), self._file_iter.current

    def _iterator(self):
        for filename, book, chapter in self._file_iter:
            book_abbr = self._file_iter.MAP[book]
            with open(filename, 'r') as f:
                html = BeautifulSoup(f, 'html.parser')

                for sup in html.find_all('sup'):
                    if hasattr(sup, 'text'):
                        tail = sup.find_next_sibling(string=True)
                        if hasattr(tail, 'text'):
                            text = tail.text.strip()
                            if len(text) > 0:
                                c_num, v_num = sup.text.split(':')
                                chapter_cnt = int(c_num)
                                verse_cnt = int(v_num)
                                yield book_abbr, chapter_cnt, verse_cnt, text

    def iter_verse(self):
        for book_abbr, chapter_cnt, verse_cnt, _ in self._iterator():
            yield BRef(book_abbr, chapter_cnt, verse_cnt, -1)

    def iter_sub(self):
        for book_abbr, chapter_cnt, verse_cnt, text in self._iterator():
            yield BRef(book_abbr, chapter_cnt, verse_cnt, -1)
            sub_verses = re.findall(r"\[\d+\]", text)
            for sub_verse in sub_verses:
                yield BRef(book_abbr, chapter_cnt, verse_cnt, int(sub_verse[1:-1]))

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text)

    def iter(self):
        for filename, book, chapter in self._file_iter:
            book_abbr = self._file_iter.MAP[book]
            with open(filename, 'r') as f:
                html = BeautifulSoup(f, 'html.parser')

                with NlpContext(self):
                    for sup in html.find_all('sup'):
                        if hasattr(sup, 'text'):
                            tail = sup.find_next_sibling(string=True)
                            if hasattr(tail, 'text'):
                                text = tail.text.strip()
                                if len(text) > 0:
                                    c_num, v_num = sup.text.split(':')
                                    chapter_cnt = int(c_num)
                                    verse_cnt = int(v_num)

                                    self._current = BRef(book_abbr, chapter_cnt, verse_cnt, -1)
                                    yield self._current
                                    sub_verses = regex.findall(r"\[\d+\]", text)
                                    sub_texts = regex.split(r"\[\d+\]", text)

                                    for token in self._tokenize(sub_texts[0]):
                                        yield token

                                    for sub_verse, sub_text in zip(sub_verses, sub_texts[1:]):
                                        self._current = BRef(book_abbr, chapter_cnt, verse_cnt, int(sub_verse[1:-1]))
                                        yield self._current

                                        for token in self._tokenize(sub_text):
                                            yield token

