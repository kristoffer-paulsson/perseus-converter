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
from curses.ascii import isdigit
from bs4 import BeautifulSoup

from perseusconverter.util.utils import BRef


class IterSinai:

    def __init__(self, xml: BeautifulSoup):
        self._xml = xml

    def __iter__(self):
        return self.iter_verse()

    def iter_verse(self):
        for book in self._xml.find_all('div', attrs={'type': 'book'}):
            # for chapter in book.find_all('div', attrs={'type': 'chapter'}):
            book_title = book.get('title')
            if book_title == 'Fragments':
                continue
            for chapter in book.find_all('div', attrs={'type': 'chapter'}):
                chapter_cnt = chapter.get('n')
                for ab in chapter.find_all('ab'):
                    verse_cnt = ab.get('n')
                    if len(verse_cnt) > 1 and not isdigit(verse_cnt[-1]):
                        verse_num = int(verse_cnt[:-1])
                        sub_verse = int(ord(verse_cnt[-1])) - 96
                    else:
                        verse_num = int(verse_cnt)
                        sub_verse = -1
                    yield BRef(book_title, int(chapter_cnt), verse_num, sub_verse)

    def iter_sub(self):
        books = dict()

        chapter_num = 0
        verse_num = 0
        sub_verse = -1
        for book in self._xml.find_all('div', attrs={'type': 'book'}):
            book_title = book.get('title')
            if book_title == 'Fragments':
                continue
            books[book_title] = dict()

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
                        sub_verse = int(ord(r_parts[1][-1])) - 96
                        verse_num = int(r_parts[1][:-1])
                    else:
                        verse_num = int(r_parts[1].strip())
                else:
                    if chapter_verse.find('-') != -1:
                        verse_num = int(chapter_verse.split('-')[0])
                    elif len(chapter_verse) > 1 and not isdigit(chapter_verse[-1]):
                        sub_verse = int(ord(chapter_verse[-1])) - 96
                        verse_num = int(chapter_verse[:-1])
                    else:
                        verse_num = int(chapter_verse.strip())

                if sub_verse != -1:
                    ref = BRef(book_title, chapter_num, verse_num, sub_verse)
                    sub_verse = -1
                    yield ref
                else:
                    yield BRef(book_title, chapter_num, verse_num, -1)


    def iter(self):
        pass