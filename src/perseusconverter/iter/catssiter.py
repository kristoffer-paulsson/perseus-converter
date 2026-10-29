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
from typing import Tuple

from greektextify.nlp.contextual import ContextObject, NlpOperation, NlpContext
from greektextify.nlp.detoken import Tokenizer
from perseusconverter.iter.fileiter import BasicIterFile
from perseusconverter.recursiveiterator import RecursiveIterator
from perseusconverter.util.books import BOOK_ABBR
from perseusconverter.util.utils import BRef


class CatSSFileIter(BasicIterFile):

    OMITTED = ('', )

    BOOK_LEN = (61, )

    LOWER = BOOK_ABBR[:BOOK_LEN[0]]

    MAP = {'Gen': 'Gen',
           'Exod': 'Exo',
           'Lev': 'Lev',
           'Num': 'Num',
           'Deut': 'Deu',
           'JoshB': 'Jsa', #
           'JoshA': 'Jos', #
           'JudgesB': 'Jda', #
           'JudgesA': 'Jdg', #
           'Ruth': 'Rut',
           '1Sam': '1Sa',
           '2Sam': '2Sa',
           '1Kings': '1Ki',
           '2Kings': '2Ki',
           '1Chron': '1Ch',
           '2Chron': '2Ch',
           '1Esdras': '1Es',
           '2Esdras': 'Ezr', # 2Es
           'Esther': 'Est',
           'Judith': 'Jdt',
           'TobitBA': 'Tob',
           'TobitS': 'Tbs',
           '1Macc': '1Ma',
           '2Macc': '2Ma',
           '3Macc': '3Ma',
           '4Macc': '4Ma',
           'Psalms': 'Psa',
           'Odes': 'Ode',
           'Proverbs': 'Pro',
           'Qoheleth': 'Ecc',  #?
           'Canticles': 'Sol', #?
           'Job': 'Job',
           'Wisdom': 'Wis',
           'Sirach': 'Sir',
           'PsSol': 'Pss',
           'Hosea': 'Hos',
           'Micah': 'Amo', #
           'Amos': 'Mic', #
           'Joel': 'Joe',
           'Jonah': 'Oba', #
           'Obadiah': 'Jon', #
           'Nahum': 'Nah',
           'Habakkuk': 'Hab',
           'Zeph': 'Zep',
           'Haggai': 'Hag',
           'Zech': 'Zec',
           'Malachi': 'Mal',
           'Isaiah': 'Isa',
           'Jer': 'Jer',
           'Baruch': 'Bar',
           'EpJer': 'Lam', #
           'Lam': 'Epj', #
           'Ezek': 'Eze',
           'BelOG': 'Sus', #
           'BelTh': 'Sut', #
           'DanielOG': 'Dan',
           'DanielTh': 'Dat',
           'SusOG': 'Bel', #
           'SusTh': 'Bet' #
        }

    def _filename_emitter(self):

        book_abbr = BOOK_ABBR[:self.BOOK_LEN[0]]
        book_adapt = filter(lambda x: x not in ('Neh', 'Sip'), book_abbr)

        file_abbr = [v[0] if not isdigit(v[0][-1]) else v[0][:-1] for v in self._file_index.values()]
        file_attr = list(dict.fromkeys(file_abbr))

        for idx, data in sorted(self._file_index.items(), key=lambda x: x[0]):
            book, filename = data
            if filename.stem in self.OMITTED:
                continue
            yield filename, book if not isdigit(book[-1]) else book[:-1], idx

    def _filename_indexer(self):
        self._file_index = dict()
        files = [filename for filename in RecursiveIterator(self._path)]

        for filename in sorted(files, key=lambda x: x.stem):
            parts = filename.stem.split('.')
            num = parts[0]
            self._file_index[int(num)] = (parts[1], filename)


