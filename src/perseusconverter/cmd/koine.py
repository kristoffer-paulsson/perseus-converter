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
import unicodedata
from argparse import Namespace

from bs4 import BeautifulSoup

from . import Command
from ..app import Config
from ..metaiterator import MetaIterator


class KoineCommand(Command):

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data")

    def __call__(self):

        all = dict()

        for obj in MetaIterator(self.target):
            for filename in obj["grc"]:
                resource = self.target.joinpath(filename)
                if resource.is_file():
                    with open(resource) as tei:
                        xml = BeautifulSoup(tei, "xml")
                        for char in list(xml.body.text):
                            if char == ":":
                                if str(resource) in all.keys():
                                    all[str(resource)] += 1
                                else:
                                    all[str(resource)] = 1
                else:
                    self.logger.info("Registered but missing file: {}".format(resource))

        for key, value in all.items():
            print("{} number of ':' in file {}".format(value, key))
        # tokens = list(all)
        # tokens.sort()
        # print(tokens)


        # unicodedata.normalize("NFKD", xml.body.text)
