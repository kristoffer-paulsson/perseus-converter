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
import collections
import re
import string
from argparse import Namespace
from curses.ascii import isalpha, isdigit

from bs4 import BeautifulSoup
from lxml.etree import XMLSyntaxError

from greektextify.nlp.contextual import NlpContext
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.bracket import Bracketing
from greektextify.text.database import GreekDatabase
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway
from . import Command
from ..app import Config, logging
from ..iter.bgmiter import IterBGM, BRef
from ..iter.bgtiter import IterBGT
from ..iter.catssiter import IterCatSS, CatSSFileIter
from ..iter.fileiter import NocrFileIter, IterNocr
from ..iter.sinaiiter import IterSinai
from ..recursiveiterator import RecursiveIterator
from ..traverse.bibbgt import BgtTraverser
from ..traverse.general import AbstractTeiTraverser
from ..traverse.lsjlex import LsjTraverser
from ..traverse.rgnt import RockTraverser
from ..util.collector import Counter, Collector
from ..util.utils import ListVerify, CountVerify

BETACODE = (
    'tlg2003.tlg008.perseus-grc1.xml',
    'tlg2003.tlg002.perseus-grc1.xml',
    'tlg2003.tlg011.perseus-grc1.xml',
    'tlg2003.tlg005.perseus-grc1.xml',
    'tlg2003.tlg001.perseus-grc1.xml',
    'tlg2003.tlg012.perseus-grc1.xml',
    'tlg2003.tlg006.perseus-grc1.xml',
    'tlg2003.tlg004.perseus-grc1.xml',
    'tlg2003.tlg010.perseus-grc1.xml',
    'tlg2003.tlg003.perseus-grc1.xml',
    'tlg2003.tlg009.perseus-grc1.xml',
    'tlg2003.tlg007.perseus-grc1.xml',
    'tlg2040.tlg002.perseus-grc1.xml',
)


VETUS = {
    'Gen': (True, 'gen', 1, 50),
    'Exo': (True, 'ex', 1, 40),
    'Lev': (True, 'lev', 1, 27),
    'Num': (True, 'num', 1, 36),
    'Deu': (True, 'deut', 1, 34),
    'Jsa': (False, 'jos', 212, 214),
    'Jos': (False, 'jos', 188, 211),
    'Jda': (False, 'ju', 236, 256),
    'Jdg': (False, 'ju', 215, 235),
    'Rut': (True, 'ru', 1, 4),
    '1Sa': (True, 'regi', 1, 31),
    '2Sa': (True, 'regii', 1, 24),
    '1Ki': (True, 'regiii', 1, 22),
    '2Ki': (True, 'regiv', 1, 25),
    '1Ch': (True, 'chri', 1, 29),
    '2Ch': (True, 'chrii', 1, 36),
    '1Es': (True, 'esri', 1, 9),
    'Ezr': (False, 'esrii', 437, 446),
    'Neh': (False, 'esrii', 447, 459),
    'Est': (True, 'esth', 1, 10),
    'Jdt': (True, 'jud', 1, 16),
    'Tob': (True, 'tob', 1, 14),
    'Tbs': (True, 'tobs', 1, 14),
    '1Ma': (True, 'macci', 1, 16),
    '2Ma': (True, 'maccii', 1, 15),
    '3Ma': (True, 'macciii', 1, 7),
    '4Ma': (True, 'macciv', 1, 18),
    'Psa': (True, 'ps', 1, 151),
    'Ode': (True, 'od', 1, 15),
    'Pro': (True, 'prov', 1, 34),
    'Ecc': (True, 'eccl', 1, 12),
    'Sol': (True, 'cant', 1, 8),
    'Job': (True, 'hiob', 1, 42),
    'Wis': (False, 'sapsal', 832, 850),
    'Sip': (False, 'sapsal', 851, 851),
    'Sir': (False, 'sapsal', 852, 902),
    'Pss': (True, 'pssal', 1, 18),
    'Hos': (True, 'hos', 1, 14),
    'Amo': (True, 'am', 1, 9),
    'Mic': (True, 'mich', 1, 7),
    'Joe': (False, 'joel', 951, 954),
    'Oba': (False, 'joel', 955, 955),
    'Jon': (True, 'jon', 1, 4),
    'Nah': (True, 'nah', 1, 3),
    'Hab': (True, 'hab', 1, 3),
    'Zep': (True, 'soph', 1, 3),
    'Hag': (False, 'agg', 1, 2),
    'Zec': (True, 'zach', 1, 14),
    'Mal': (True, 'mal', 1, 3),
    'Isa': (True, 'is', 1, 66),
    'Jer': (True, 'jer', 1, 52),
    'Bar': (True, 'bar', 1, 5),
    'Lam': (False, 'lamjer', 1111, 1115),
    'Epj': (False, 'lamjer', 1116, 1116),
    'Eze': (False, 'ez', 1117, 1164),
    'Sus': (False, 'ez', 1165, 1165),
    'Sut': (False, 'ez', 1166, 1166),
    'Dan': (True, 'dans', 1, 12),
    'Dat': (False, 'danth', 1179, 1190),
    'Bel': (False, 'danth', 1191, 1191),
    'Bet': (False, 'danth', 1192, 1192)
}

