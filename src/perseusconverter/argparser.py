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
        self._parser = ArgumentParser(description="Use to convert the Perseus Digital Library into nlp corpora.")
        self._parser.add_argument("-d", "--destination", default="",
                                  help="Path to the parent folder of the koine/latin corpora.")
        self._parser.add_argument("-s", "--source", default="",
                                  help="Path to the parent folder of the Perseus ./Classics/* folder.")
        parsers = self._parser.add_subparsers(
            title="Commands",
            description="Extracting a corpus from Perseus for NLP use with nlp.",
            dest="command",
            help="Use koine or latin for corpora.",
        )
        self._download(parsers)
        self._koine(parsers)

    @classmethod
    def parse_args(cls) -> Namespace:
        return cls()._parser.parse_args()

    def _download(self, subparser):
        load = subparser.add_parser(name="download", help="Downloads and updates the latest corpora")
        load.add_argument('corpora', choices=['pdl', 'bib', 'lex'])

    def _koine(self, subparser):
        koine = subparser.add_parser(name="koine", help="Imports the corpora and caches them as \"parsings.\"")
        koine.add_argument('corpora', choices=['pdl', 'bib', 'lex'])
