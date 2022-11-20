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

    GIT = "https://github.com/PerseusDL/canonical-greekLit.git"

    def __init__(self, config: Config, args: Namespace):
        Command.__init__(self, config, args)
        self.target = self._config.get("data").joinpath("canonical-greekLit")

    def __call__(self):
        if self.target.is_dir():
            self.logger.info("Perseus Digital Library found")
            self.upgrade()
        else:
            self.logger.info("Perseus Digital Library NOT found")
            self.clone()

    def clone(self):
        self.logger.info("Start cloning PDT from {} to {}".format(self.GIT, self.target))
        git.Git(self._config.get("data")).clone(self.GIT)
        self.logger.info("Done cloning PDT from {}".format(self.GIT))

    def upgrade(self):
        self.logger.info("Start upgrading PDT from {}".format(self.GIT))
        origin = git.Repo(self.target).remotes.origin
        origin.pull()
        self.logger.info("Done upgrading PDT from {}".format(self.GIT))
