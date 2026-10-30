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
import json
from curses.ascii import isalpha
from typing import Tuple

from greektextify.nlp.contextual import ContextObject, NlpOperation, NlpContext
from greektextify.nlp.detoken import Tokenizer
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway
from greektextify.text.punctuation import GreekPunctuation
from greektextify.text.standardizer import TokenStandardizerMixin
from perseusconverter.iter.fileiter import BasicIterFile
from perseusconverter.recursiveiterator import RecursiveIterator
from perseusconverter.util.books import OLD_ABBR, BOOK_ABBR
from perseusconverter.util.utils import BRef


class FixFileIter(BasicIterFile):

    OMITTED = ('', )

    LOWER = [x.lower() for x in OLD_ABBR]

    def _filename_emitter(self):
        for book in self._file_index:
            for chapter in self._file_index[book]:
                yield self._file_index[book][chapter], book, chapter

    def _filename_indexer(self):
        self._file_index = dict()
        files = [filename for filename in RecursiveIterator(self._path)]

        for filename in sorted(files, key=lambda x: x.stem):
            parts = filename.stem.split('.')
            book = parts[0]
            if book in ('alt', 'lxx'):
                continue
            chapter = int(parts[1])
            if book not in self._file_index:
                self._file_index[book] = dict()
            self._file_index[book][chapter] = filename


class FixUtfStandard(TokenStandardizerMixin):
    MIDDLE_DOT = ord('\u00B7')
    SEMICOLON = ord('\u003B')
    ASTERISK = ord('\u002A')
    DOUBLE_DAGGER = ord('\u2021')

    TRANSFORM = {
        GreekExtended.KORONIS: GreekMidway.APOSTROPHE,
        MIDDLE_DOT: GreekPunctuation.ANO_TELEIA,
        SEMICOLON: GreekPunctuation.QUESTION_MARK,
        ASTERISK: ' ',
        DOUBLE_DAGGER: ' ',
    }

    @classmethod
    def standardize(cls, text: str) -> str:
        return text.translate(cls.TRANSFORM)  # Translates the rest


class IterFix(ContextObject):

    def __init__(self, file_iter: FixFileIter):
        super().__init__()
        self._file_iter = file_iter
        self._tokenizer = Tokenizer.utf_tokenizer(FixUtfStandard())
        self._current = 'n/a'

    def __iter__(self):
        return self.iter()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), self._file_iter.current

    def iter_verse(self):
        pass

    def iter_sub(self):
        pass

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text)

    def iter(self):
        last_bref = ''
        with NlpContext(self):
            for filename, book, chapter in self._file_iter:
                data = json.load(filename.open('r'))
                for paragraphs in data['data']['chapter']['content']:
                    if 'content' not in paragraphs:
                        pass
                        #print('Paragraph missing content')
                    else:
                        for content in paragraphs['content']:
                            if content['type'] == 'verse-number':
                                book_ref, chapter_num, verse_num = content['verseId'].split('.')
                                if book_ref == 'DAG' and book == 'danth':
                                    book_ref = 'DAT'
                                elif book_ref == 'DAG' and book == 'dan':
                                    book_ref = 'DAN'
                                elif book_ref == 'ESG':
                                    book_ref = 'EST'
                                book_abbr = BOOK_ABBR[self._file_iter.LOWER.index(book_ref.lower())]
                                chapter_cnt = int(chapter_num)
                                if isalpha(verse_num[-1]):
                                    verse_cnt = int(verse_num[:-1])
                                    sub_verse = ord(verse_num[-1]) - ord('a')
                                else:
                                    verse_cnt = int(verse_num)
                                    sub_verse = -1
                                bref = BRef(book_abbr, chapter_cnt, verse_cnt, sub_verse)
                                if last_bref != str(bref):
                                    last_bref = str(bref)
                                    yield bref
                            elif content['type'] in ('verse-text', 'text'):
                                for token in self._tokenize(content['content']):
                                    yield token
                            else:
                                raise ValueError("Type: {}".format(content['type']))
