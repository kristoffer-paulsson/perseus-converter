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
from typing import Tuple

from greektextify.nlp.contextual import ContextObject, NlpOperation, NlpContext
from greektextify.nlp.detoken import Tokenizer
from greektextify.text.standardizer import TokenStandardizerMixin
from perseusconverter.util.books import NEW_ABBR
from perseusconverter.util.utils import BRef


class OpenUtfStandard(TokenStandardizerMixin):
    PILCROW_SIGN = ord('\u00B6')
    NOT_SIGN = ord('\u00AC')

    TRANSFORM = {
        PILCROW_SIGN: '',
        NOT_SIGN: '',
    }

    @classmethod
    def standardize(cls, text: str) -> str:
        return text.translate(cls.TRANSFORM)  # Translates the rest


class IterOpenGNT(ContextObject):

    def __init__(self, reader):
        super().__init__()
        self._reader = reader
        self._tokenizer = Tokenizer.utf_tokenizer(OpenUtfStandard())
        self._current = 'n/a'

    def __iter__(self):
        return self.iter()

    def location(self) -> Tuple[str, ...]:
        return str(self._current), ''

    def iter_verse(self):
        pass

    def iter_sub(self):
        pass

    @NlpOperation()
    def _tokenize(self, text) -> list:
        text = self._tokenizer.standardize(text)
        return self._tokenizer.tokenize(text)

    def iter(self):
        last_verse = 0
        current_index = 0
        v_text = None
        row_idx = 1

        next(self._reader)

        for row in self._reader:
            with NlpContext(self):
                book_idx, chapter_num, verse_num = row[6].strip('〔〕').split('｜')
                book_abbr = NEW_ABBR[int(book_idx) - 40]
                chapter_cnt = int(chapter_num)
                verse_cnt = int(verse_num)
                if verse_cnt != last_verse:
                    if v_text is not None:
                        for token in self._tokenize(v_text):
                            yield token
                    v_text = ''

                    current_index = 1
                    last_verse = verse_cnt
                    bref = BRef(book_abbr, chapter_cnt, verse_cnt, -1)
                    self._current = str(bref)
                    yield bref
                else:
                    current_index += 1

                row_idx += 1
                self._current += " row :{}".format(row_idx)

                word = ' ' + row[7].strip('〔〕').split('｜')[2]
                punctuation = ''.join(row[11].strip('〔〕').split('｜')).replace('<pm>', '').replace('</pm>', '')
                v_text += word + punctuation
