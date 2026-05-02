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
from .scanner import LexemeScanner, Token
from pathlib import Path

class BGMScanner(LexemeScanner):
    """Scanner for Byzantine Greek Morphology corpus files."""

    def __init__(self, filepath: str):
        """Initialize the scanner with a path to bgm.txt file."""
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

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

        # Skip "BGM" prefix at parts[0]
        # Find the chapter:verse part (contains ':' and is numeric)
        chapter_verse_idx = None
        for i in range(1, len(parts)):
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
        book = ' '.join(parts[1:chapter_verse_idx])

        # Extract chapter and verse
        chapter_verse = parts[chapter_verse_idx].split(':')
        chapter = int(chapter_verse[0])
        verse = int(chapter_verse[1]) if len(chapter_verse) > 1 else 0

        return (book, chapter, verse)

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
        #book = parts[1]
        #chapter_verse = parts[2].split(':')
        #chapter = int(chapter_verse[0])
        #verse = int(chapter_verse[1]) if len(chapter_verse) > 1 else 0

        # Extract and parse tokens
        tokens = []
        counter = 1
        for part in parts:
            if '@' in part:
                lexeme, morpheme = part.split('@', 1)
                tokens.append(Token(reference[0], reference[1], reference[2], counter, lexeme))
                counter += 1

        return tokens

    def iter(self):
        f = self.filepath.open()
        for line in f:
            tokens = self.read_line(line)
            if tokens:
                for token in tokens:
                    yield token