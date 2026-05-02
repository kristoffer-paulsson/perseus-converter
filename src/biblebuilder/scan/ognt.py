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

class OGNTScanner(LexemeScanner):

    def __init__(self, filepath: str):
        """Initialize the scanner with a path to bgm.txt file."""
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

    def iter(self):
        """
        Extract Matthew lexemes from OpenGNT corpus.
        """

        bookMap = {40: 'Matthew', 41: 'Mark', 42: 'Luke', 43: 'John', 44: 'Acts', 45: 'Romans', 46: '1 Corinthians',
                   47: '2 Corinthians', 48: 'Galatians', 49: 'Ephesians', 50: 'Philippians', 51: 'Colossians',
                   52: '1 Thessalonians', 53: '2 Thessalonians', 54: '1 Timothy', 55: '2 Timothy', 56: 'Titus',
                   57: 'Philemon', 58: 'Hebrews', 59: 'James', 60: '1 Peter', 61: '2 Peter', 62: '1 John', 63: '2 John',
                   64: '3 John', 65: 'Jude', 66: 'Revelation'
        }

        with open(self.filepath, 'r', encoding='utf-8') as f:
            # Skip header
            last_verse = 0
            current_index = 0
            next(f)

            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 8:
                    # Extract book/chapter/verse info: 〔40｜1｜1〕
                    book_info = parts[6].strip('〔〕')
                    book_parts = book_info.split('｜')
                    if len(book_parts) >= 3:
                        book_num = int(book_parts[0])
                        chapter = int(book_parts[1])
                        verse = int(book_parts[2])

                        book = bookMap[book_num]

                        if(verse != last_verse):
                            current_index = 1
                            last_verse = verse
                        else:
                            current_index += 1

                        # Extract lexeme from: 〔βιβλοϲ｜Βιβλος｜Βίβλος｜βίβλος｜N-NSF｜G976〕
                        lexeme_info = parts[7].strip('〔〕')
                        lexeme_parts = lexeme_info.split('｜')

                        yield Token(book, chapter, verse, current_index, lexeme_parts[3])  # Yielding raw data for debugging