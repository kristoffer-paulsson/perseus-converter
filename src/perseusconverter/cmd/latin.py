#
# Copyright (c) 2022 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Module containing the LOAD command class."""
from pathlib import PosixPath

from . import Command
from ..converter import Converter
from ..scanner import Scanner


class LatinCommand(Command):
    ALPHABET = ["", "_b", "_c", "_d", "_e", "_f", "_g", "_h", "_i", "_j", "_k", "_l", "_m", "_n", "_o", "_p", "_q", "_r", "_s", "_t", "_u", "_v", "_x", "_y", "_z"]
    NAMES = set()

    def __call__(self):
        self._config.get("corpus").joinpath("latin").mkdir(exist_ok=True)
        Scanner(self._config.get("data")).scan(self.dealer)

    def dealer(self, file: PosixPath):
        data = Converter(file, self._config.get("remove"))
        if data.is_latin():
            self.logger.info("Start converting: {}".format(data.file))
            self.logger.info("Export: {}".format(
                data.export(
                    self._config.get("corpus").joinpath("latin"),
                    self.calc_name(data.get_filename()) + ".txt",
                    False
                )
            ))

    def calc_name(self, name: str) -> str:
        num = 0
        while name + self.ALPHABET[num] in self.NAMES:
            num += 1

        self.NAMES.add(name + self.ALPHABET[num])
        return name + self.ALPHABET[num]
