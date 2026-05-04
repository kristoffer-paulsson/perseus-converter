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
import unicodedata, csv

from biblebuilder.scan.bgt import BGTScanner
from biblebuilder.scan.scanner import Reference, ScanIter


class CorpusGenerator:
    pass

    def generate(self):
        pass


class BGTCorpusGenerator(CorpusGenerator):

    def __init__(self, bgtScanner: BGTScanner, start: Reference):
        """Initialize the comparator with scanners for both corpora."""
        self.bgtScanner = ScanIter(bgtScanner, start)
        self.errors = dict()

    def generate(self):
        with open('bgt_nt_corpus.csv', 'w', newline='\n', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['book', 'chapter', 'verse', 'index', 'token'])
            for token in self.bgtScanner:
                writer.writerow([token.book, token.chapter, token.verse, token.index, unicodedata.normalize('NFD', token.token)])
