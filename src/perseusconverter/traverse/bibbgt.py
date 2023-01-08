#
# Copyright (c) 2023 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Plain text BGT traverser."""
from pathlib import PurePath
from regex import regex

from greektextify.text.standardize import Standardize
from perseusconverter.traverse.plain import AbstractPlainTraverser


class BgtTraverser(AbstractPlainTraverser):

    def __init__(self, path: PurePath):
        AbstractPlainTraverser.__init__(self, path)
        self._hierarchy = 'book-chapter-verse'
        self._book = None
        self._chapter = None
        self._verse = None

    def _traverse(self, line: str):
        self._book, self._chapter, self._verse, text = regex.search(r"(.*) (\d+):(\d+)?(.*)$", line.strip()).groups()
        std = Standardize.pdl(text.strip())
        self.general(std)
