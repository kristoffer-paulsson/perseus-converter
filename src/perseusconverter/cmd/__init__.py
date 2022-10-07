#
# Copyright (c) 2021 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""The CMD (command) package stores all executable commands of the BibleAnalyzer.
The init also contains the Command baseclass."""
import importlib
import logging
from argparse import Namespace
from collections import ChainMap
from pathlib import Path

from perseusconverter.app.config import Config
from perseusconverter.app.logging import Logger
from perseusconverter.data import NAME, VERSION


class Command:
    SUCCESS = 0
    FAIL = 0

    logger = None

    def __init__(self, config: Config, args: Namespace):
        self.logger.info("Running command: {}".format(self.__class__.__name__))
        self.logger.info("using parameters: {}.".format(args))

        self._args = args
        self._runtime(config)
        self._validate(config)
        self._config = config

    @classmethod
    def execute(cls, args: Namespace) -> int:
        status = cls.SUCCESS
        config = Config()

        if args.destination:
            config.update({"corpus": Path(args.destination).absolute()})
        if args.source:
            config.update({"data": Path(args.source).absolute()})

        # if args.debug:
        #    config.update({"level": logging.DEBUG})
        cls.logger = Logger.create(config, args.command)

        try:
            klass = getattr(
                importlib.import_module("perseusconverter.cmd.{}".format(args.command)),
                "{}Command".format(args.command.capitalize())
            )

            cmd = klass(config, args)
            cmd()
        except Exception as e:
            status = cls.FAIL
            cls.logger.critical("There was a bug in {} {}.".format(NAME, VERSION), exc_info=e)
            print("\033[0;31mSomething went wrong.\033[0;0m See the logs for additional information.")
        else:
            msg = "Done running command [{}].".format(args.command)
            cls.logger.info(msg)
            print(f"{msg} Errors: {cmd.logger.errors}, warnings: {cmd.logger.warnings}.")

        return status

    def _validate(self, config: ChainMap):
        if not config.get("corpus").is_dir():
            raise RuntimeError("Corpus directory not found, {}".format(config.get("corpus")))

    def _runtime(self, config: ChainMap):
        self.logger.info("-" * 10 + " Runtime information " + "-" * 10)
        self.logger.info("Log level: {}".format(logging.getLevelName(self.logger.getEffectiveLevel())))
        self.logger.info("Corpus directory: {}".format(config.get("corpus")))
        self.logger.info("-" * 10 + " Runtime information " + "-" * 10)

    def __call__(self):
        raise NotImplementedError()


__all__ = [
    "Command"
]