class IterCatSS(ContextObject):

    OMITTED = (
        'Pro 24', 'Pro 25', 'Pro 26', 'Pro 27', 'Pro 28', 'Pro 29', 'Pro 30',
        'Pro 31', 'Pro 33', 'Pro 33', 'Pro 34', 'Pro 35', 'Pro 36' # Disorder
        'Dat 3', # Five verses removed that exists in other editions of LXX
    )

    MAP = {
        'Gen': 'Gen', 'Exod': 'Exo', 'Lev': 'Lev', 'Num': 'Num', 'Deut': 'Deu',
        'JoshB': 'Jos', 'JoshA': 'Jsa', # Matched by chapter 15 for A version
        'JudgB': 'Jdg', 'JudgA': 'Jda', # Matched on having 11:4 for A version
        # later RH seems to prefer A version
        'Ruth': 'Rut',
        '1Sam/K': '1Sa', '2Sam/K': '2Sa', '1/3Kgs': '1Ki', '2/4Kgs': '2Ki', '1Chr': '1Ch',
        '2Chr': '2Ch', '1Esdr': '1Es', '2Esdr': '2Es', 'Esth': 'Est', 'Jdt': 'Jdt',
        'TobBA': 'Tob', 'TobS': 'Tbs', '1Mac': '1Ma', '2Mac': '2Ma', '3Mac': '3Ma',
        '4Mac': '4Ma', 'Ps': 'Psa', 'Od': 'Ode', 'Prov': 'Pro', 'Qoh': 'Ecc',
        'Cant': 'Sol', 'Job': 'Job', 'Wis': 'Wis', 'Sir Prolog': 'Sip', 'Sir': 'Sir',
        'PsSol': 'Pss', 'Hos': 'Hos', 'Mic': 'Mic', 'Amos': 'Amo', 'Joel': 'Joe',
        'Jonah': 'Jon', 'Obad': 'Oba', 'Nah': 'Nah', 'Hab': 'Hab', 'Zeph': 'Zep',
        'Hag': 'Hag', 'Zech': 'Zec', 'Mal': 'Mal', 'Isa': 'Isa', 'Jer': 'Jer',
        'Bar': 'Bar', 'EpJer': 'Epj', 'Lam': 'Lam', 'Ezek': 'Eze', 'Bel': 'Bel',
        'BelTh': 'Bet', 'Dan': 'Dan', 'DanTh': 'Dat', 'Sus': 'Sus', 'SusTh': 'Sut'
    }



    def __init__(self, file_iter: CatSSFileIter):
        super().__init__()
        self._file_iter = file_iter
        self._tokenizer = Tokenizer.beta_tokenizer()
        self._current = 'n/a'

    def __iter__(self):
        return self.iter()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), self._file_iter.current

    def _iterator(self):
        cur_book = ''
        cur_chapter = 0
        cur_verse = 0

        for filename, native_book_abbr, idx in self._file_iter:
            # print(filename, book, idx)
            with NlpContext(self):
                with open(filename, 'r') as f:
                    for lines in f.read().split('\n\n'):
                        lines = lines.strip()
                        sublines = lines.split('\n')
                        line = sublines[0].strip()
                        sub_verse = -1

                        if line == '':  # Unnatural empty row
                            continue
                        elif ' ' not in line:  # Unnatural row without ref part
                            # We assume this only happens before the coming 1st verse of next chapter
                            # Hopefully this only happens as a chapter prologue
                            cur_verse = 0
                            cur_chapter += 1
                            book = line
                            if book != cur_book:
                                cur_chapter = 1
                                cur_book = book
                            # yield BRef(book, cur_chapter, cur_verse, -1)
                            # print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                            continue

                        if line.startswith('Sir Prolog'):  # Correcting sirach prolog refs
                            book, chapter_verse = line.split(':')
                        else:  # Normal Book chapter:verse
                            book, chapter_verse = line.split(' ')
                        if book != cur_book:  # Reset chapter and verse
                            cur_verse = 1
                            cur_chapter = 1
                            cur_book = book
                        if ':' in chapter_verse:  # Normal chapter:verse ref
                            chapter, verse = chapter_verse.split(':')
                            cur_chapter = int(chapter)
                        else:  # For books with one implicit chapter
                            verse = chapter_verse
                            cur_chapter = 1
                        if '/' in verse:
                            cur_verse = int(verse.split('/')[0])
                            # yield BRef(book, cur_chapter, cur_verse, -1)
                            # print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif '-' in verse:
                            cur_verse = int(verse.split('-')[0])
                            # yield BRef(book, cur_chapter, cur_verse, -1)
                            # print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif len(verse) > 0 and isalpha(chapter_verse[-1]):
                            cur_verse = int(verse[:-1])
                            sub_verse = ord(verse[-1]) - 96
                            # yield BRef(book, cur_chapter, cur_verse, sub_verse)
                            # print("({}), {} {}:{}({})".format(line, cur_book, cur_chapter, cur_verse, sub_verse))
                        else:
                            cur_verse = int(verse)
                        self._current = (filename, cur_book, cur_chapter, cur_verse)

                        yield book, cur_chapter, cur_verse, sub_verse, sublines


    def iter_verse(self):
        for book_abbr, chapter_cnt, verse_cnt, sub_verse, _ in self._iterator():
            if sub_verse != -1:
                yield BRef(book_abbr, chapter_cnt, verse_cnt, -1)

    def iter_sub(self):
        for book_abbr, chapter_cnt, verse_cnt, sub_verse, _ in self._iterator():
            yield BRef(book_abbr, chapter_cnt, verse_cnt, sub_verse)

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text) # [PrintGreek.format(BetaWord.glyphen(b)) for b in self._tokenizer.tokenize(text)]

    def iter(self):
        cur_book = ''
        cur_chapter = 0
        cur_verse = 0

        for filename, native_book_abbr, idx in self._file_iter:
            #print(filename, book, idx)
            with NlpContext(self):
                with open(filename, 'r') as f:
                    for lines in f.read().split('\n\n'):
                        lines = lines.strip()
                        sublines = lines.split('\n')
                        line = sublines[0].strip()
                        sub_verse = -1

                        if line == '':  # Unnatural empty row
                            continue
                        elif ' ' not in line:  # Unnatural row without ref part
                            # We assume this only happens before the coming 1st verse of next chapter
                            # Hopefully this only happens as a chapter prologue
                            cur_verse = 0
                            cur_chapter += 1
                            book = line
                            if book != cur_book:
                                cur_chapter = 1
                                cur_book = book
                            #yield BRef(book, cur_chapter, cur_verse, -1)
                            #print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                            continue

                        if line.startswith('Sir Prolog'):  # Correcting sirach prolog refs
                            book, chapter_verse = line.split(':')
                        else:  # Normal Book chapter:verse
                            book, chapter_verse = line.split(' ')
                        if book != cur_book:  # Reset chapter and verse
                            cur_verse = 1
                            cur_chapter = 1
                            cur_book = book
                        if ':' in chapter_verse:  # Normal chapter:verse ref
                            chapter, verse = chapter_verse.split(':')
                            cur_chapter = int(chapter)
                        else:  # For books with one implicit chapter
                            verse = chapter_verse
                            cur_chapter = 1
                        if '/' in verse:
                            cur_verse = int(verse.split('/')[0])
                            #yield BRef(book, cur_chapter, cur_verse, -1)
                            # print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif '-' in verse:
                            cur_verse = int(verse.split('-')[0])
                            #yield BRef(book, cur_chapter, cur_verse, -1)
                            # print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif len(verse) > 0 and isalpha(chapter_verse[-1]):
                            cur_verse = int(verse[:-1])
                            sub_verse = ord(verse[-1]) - 96
                            #yield BRef(book, cur_chapter, cur_verse, sub_verse)
                            #print("({}), {} {}:{}({})".format(line, cur_book, cur_chapter, cur_verse, sub_verse))
                        else:
                            cur_verse = int(verse)
                        self._current = (filename, cur_book, cur_chapter, cur_verse)

                        corr_chap = cur_chapter
                        if self.MAP[book] == '2Es':
                            if cur_chapter <= 10:
                                corr_book = BOOK_ABBR[17]  #'Ezr'
                            else:
                                corr_book = BOOK_ABBR[18]  #'Neh'
                                corr_chap = cur_chapter - 10
                        else:
                            corr_book = self.MAP[book]

                        yield BRef(corr_book, corr_chap, cur_verse, sub_verse)

                        for line in sublines[1:]:
                            end = line.find(' ')
                            for token in self._tokenize(line[:end]):
                                yield token

        # print(dict(zip(self.MAP, BOOK_ABBR[:61])))
