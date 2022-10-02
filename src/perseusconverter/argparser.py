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
from argparse import ArgumentParser, Namespace


class CLI:

    def __init__(self):
        self._parser = ArgumentParser(description="Perseus Converter, for converting Koine Greek Material from the Perseus Digital Library")
        self._parser.add_argument("-d", "--debug", action="store_true", default=False,
                                  help="Print debug messages in the log file.")
        parsers = self._parser.add_subparsers(
            title="Commands",
            description="Operations on how to import and convert data from the Perseus project.",
            dest="command",
            help="",
        )
        self._import(parsers)
    @classmethod
    def parse_args(cls) -> Namespace:
        return cls()._parser.parse_args()

    def _import(self, subparser):
        imp = subparser.add_parser(name="import", help="Imports the Persues text data.")
