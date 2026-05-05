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
import unicodedata
from pathlib import Path
from typing import NamedTuple, List

from greektextify.text.word import GreekWord


class Reference(NamedTuple):
    book: str
    chapter: int
    verse: int


class Token(NamedTuple):
    """Represents a single word token."""
    book: str
    chapter: int
    verse: int
    index: int
    token: str
    # word: GreekWord
    # lexeme: GreekWord


class Scanner:
    """Scanner for Lexemes corpus files."""

    def iter(self):
        """Extract Matthew lexemes from Lexemes corpus."""
        # Placeholder for actual implementation
        # This should read the Lexemes corpus file and yield Token instances
        pass


class ScanIter:

    def __init__(self, scanner: Scanner, startRef: Reference = None):
        """Initialize the scanner with a path to bgm.txt file."""
        self.scanner = scanner
        self.startRef = startRef

    def __iter__(self):
        return self.scan_from()

    def scan_from(self):
        """Scan from a specific reference."""
        skip = False if self.startRef is None else True
        for token in self.scanner.iter():
            if self.startRef is not None:
                if token.book == self.startRef.book and token.chapter == self.startRef.chapter and token.verse == self.startRef.verse:
                    skip = False
            if not skip:
                yield token

    def token_printer(self):
        for token in self.scanner.iter():
            print(token)