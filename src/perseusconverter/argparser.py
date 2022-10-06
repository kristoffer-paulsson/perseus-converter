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
        self._parser = ArgumentParser(description="Use to convert the Perseus Digital Library into nltk corpora.")
        self._parser.add_argument("-d", "--debug", action="store_true", default=False,
                                  help="Print debug messages in the log file.")
        parsers = self._parser.add_subparsers(
            title="Commands",
            description="Extracting a corpus from Perseus for NLP use with nltk.",
            dest="command",
            help="Use koine or latin for corpora.",
        )
        self._koine(parsers)
        self._latin(parsers)

    @classmethod
    def parse_args(cls) -> Namespace:
        return cls()._parser.parse_args()

    def _koine(self, subparser):
        load = subparser.add_parser(name="koine", help="Imports the corpora and caches them as \"parsings.\"")
        load.add_argument("format", choices=["text", "markdown"], help="Which corpora to load.")
        load.add_argument("-v", "--verify", action="store_true", default=False, help="Verify output against source.")

    def _latin(self, subparser):
        line = subparser.add_parser(name="latin", help="Lines up the corpora \"parsings\" into \"linear\" for analysis.")
        line.add_argument("corpus", choices=["text", "markdown"], help="Which parsings to process.")
        line.add_argument("-v", "--verify", action="store_true", default=False, help="Verify output against source.")
