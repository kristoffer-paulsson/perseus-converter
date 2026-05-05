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
from typing import List, Dict

from .scanner import Scanner, Token
from pathlib import Path
import string


class BGTScanner(Scanner):
    """Scanner for Bibleworks Greek Text corpus files."""

    @property
    def book_abbr(self) -> List[str]:
        return [
            'Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jsa', 'Jos', 'Jda', 'Jdg', 'Rut', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch',
            '2Ch', '1Es', 'Ezr', 'Neh', 'Est', 'Jdt', 'Tob', 'Tbs', '1Ma', '2Ma', '3Ma', '4Ma', 'Psa', 'Ode', 'Pro',
            'Ecc', 'Sol', 'Job', 'Wis', 'Sip', 'Sir', 'Pss', 'Hos', 'Amo', 'Mic', 'Joe', 'Oba', 'Jon', 'Nah', 'Hab',
            'Zep', 'Hag', 'Zec', 'Mal', 'Isa', 'Jer', 'Bar', 'Lam', 'Epj', 'Eze', 'Sus', 'Sut', 'Dan', 'Dat', 'Bel',
            'Bet', 'Mat', 'Mar', 'Luk', 'Joh', 'Act', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Phi', 'Col', '1Th', '2Th',
            '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jam', '1Pe', '2Pe', '1Jo', '2Jo', '3Jo', 'Jud', 'Rev'
        ]

    @property
    def book_names(self) -> List[str]:
        return {
            40: 'Matthew', 41: 'Mark', 42: 'Luke', 43: 'John', 44: 'Acts', 45: 'Romans', 46: '1 Corinthians',
            47: '2 Corinthians', 48: 'Galatians', 49: 'Ephesians', 50: 'Philippians', 51: 'Colossians',
            52: '1 Thessalonians', 53: '2 Thessalonians', 54: '1 Timothy', 55: '2 Timothy', 56: 'Titus',
            57: 'Philemon', 58: 'Hebrews', 59: 'James', 60: '1 Peter', 61: '2 Peter', 62: '1 John', 63: '2 John',
            64: '3 John', 65: 'Jude', 66: 'Revelation'
        }.values()

    @property
    def bookMap(self) -> Dict[str, str]:
        return dict(zip(self.book_abbr[61:88], self.book_names))

    def __init__(self, filepath: str, include_punctuation: bool = False):
        """Initialize the scanner with a path to bgt.txt file.

        Args:
            filepath: Path to the bgt.txt file
            include_punctuation: If True, include punctuation marks as tokens.
                                If False, strip punctuation from tokens.
        """
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        self.include_punctuation = include_punctuation

    def parse_reference(self, line: str) -> tuple:
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
        line = line.strip()
        if not line:
            return None

        parts = line.split()
        #print("Parsing line:", line)

        # Skip "BGM" prefix at parts[0]
        # Find the chapter:verse part (contains ':' and is numeric)
        chapter_verse_idx = None
        for i in range(0, len(parts)):
            if ':' in parts[i]:
                # Check if it matches Chapter:Verse pattern
                cv_parts = parts[i].split(':')
                if len(cv_parts) == 2:
                    try:
                        int(cv_parts[0])
                        int(cv_parts[1])
                        chapter_verse_idx = i
                        break
                    except ValueError:
                        continue

        if chapter_verse_idx is None:
            return None

        # Everything between "BGM" and chapter:verse is the book name
        book = ' '.join(parts[0:chapter_verse_idx])

        # Extract chapter and verse
        chapter_verse = parts[chapter_verse_idx].split(':')
        chapter = int(chapter_verse[0])
        verse = int(chapter_verse[1]) if len(chapter_verse) > 1 else 0

        return (self.bookMap.get(book, book), chapter, verse)

    def read_line(self, line: str) -> List[Token]:
        """
        Reads a single line from bgm.txt.
        """
        line = line.strip()
        if not line:
            return None

        reference = self.parse_reference(line)

        # Split the line into parts
        parts = line.split(str(reference[1]) + ":" + str(reference[2]))[1].strip().split(' ')
        # book = parts[1]
        # chapter_verse = parts[2].split(':')
        # chapter = int(chapter_verse[0])
        # verse = int(chapter_verse[1]) if len(chapter_verse) > 1 else 0

        # Extract and parse tokens
        tokens = []
        counter = 1
        for part in parts:
            word = part.strip(',.·;') if not self.include_punctuation else part
            if not word == '':
                tokens.append(Token(reference[0], reference[1], reference[2], counter,  word) )
                counter += 1

        return tokens

    def iter(self):
        f = self.filepath.open()
        for line in f:
            tokens = self.read_line(line)
            if tokens:
                for token in tokens:
                    yield token