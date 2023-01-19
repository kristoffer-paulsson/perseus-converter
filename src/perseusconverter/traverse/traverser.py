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
"""Abstract traverser."""
from abc import ABCMeta, abstractmethod
from pathlib import PurePath
from typing import Tuple

from greektextify.text.token import Tokenize


class AbstractTraverser(metaclass=ABCMeta):

    def __init__(self, tokenizer: Tokenize, path: PurePath):
        self._hierarchy = None
        self._tokenizer = tokenizer
        self._filename = path

    @abstractmethod
    def hierarchy(self):
        return NotImplemented

    @property
    def filename(self) -> str:
        return str(self._filename)

    # @abstractmethod
    # def location(self) -> Tuple:
    #     return NotImplemented

    @abstractmethod
    def traverse(self):
        return NotImplemented

    @abstractmethod
    def general(self):
        return NotImplemented

