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
import re


class RSGNTScanner(Scanner):
    """Scanner for the Rock-Solid GNT corpus (rock-solid-gnt.txt).

    This scanner follows the same concept as `BGTScanner` but is tolerant to a
    few reference formats found in rock-solid-gnt.txt. It attempts to detect
    references in the following ways (in order):
      - OpenGNT-style markers: 〔40｜1｜1〕 or similar
      - A token containing chapter:verse (e.g. "1:1") with a preceding book name
      - A book-abbreviation followed by chapter:verse

    It exposes `include_punctuation` to control whether tokens should retain
    surrounding punctuation.
    """

    # Map of book abbreviations (same ordering as other scanners) to support
    # abbreviated references in the rock-solid file.
    @property
    def book_abbr(self) -> List[str]:
        return [
            'Mt', 'Mk', 'Lk', 'Jn', 'Ac', 'Ro', '1Co', '2Co', 'Ga', 'Eph', 'Php', 'Col', '1Th', '2Th', '1Ti', '2Ti',
            'Tit', 'Phm', 'Heb', 'Jas', '1Pe', '2Pe', '1Jn', '2Jn', '3Jn', 'Jud', 'Re'
        ]

    @property
    def book_names(self) -> List[str]:
        return list({
            40: 'Matthew', 41: 'Mark', 42: 'Luke', 43: 'John', 44: 'Acts', 45: 'Romans', 46: '1 Corinthians',
            47: '2 Corinthians', 48: 'Galatians', 49: 'Ephesians', 50: 'Philippians', 51: 'Colossians',
            52: '1 Thessalonians', 53: '2 Thessalonians', 54: '1 Timothy', 55: '2 Timothy', 56: 'Titus',
            57: 'Philemon', 58: 'Hebrews', 59: 'James', 60: '1 Peter', 61: '2 Peter', 62: '1 John', 63: '2 John',
            64: '3 John', 65: 'Jude', 66: 'Revelation'
        }.values())

    @property
    def bookMap(self) -> Dict[str, str]:
        # Align with other scanners: book_abbr indices correspond to many books; slice used elsewhere
        return dict(zip(self.book_abbr, self.book_names))

    def __init__(self, filepath: str, include_punctuation: bool = False):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        self.include_punctuation = include_punctuation

    def iter(self):
        book = ''
        chapter = 0
        verse = 0
        token_index = 0

        f = self.filepath.open()
        for line in f:
            for part in line.strip().split(' '):
                if part.isnumeric():
                    num = int(part)
                    if num != verse:
                        verse = num
                        token_index = 0
                    else:
                        raise RuntimeError(f"Verse {verse} appears several times")
                elif part.isalnum() and part.isascii():
                    if book != part:
                        book = self.bookMap.get(part, part)
                elif ':' in part:
                    cv_parts = part.split(':')
                    if len(cv_parts) == 2 and cv_parts[0].isnumeric() and cv_parts[1].isnumeric():
                        chapter = int(cv_parts[0])
                        verse = int(cv_parts[1])
                        token_index = 0
                    else:
                        raise RuntimeError(f"Invalid chapter:verse format: {part}")
                else:
                    token_str = part if self.include_punctuation else re.sub(r'^\W+|\W+$', '', part)
                    # token_str = unicodedata.normalize('NFD', token_str)
                    token_index += 1
                    # print(f"Yielding token: {book} {chapter}:{verse} [{token_index}] '{token_str}'")
                    yield Token(book, chapter, verse, token_index, token_str)
