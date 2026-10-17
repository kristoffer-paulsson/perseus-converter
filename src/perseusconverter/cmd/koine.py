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
import itertools
import re
from argparse import Namespace
from curses.ascii import isblank, isalpha

from bs4 import BeautifulSoup
from lxml.etree import XMLSyntaxError
from numpy.matlib import empty

from greektextify.nlp.contextual import NlpContext
from biblebuilder.scan.nocrvt import NocrVtScanner
from . import Command
from ..app import Config, logging
from ..recursiveiterator import RecursiveIterator
from ..traverse.bibbgt import BgtTraverser
from ..traverse.general import AbstractTeiTraverser
from ..traverse.lsjlex import LsjTraverser
from ..traverse.rgnt import RockTraverser

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
                raise RuntimeError("Dictionaru file missing: {}".format(str(filename)))
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
            self._lex_lsj()
        elif self._args.corpora == 'rock':
            self._rgnt()
        else:
            pass

    def _nocr(self):

        LOWER_OFFICIAL = [x.lower() for x in OFFICIAL_VETUS]

        MAP_OFFICIAL = dict(zip(LOWER_OFFICIAL, OFFICIAL_VETUS))

        filename = self.target.joinpath("bible-analyzer-corpora/corpora/nocr")

        files = [filename for filename in RecursiveIterator(filename)]

        books_index = dict()
        #num_order = dict()
        for filename in sorted(files, key=lambda x: x.stem):
            parts = filename.stem.split('.')
            book = parts[0]
            chapter = int(parts[1])
            if book not in books_index:
                books_index[book] = dict()
            books_index[book][chapter] = filename
        #    num_order[int(parts[2])] = filename

        abbr_set = set([x.lower() for x in OFFICIAL_VETUS])

        if set(books_index.keys()) != abbr_set:
            raise RuntimeError("Book OT abbreviations not valid: {}".format(books_index))

        for book, chapters in books_index.items():
            chapter_index = set(chapters.keys())
            chapter_set = set(range(1, len(chapters) + 1))

            if chapter_index != chapter_set:
                raise RuntimeError("Chapter OT index not valid: {}".format(chapter_set))

        for book, chapters in sorted(books_index.items(), key=lambda x: LOWER_OFFICIAL.index(x[0])):
            chapter_verify = CountVerify(len(chapters))
            for chapter, filename in sorted(chapters.items()):
                chapter_verify.verify(chapter)
                with open(filename, 'r') as f:
                    # print("Working: {}".format(filename))
                    html = BeautifulSoup(f, 'html.parser')
                    header = html.find('h2')
                    if hasattr(header, 'text'):
                        #print(html.find('h2').text)
                        if int(header.text.split(' ')[-1]) != chapter:
                            print("Header chapter not consistent: {}".format(filename))
                    else:
                        print("No header found: {}".format(filename))

                    verses = html.find_all('sup')
                    verses_verify = CountVerify(len(verses))
                    last_v_num = -1
                    for verse in verses:
                        if hasattr(verse, 'text'):
                            c_num, v_num = verse.text.strip().split(':')
                            if int(c_num) != chapter:
                                print("Verse chapter {}  not consistent: {}".format(chapter, filename))
                            if verses_verify.verify_no_exc(int(v_num)):
                                last_v_num = v_num
                            else:
                                print("Expected verse {} but got {}: {}".format(last_v_num, v_num, filename))
                        else:
                            print("No verse {} found: {}".format(last_v_num, filename))

                    #data = html.find('td', attrs={'width': '75%', 'border': '0'})
                    data = html.find_all('table', attrs={'width': '75%', 'border': '0'})
                    if len(data) < 3:
                        print("No verse corpus found (1): {}".format(filename))
                    else:
                        if not hasattr(data[2], 'text'):
                            print("No verse corpus found (2): {}".format(filename))
                        else:
                            rows = list()
                            for row in data[2].text.strip().split('\n'):
                                row = row.strip()
                                if row != '':
                                    rows.append(row)
                                    first_space_idx = row.find(' ')
                                    if first_space_idx == -1:
                                        print("Verse without corpus found {} {}, {}".format(MAP_OFFICIAL[book], row, filename))
                                    else:
                                        ref_txt = row[:first_space_idx].strip()
                                        v_txt = row[first_space_idx:].strip()
                                        subv_cnt = len(re.findall(r"\[\d+\]", v_txt))
                                        if subv_cnt > 0:
                                            print("Verse contains {} sub-verse(s) in {} {}, {}".format(subv_cnt, MAP_OFFICIAL[book], ref_txt, filename))

    def _rgnt(self):
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

        for idx, filename in sorted(num_order.items(), key=lambda x: x[0]):
            with open(filename, 'r') as f:
                # print("Working: {}".format(filename))
                html = BeautifulSoup(f, 'html.parser')
                book = html.find('span', attrs={'id': 'h2'})
                if hasattr(book, 'text'):
                    book_name = book.text.split(' ')[1]
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
                print(filename)
                if chapter_num == '_':
                    chapter_cnt = 1
                else:
                    chapter_cnt = int(chapter_num)
                for v in verse:
                    v2 = v.text.split(' ')[1].strip()
                    split_index = v2.find('-')
                    if split_index != -1:
                        v_from = int(v2[:split_index])
                        v_to = int(v2[split_index + 1:])
                        for v3 in range(v_from, v_to+1):
                            verse_cnt = int(v3)
                            print(greek_name, book_name, chapter_cnt, verse_cnt)
                    else:
                        if isalpha(v2[-1]):
                            verse_cnt = int(v2[:-1])
                            subv_cnt = ord(v2[-1]) - 96
                            print(greek_name, book_name, chapter_cnt, verse_cnt, subv_cnt)
                        else:
                            verse_cnt = int(v2)
                            subv_cnt = 0
                            print(greek_name, book_name, chapter_cnt, verse_cnt)

                #if hasattr(header, 'text'):
                #    # print(html.find('h2').text)
                #    if int(header.text.split(' ')[-1]) != chapter:
                #        print("Header chapter not consistent: {}".format(filename))
                #else:
                #    print("No header found: {}".format(filename))


class ListVerify:
    def __init__(self, target: list):
        self._target = target
        self._index = 0

    def verify(self, item):
        if not self.verify_no_exc(item):
            raise RuntimeError("Verified item not in lieu: {}".format(item))

    def verify_no_exc(self, item) -> bool:
        result = item == self.show_cur()
        self._index += 1
        return result

    def show_cur(self):
        return self._target[self._index]


class CountVerify(ListVerify):
    def __init__(self, length: int,):
        super().__init__(list(range(1, length + 1)))

