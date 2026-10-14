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

from greektextify.text.word import GreekWord
from perseusconverter.recursiveiterator import RecursiveIterator
from perseusconverter.traverse.bibvt import VetusTraverser
from .scanner import Scanner, WideToken
from pathlib import Path


VETUSJG = {
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


class JGVTScanner(Scanner):

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
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
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

        files = [filename for filename in RecursiveIterator(self.target.joinpath("bible-analyzer-corpora/corpora/septuagint3/"))]

        book_order = dict()
        num_order = dict()
        for filename in sorted(files, key=lambda x: int(x.stem.split('-')[2])):
            parts = filename.stem.split('-')
            book = parts[0]
            chapter = int(parts[1])
            if book not in book_order:
                book_order[book] = dict()
            book_order[book][chapter] = filename
            num_order[int(parts[2])] = filename

        ref = ('', 0, 0, 0)
        token_cnt = 0
        for key, data in VETUSJG.items():
            if data[0]:
                for chapter, filename in book_order[data[1]].items():
                    for token in VetusTraverser(filename, key, chapter).traverse():
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
            else:
                chapter_cnt = 0
                for num in range(int(data[2]), int(data[3] + 1)):
                    chapter_cnt += 1
                    for token in VetusTraverser(num_order[num], key, chapter_cnt).traverse():
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