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
"""Module containing the DOWNLOAD command class."""
from argparse import Namespace

import git

from . import Command
from ..app import Config


class DownloadCommand(Command):

    GIT = {
        'pdl': ("Perseus Digital Library", "https://github.com/PerseusDL/canonical-greekLit.git", "canonical-greekLit"),
        'bib': ("Bib", "https://github.com/kristoffer-paulsson/bible-analyzer-corpora.git", "bible-analyzer-corpora"),
    }

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data").joinpath(self.GIT[self._args.corpora][2])

    def __call__(self):
        if self.target.is_dir():
            self.logger.info("{} found".format(self.GIT[self._args.corpora][0]))
            self.upgrade()
        else:
            self.logger.info("{} NOT found".format(self.GIT[self._args.corpora][0]))
            self.clone()

    def clone(self):
        self.logger.info("Start cloning {} from {} to {}".format(
            self.GIT[self._args.corpora][0],
            self.GIT[self._args.corpora][1],
            self.target))
        git.Git(self._config.get("data")).clone(self.GIT[self._args.corpora][1])
        self.logger.info("Done cloning {} from {}".format(
            self.GIT[self._args.corpora][0],
            self.GIT[self._args.corpora][1],
        ))

    def upgrade(self):
        self.logger.info("Start upgrading {} from {}".format(
            self.GIT[self._args.corpora][0],
            self.GIT[self._args.corpora][1]
        ))
        origin = git.Repo(self.target).remotes.origin
        origin.pull()
        self.logger.info("Done upgrading {} from {}".format(
            self.GIT[self._args.corpora][0],
            self.GIT[self._args.corpora][1]
        ))
