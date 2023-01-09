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
"""Data used in the application for several reasons."""
from pathlib import PosixPath


class RecursiveIterator:
    """Iterator for the PDL using the canonical-greekLit.tracking.json"""
    def __init__(self, data_path: PosixPath):
        self.path = data_path

    def __iter__(self):
        for resource in self._iter_folder(self.path):
            yield resource

    def _iter_folder(self, path: PosixPath):
        for x in path.iterdir():
            if x.is_dir():
                for y in self._iter_folder(x):
                    yield y
            else:
                yield x

            #elif "grc" in x.name and x.suffix == ".xml":
            #    yield x