OFFICIAL_VETUS = [
    'Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jsa', 'Jos', 'Jda', 'Jdg', 'Rut', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch',
    '2Ch', '1Es', 'Ezr', 'Neh', 'Est', 'Jdt', 'Tob', 'Tbs', '1Ma', '2Ma', '3Ma', '4Ma', 'Psa', 'Ode', 'Pro',
    'Ecc', 'Sol', 'Job', 'Wis', 'Sip', 'Sir', 'Pss', 'Hos', 'Amo', 'Mic', 'Joe', 'Oba', 'Jon', 'Nah', 'Hab',
    'Zep', 'Hag', 'Zec', 'Mal', 'Isa', 'Jer', 'Bar', 'Lam', 'Epj', 'Eze', 'Sus', 'Sut', 'Dan', 'Dat', 'Bel',
    'Bet'
]

BOOK_NAME = [
            'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua (A)', 'Joshua', 'Judges (A)', 'Judges',
            'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', '1 Esdras', 'Ezra',
            'Nehemiah', 'Esther', 'Judith', 'Tobit', 'Tobit (S)', '1 Maccabees', '2 Maccabees', '3 Maccabees',
            '4 Maccabees', 'Psalm', 'Odes', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Job', 'Wisdom',
            'Sirach Prolog', 'Sirach', 'Psalms of Solomon', 'Hosea', 'Amos', 'Micah', 'Joel', 'Obadiah', 'Jonah',
            'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Isaiah', 'Jeremiah', 'Baruch',
            'Lamentations', 'Epistle of Jeremiah', 'Ezekiel', 'Susanna', 'Susanna (TH)', 'Daniel', 'Daniel (TH)', 'Bel',
            'Bel (TH)', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians',
            'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy',
            '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John',
            'Jude', 'Revelation'
        ]

BOOK_ABBR = [
            'Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jsa', 'Jos', 'Jda', 'Jdg', 'Rut', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch',
            '2Ch', '1Es', 'Ezr', 'Neh', 'Est', 'Jdt', 'Tob', 'Tbs', '1Ma', '2Ma', '3Ma', '4Ma', 'Psa', 'Ode', 'Pro',
            'Ecc', 'Sol', 'Job', 'Wis', 'Sip', 'Sir', 'Pss', 'Hos', 'Amo', 'Mic', 'Joe', 'Oba', 'Jon', 'Nah', 'Hab',
            'Zep', 'Hag', 'Zec', 'Mal', 'Isa', 'Jer', 'Bar', 'Lam', 'Epj', 'Eze', 'Sus', 'Sut', 'Dan', 'Dat', 'Bel',
            'Bet', 'Mat', 'Mar', 'Luk', 'Joh', 'Act', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Phi', 'Col', '1Th', '2Th',
            '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jam', '1Pe', '2Pe', '1Jo', '2Jo', '3Jo', 'Jud', 'Rev'
        ]


class KoineCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def _pdl(self):
        count = 0
        for filename in RecursiveIterator(self.target.joinpath("canonical-greekLit/data/")):
            if not filename.is_file() or not filename.name[23:].startswith('grc') or not filename.name.endswith('.xml'):
                self.logger.warn("Registered but missing file: {}".format(filename))
                continue
            self.logger.info("Processing file: {}".format(filename))
            try:
                with NlpContext(AbstractTeiTraverser.open(filename), self.logger) as xml:
                    if isinstance(xml, AbstractTeiTraverser):
                        if filename.name in BETACODE:
                            self.logger.info("Traversing file {}".format(filename.name))
                            xml.traverse()
                        count += 1
            except XMLSyntaxError as e:
                self.logger.warn("{}: {}".format(e.__class__, str(e)))

        print(count)

    def _bib(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgt.txt")
        txt = BgtTraverser(filename)
        txt.traverse()
        for filename in RecursiveIterator(self.target.joinpath("bible-analyzer-corpora/corpora/abcom/")):
            if not filename.is_file():
                self.logger.warn("Registered but missing file: {}".format(filename))
                continue
            self.logger.info("Processing file: {}".format(filename))
            txt = BgtTraverser(filename)
            for token in txt.traverse():
                print(token)

    def _lex_lsj(self):
        counter = 0
        error = 0
        for number in range(1, 27+1):
            filename = self.target.joinpath("lexica/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng{}.xml".format(number))
            if not filename.is_file():
                raise RuntimeError("Dictionary file missing: {}".format(str(filename)))
            try:
                with NlpContext(LsjTraverser.open(filename), self.logger) as xml:
                    xml.traverse()
                    counter += xml.counter
                    error += xml.error
            except XMLSyntaxError as e:
                self.logger.warn("{}: {}".format(e.__class__, str(e)))
        print("Entries: {}".format(counter))
        print("Failed: {}".format(error))

    def __call__(self):
        if self._args.corpora == 'bib':
            self._bib()
        elif self._args.corpora == 'pdl':
            self._pdl()
        elif self._args.corpora == 'lex':
            self._bgm()
        elif self._args.corpora == 'bgt':
            self._bgt()
        elif self._args.corpora == 'sinai':
            self._sinai()
        elif self._args.corpora == 'nocr':
            self._nocr()
        elif self._args.corpora == 'sept3':
            self._sept3()
        elif self._args.corpora == 'catss':
            self._catss()
        elif self._args.corpora == 'check':
            self._meta()
        else:
            pass

    def _sinai(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/FINAL_TRANSCRIPTION_version104.xml")

        #books = dict()
        #marked = set()

        with open(filename, 'r') as f:
            siter = IterSinai(BeautifulSoup(f, 'xml'))
            collect = Collector(siter)
            collect.collect()
            collect.analyze()

            exit()
            chapter_num = 0
            verse_num = 0
            sub_verse = ''
            last_word = ''
            chapter_changed = True
            for book in xml.find_all('div', attrs={'type': 'book'}):
                # for chapter in book.find_all('div', attrs={'type': 'chapter'}):
                book_title = book.get('title')
                if book_title == 'Fragments':
                    continue
                books[book_title] = dict()
                print('\n\n', book_title)
                for chapter in book.find_all('div', attrs={'type': 'chapter'}):
                    chapter_cnt = chapter.get('n')
                    chapter_changed = True
                    for ab in chapter.find_all('ab'):
                        verse_cnt = ab.get('n')
                        if chapter_changed:
                            print('\n{' + chapter_cnt + ':' + verse_cnt + '}', end=' ')
                            chapter_changed = False
                        else:
                            print('{' + verse_cnt + '}', end=' ')

                        for child in ab.find_all('w'):
                            # choosing last correction of an apparatus to avoid doubles
                            app = child.find_parent('app')
                            if app is not None:
                                rdgs = app.find_all('rdg', attrs={'type': 'corr'})
                                rdg = child.find_parent('rdg')
                                if rdgs[-1] is not rdg:
                                    continue

                            note = child.find('note')
                            if note:
                                note.decompose()
                            nomina = child.find('hi', attrs={'rend': 'ol2'})
                            text = child.text.strip()
                            if nomina:
                                marked.add(text.replace('\n', ''))
                            word = text.replace('\n', ' ')
                            if word == '':
                                continue
                            print(word, end=' ')

                for verse in book.find_all('lb', attrs={'vnumber': True}):
                    chapter_verse = verse.get('vnumber').strip()

                    if chapter_verse.find('/'):
                        chapter_verse = chapter_verse.split('/')[0].strip()

                    if chapter_verse.find(':') != -1:
                        r_parts = chapter_verse.split(':')
                        chapter_num = int(r_parts[0].strip())
                        if r_parts[1].find('-') != -1:
                            verse_num = int(r_parts[1].split('-')[0])
                        elif len(r_parts[1]) > 1 and not isdigit(r_parts[1][-1]):
                            sub_verse = ord(r_parts[1][-1]) - 96
                            verse_num = int(r_parts[1][:-1])
                        else:
                            verse_num = int(r_parts[1].strip())
                    else:
                        if chapter_verse.find('-') != -1:
                            verse_num = int(chapter_verse.split('-')[0])
                        elif len(chapter_verse) > 1 and not isdigit(chapter_verse[-1]):
                            sub_verse = ord(chapter_verse[-1]) - 96
                            verse_num = int(chapter_verse[:-1])
                        else:
                            verse_num = int(chapter_verse.strip())

                    if books[book_title].get(chapter_num) is None:
                        books[book_title][chapter_num] = dict()
                    if books[book_title][chapter_num].get(verse_num) is None:
                        books[book_title][chapter_num][verse_num] = list()
                    if sub_verse != 0:
                        books[book_title][chapter_num][verse_num].append(sub_verse)
                        sub_verse = 0

                    #print(book_title, "{}:{}".format(chapter_num, verse_num))
        print(books)
        for marking in sorted(marked, key=lambda x: len(x)):
            print(marking, end='" - "')

    def _bgt(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgt.txt")
        with filename.open('r') as f:
            viter = IterBGT(f)
            collect = Collector(viter)
            collect.collect()
            #collect.analyze()

            filename2 = self.target.joinpath("bible-analyzer-corpora/corpora/bgm.txt")
            with filename2.open('r') as f:
                viter2 = IterBGM(f)
                collect2 = Collector(viter2)
                collect2.collect()
                #collect2.analyze()

                print(collect.difference(collect2))

    def _bgm(self):
        dictionary = dict()
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgm.txt")
        with filename.open('r') as f:
            viter = IterBGM(f)
            for token in viter.iter():
                if isinstance(token, str):
                    if token not in dictionary:
                        dictionary[token] = 1
                    else:
                        dictionary[token] += 1

            #filter(dictionary, )

            ordered = collections.OrderedDict(sorted(dictionary.items()))
            print(ordered)
            print(len(ordered))
            print(sum(dictionary.values()))

            exit()
            for line in f:
                line = line.strip()
                fst = line.find(' ')+1
                idx = line.find(':')
                idy = line.find(' ', idx)
                idv = line.rfind(' ', fst, idx)
                book_abbr = BOOK_ABBR[BOOK_NAME.index(line[fst:idv])]
                chapter_num, verse_num = line[idv:idy].split(':')
                ref = "{} {}:{}".format(book_abbr, chapter_num.strip(), verse_num.strip())
                # print('\n', ref, end=' ')
                sub_verse = -1
                sref = ref
                for t in line[idy:].strip().split(' '):
                    svs = t.find('[')
                    if svs != -1:
                        sve = t.find(']')
                        sub_verse = int(t[(svs+1):(sve)])
                        sref = "{}({})".format(ref, sub_verse)
                    else:
                        tag = t.split('@')[0]
                        if tag not in dictionary:
                            dictionary[tag] = list()
                        dictionary[tag].append(sref)

        for key in sorted(dictionary, key=lambda x: x):
            print(key, len(dictionary[key]))

    def _catss(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/catss")
        citer = IterCatSS(CatSSFileIter(filename))
        collect = Collector(citer)
        collect.collect()
        #collect.analyze()

        filename2 = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")
        niter = IterNocr(NocrFileIter(filename2))
        collect2 = Collector(niter)
        collect2.collect()
        #collect2.analyze()

        print(collect.difference(collect2))
        exit()


        files = [filename for filename in RecursiveIterator(filename)]

        books_index = dict()
        num_order = dict()
        for filename in sorted(files, key=lambda x: x.stem):
            parts = filename.stem.split('.')
            num = parts[0]
            # book = parts[1]
            #if book not in books_index:
            #    books_index[book] = dict()
            #books_index[book][chapter] = filename
            num_order[int(num)] = filename

            cur_book = ''
            cur_chapter = 0
            cur_verse = 0

            for idx, filename in sorted(num_order.items(), key=lambda x: x[0]):
                with open(filename, 'r') as f:
                    after_empty = False
                    before_verse = True
                    refs = list()
                    # print(filename)
                    for lines in f.read().split('\n\n'):
                        lines = lines.strip()
                        line = lines.split('\n')[0].strip()

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
                            print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
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
                            print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif '-' in verse:
                            cur_verse = int(verse.split('-')[0])
                            print("({}), {} {}:{}".format(line, cur_book, cur_chapter, cur_verse))
                        elif len(verse) > 0 and isalpha(chapter_verse[-1]):
                            cur_verse = int(verse[:-1])
                            sub_verse = ord(verse[-1]) - 96
                            print("({}), {} {}:{}({})".format(line, cur_book, cur_chapter, cur_verse, sub_verse))
                        else:
                            cur_verse = int(verse)
                            # print("{} {}:{}".format(cur_book, cur_chapter, cur_verse))
                        #refs.append(line)

                        # print(line)
                        #if line == '':
                        #    before_verse = True
                        #if before_verse:
                        #    before_verse = False
                        #else:
                        #    pass
                    #print(refs)

    def _nocr(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")
        niter = IterNocr(NocrFileIter(filename))
        collect = Collector(niter)
        collect.collect()
        #collect.analyze()

        filename2 = self.target.joinpath("bible-analyzer-corpora/corpora/catss")
        citer = IterCatSS(CatSSFileIter(filename2))
        collect2 = Collector(citer)
        collect2.collect()
        # collect.analyze()

        print(collect.difference(collect2))
        exit()
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/bgm.txt")
        with filename.open('r') as f:
            viter = IterBGM(f)
            collect2 = Collector(viter)
            collect2.collect()

            print(collect.difference(collect2))
            print(collect2.difference(collect))


    def _sept3(self):
        filename = self.target.joinpath("bible-analyzer-corpora/corpora/septuagint3")

        files = [filename for filename in RecursiveIterator(filename)]

        books_index = dict()
        num_order = dict()
        book_verify = CountVerify(len(files))
        for filename in sorted(files, key=lambda x: int(x.stem.split('-')[2])):
            parts = filename.stem.split('-')
            book = parts[0]
            chapter = int(parts[1])
            num = int(parts[2])
            book_verify.verify(num)
            if book not in books_index:
                books_index[book] = dict()
            books_index[book][chapter] = filename
            num_order[num] = filename

        jos_a = {1: 15, 2: 18, 3: 19}

        chapter_cnt = Counter()
        sub_chapter_cnt = Counter()
        verse_cnt = Counter()
        subverse_cnt = Counter()
        for idx, filename in sorted(num_order.items(), key=lambda x: x[0]):
            with open(filename, 'r') as f:
                # print("Working: {}".format(filename))
                html = BeautifulSoup(f, 'html.parser')

                spans = html.find_all('span')
                for span in spans:
                    span_id = span.get('id')
                    if span_id == 'h2':
                        b_part = span.text.split(' ')
                        book_abbr = b_part[1].strip()
                        print(book_abbr)
                        if book_abbr == 'Sir.':
                            chapter_cnt.reset(-1)
                        else:
                            chapter_cnt.reset()
                        if book_abbr in ('Od.', '-') and verse_num in (1,): # 9a
                            verse_cnt.reset(-1)
                        else:
                            verse_cnt.reset()
                    elif span_id == 'h3':
                        c_part = span.text.split(' ')
                        chapter = c_part[1].strip()
                        if chapter.find('_') != -1 and len(chapter) > 1:
                            chapter = chapter.split('_')[0].strip()
                        if chapter == '_':
                            chapter_num = 1
                        elif len(chapter) > 0 and isalpha(chapter[-1]): # Od 9 specific
                            if sub_chapter_cnt.current() == 0:
                                chapter_cnt.increment()
                            sub_chapter_cnt.increment()
                            chapter_num = int(chapter[:-1])
                        else:
                            if sub_chapter_cnt.current() != 0:
                                sub_chapter_cnt.reset()
                            chapter_num = int(chapter)
                        if sub_chapter_cnt.current() == 0:
                            if book_abbr in ('Jos._A', '-'):
                                if jos_a[chapter_cnt.increment()] != chapter_num:
                                    print("Chapter {} not consistent with {}: {}".format(chapter, chapter_cnt.current(), filename, idx))
                            elif chapter_cnt.increment() != chapter_num:
                                print("Chapter {} not consistent with {}: {}".format(chapter, chapter_cnt.current(), filename, idx))
                        else:
                            if chapter_cnt.current() != chapter_num:
                                print("Chapter {} not consistent with {}: {}".format(chapter, chapter_cnt.current(), filename, idx))
                        if book_abbr in ('Od.', '-') and verse_num in (1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14): # 9a
                            verse_cnt.reset(-1)
                        else:
                            verse_cnt.reset()
                        # print(chapter_num)
                    elif span_id == 'h4':
                        v_parts = span.text.split(' ')
                        verse = v_parts[1].strip()
                        if '/' in verse:
                            verse = verse.split('/')[0]
                            subverse_cnt.reset()
                        elif '-' in verse:
                            verse = verse.split('-')[0]
                            subverse_cnt.reset()
                        if len(verse) > 0 and isalpha(verse[-1]):
                            verse_num = int(verse[:-1])
                            sub_verse = ord(verse[-1]) - 96
                            while subverse_cnt.increment() < sub_verse:
                                print("Sub-verse {}:{}({}) is missing: {}".format(chapter_num, verse_num, subverse_cnt.current(), filename))
                            print("{} {}:{}({})".format(book_abbr, chapter_num, verse_num, sub_verse))
                        else:
                            verse_num = int(verse)
                            subverse_cnt.reset()
                            while verse_cnt.increment() < verse_num:
                                print("Verse {}:{} is missing: {}".format(chapter_num, verse_cnt.current(), filename))

                        #print(span.text)
                    elif span_id == 'gr16':
                        pass
                        # print(span.text)
                    else:
                        pass

                """book = html.find('span', attrs={'id': 'h2'})
                if hasattr(book, 'text'):
                    book_name = book.text.split(' ')[1]
                    if previous_book != book_name:
                        previous_book = book_name
                        chapter_cnt_exp = 0
                greek = html.find('span', attrs={'id': 'gr22'})
                if hasattr(greek, 'text'):
                    greek_name = html.find('span', attrs={'id': 'gr22'}).text
                chapter = html.find('span', attrs={'id': 'h3'})
                if hasattr(chapter, 'text'):
                    chapter_num = chapter.text.split(' ')[1][:-1].strip()
                    if chapter_num.find('_') != -1 and len(chapter_num) > 1:
                        chapter_num = chapter_num.split('_')[0]
                    if isalpha(chapter_num[-1]) and len(chapter_num) > 1:
                        chapter_num = chapter_num[:-1]
                else:
                    chapter_num = '_'
                # Scan for spans and ceertain id:s in a type of state loop to extract full verses
                #spans = html.find_all('span')
                #for span in spans:
                #    print(span.get('id'))
                verse = html.find_all('span', attrs={'id': 'h4'})
                # print(filename)
                if chapter_num == '_':
                    chapter_cnt = 1
                    verse_cnt_exp = 0
                else:
                    chapter_cnt = int(chapter_num)
                    verse_cnt_exp = 0
                chapter_cnt_exp += 1
                if chapter_cnt_exp != chapter_cnt:
                    print("Chapter {} != {} not consistent: {}".format(chapter_cnt_exp, chapter_cnt, filename))
                for v in verse:
                    v2 = v.text.split(' ')[1].strip()
                    split_index = v2.find('-')
                    if split_index != -1:
                        v_from = int(v2[:split_index])
                        v_to = int(v2[split_index + 1:])
                        for v3 in range(v_from, v_to+1):
                            verse_cnt = int(v3)
                            #print(greek_name, book_name, chapter_cnt, verse_cnt)
                    else:
                        if isalpha(v2[-1]):
                            verse_cnt = int(v2[:-1])
                            subv_cnt = ord(v2[-1]) - 96
                            #print(greek_name, book_name, chapter_cnt, verse_cnt, subv_cnt)
                        else:
                            verse_cnt = int(v2)
                            subv_cnt = 0
                            #print(greek_name, book_name, chapter_cnt, verse_cnt)
                    verse_cnt_exp += 1
                    if verse_cnt_exp != verse_cnt:
                        # print("Verse {} != {} not consistent: {}".format(verse_cnt_exp, verse_cnt, filename))
                        pass"""

    def _meta(self):
        greek_dict = dict(GreekDatabase.ALL_UTF_LETTERS)
        for letter in GreekAlphabet.ALPHABET:
            if letter not in greek_dict:
                print("Letter {} is missing in GreekDatabase".format(letter))

        for letter in GreekExtended.LETTERS:
            if letter not in greek_dict:
                print("Letter {} is missing in GreekDatabase".format(letter))

        for letter in GreekMidway.LETTERS:
            if letter not in greek_dict:
                print("Letter {} is missing in GreekDatabase".format(letter))

        combined_letters = set(
            list(GreekAlphabet.ALPHABET) + list(GreekExtended.LETTERS) +
            list(GreekMidway.LETTERS) + list(GreekMidway.MODIFIERS)
        )
        dict_letters = set(greek_dict.keys())
        if dict_letters - combined_letters:
            print("Combined letters {}".format(dict_letters - combined_letters))

        if combined_letters - dict_letters:
            print("Combined letters {}".format(combined_letters - dict_letters))

        combined_others = set(
            list(GreekDiacritic.DIACRITICS) + list(GreekExtended.DIACRITICS) +
            list(Bracketing.BRACKETS) # + list(GreekMidway.MODIFIERS)
        )
        if dict_letters & combined_others:
            print("Combined others {}".format(dict_letters & combined_others))

        for diacritic in GreekDiacritic.DIACRITICS:
            if diacritic in greek_dict:
                print("Diacritic {} is missing in GreekDatabase".format(diacritic))

        for diacritic in GreekExtended.DIACRITICS:
            if diacritic in greek_dict:
                print("Diacritic {} is missing in GreekDatabase".format(diacritic))

        upper = string.ascii_uppercase + '_'
        valid_attr = set()
        remove = ('ALL_UTF_LETTERS', 'LEGAL', 'DEBUG_CIRCLE')
        for attr in GreekDatabase.__dict__.keys():
            if all(char in upper for char in attr):
                if attr not in remove:
                    valid_attr.add(attr)

        for attr in valid_attr:
            if GreekDatabase.__dict__[attr][0] not in dict_letters:
                print("{} not in GreekDatabase".format(GreekDatabase.__dict__[attr][0]))

        print(len(GreekAlphabet.FROM_LOWER), len(GreekAlphabet.FROM_UPPER), len(GreekAlphabet.CASE_LOWER), len(GreekAlphabet.CASE_UPPER))

