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
from typing import Dict, List

from bs4 import BeautifulSoup

from greektextify.text.word import GreekWord
from perseusconverter.traverse.nocr import NocrTraverser
from .scanner import Scanner, WideToken
from pathlib import Path


CHAPTER_COUNT = {
    'Gen': 50, 'Exo': 40, 'Lev': 27, 'Num': 36, 'Deu': 34, 'Jsa': 19, 'Jos': 24, 'Jda': 21, 'Jdg': 21, 'Rut': 4,
    '1Sa': 31, '2Sa': 24, '1Ki': 22, '2Ki': 25, '1Ch': 29, '2Ch': 36, '1Es': 9, 'Ezr': 10, 'Neh': 13, 'Est': 10,
    'Jdt': 16, 'Tob': 14, 'Tbs': 14, '1Ma': 16, '2Ma': 15, '3Ma': 7, '4Ma': 18, 'Psa': 151, 'Ode': 14, 'Pro': 31,
    'Ecc': 12, 'Sol': 8, 'Job': 42, 'Wis': 19, 'Sip': 1, 'Sir': 51, 'Pss': 18, 'Hos': 14, 'Amo': 9, 'Mic': 7, 'Joe': 4,
    'Oba': 1, 'Jon': 4, 'Nah': 3, 'Hab': 3, 'Zep': 3, 'Hag': 2, 'Zec': 14, 'Mal': 3, 'Isa': 66, 'Jer': 52, 'Bar': 5,
    'Lam': 5, 'Epj': 1, 'Eze': 48, 'Sus': 1, 'Sut': 1, 'Dan': 12, 'Dat': 12, 'Bel': 1, 'Bet': 1
}


class NocrVtScanner(Scanner):

    @property
    def book_abbr(self) -> List[str]:
        return [
            'Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jsa', 'Jos', 'Jda', 'Jdg', 'Rut', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch',
            '2Ch', '1Es', 'Ezr', 'Neh', 'Est', 'Jdt', 'Tob', 'Tbs', '1Ma', '2Ma', '3Ma', '4Ma', 'Psa', 'Ode', 'Pro',
            'Ecc', 'Sol', 'Job', 'Wis', 'Sip', 'Sir', 'Pss', 'Hos', 'Amo', 'Mic', 'Joe', 'Oba', 'Jon', 'Nah', 'Hab',
            'Zep', 'Hag', 'Zec', 'Mal', 'Isa', 'Jer', 'Bar', 'Lam', 'Epj', 'Eze', 'Sus', 'Sut', 'Dan', 'Dat', 'Bel',
            'Bet'
        ]

    @property
    def book_names(self) -> List[str]:
        return [
            'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua (A)', 'Joshua', 'Judges (A)', 'Judges',
            'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', '1 Esdras', 'Ezra',
            'Nehemiah', 'Esther', 'Judith', 'Tobit', 'Tobit (S)', '1 Maccabees', '2 Maccabees', '3 Maccabees',
            '4 Maccabees', 'Psalm', 'Odes', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Job', 'Wisdom',
            'Sirach Prolog', 'Sirach', 'Psalms of Solomon', 'Hosea', 'Amos', 'Micah', 'Joel', 'Obadiah', 'Jonah',
            'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Isaiah', 'Jeremiah', 'Baruch',
            'Lamentations', 'Epistle of Jeremiah', 'Ezekiel', 'Susanna', 'Susanna (TH)', 'Daniel', 'Daniel (TH)', 'Bel',
            'Bel (TH)'
        ]

    def __init__(self, filepath: str, lexeme: bool = False, include_punctuation: bool = False):
        """Initialize the scanner with a path to bgm.txt file."""
        self._book_map = dict(zip(self.book_abbr, self.book_names))
        self.filepath = Path(filepath)
        if not self.filepath.is_dir():
            raise FileNotFoundError(f"Directory not found: {filepath}")
        self._lexeme = lexeme
        self.include_punctuation = include_punctuation

    @property
    def bookMap(self) -> Dict[str, str]:
        return self._book_map

    def parse_reference(self, ref: str) -> tuple:
        """
        Extract Book, Chapter, and Verse from a BGM line.

        Expected format: BGM Book Chapter:Verse lexeme@morpheme lexeme@morpheme ...
        Handles book names with suffixes like "Judges (A)" or multi-word book names like "1 John"

        Args:
            line: A single line from the bgm.txt file

        Returns:
            Tuple of (book: str, chapter: int, verse: int)
            Examples:
                ("Genesis", 7, 3)
                ("Judges (A)", 16, 6)
                ("1 John", 1, 1)
        """
        parts = ref.split(' ')
        # Everything between "BGM" and chapter:verse is the book name
        book = parts[0]

        # Extract chapter and verse
        chapter_verse = parts[1].split(':')
        chapter = int(chapter_verse[0])
        if chapter_verse[1][-1].isalpha():
            sub_verse = ord(chapter_verse[1][-1]) - 96
            verse = int(chapter_verse[1][:-1]) if len(chapter_verse) > 1 else 0
        else:
            sub_verse = 0
            verse = int(chapter_verse[1]) if len(chapter_verse) > 1 else 0

        return (self.bookMap.get(book, book), chapter, verse, sub_verse)

    def iter(self):
        """
        Extract Matthew lexemes from OpenGNT corpus.
        """
        for abbr, book in self._book_map.items():
            for chapter in range(1, CHAPTER_COUNT[abbr] + 1):
                for token in self.token_iter(NocrTraverser(self.filepath, abbr, chapter)):
                    yield token


    def token_iter(self, traverser: NocrTraverser):
        ref = ('', 0, 0, 0)
        token_cnt = 0
        for token in traverser.traverse():
            if token[0] == 5:
                ref = self.parse_reference(token[1])
                token_cnt = 0
            elif token[0] == 2 and self.include_punctuation:
                pass
            elif token[0] == 0:
                token_cnt += 1
                word = token[1]
                yield WideToken(
                    str(ref[0]), int(ref[1]), int(ref[2]), int(ref[3]), token_cnt, word,
                    None, GreekWord.glyphen(word)
                )
            else:
                pass