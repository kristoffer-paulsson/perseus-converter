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
"""Configuring a logger for Perseus Converter for search and debugging errors."""
import datetime
import logging
from pathlib import Path

from perseusconverter.config import Config


class Logger(logging.Logger):
    _config = Config({})

    def __init__(self, name):
        self._warn_cnt = 0
        self._err_cnt = 0

        self.manager.setLoggerClass(self.__class__)
        logging.Logger.__init__(self, name, self._config.get("level"))
        handler = logging.FileHandler(
            filename=self._config.get("logs").joinpath(
                "{}.log".format(datetime.datetime.utcnow().strftime("%Y-%m-%d_%H%M%S"))),
            encoding="utf-8"
        )
        handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
        self.addHandler(handler)

    @property
    def warnings(self) -> int:
        return self._warn_cnt

    @property
    def errors(self) -> int:
        return self._err_cnt

    def warning(self, msg, *args, **kwargs):
        self._warn_cnt += 1
        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._err_cnt += 1
        self.log(logging.ERROR, msg, *args, **kwargs)

    @classmethod
    def file_format(cls, msg: str, path: Path, line: int, token: str = "here") -> str:
        return "{}:\n  File \"{}\", line {}, in {}".format(msg, path, line, token)

    @classmethod
    def create(cls, config, command):
        if not config.get("logs").is_dir():
            raise RuntimeError("Log directory not found, {}".format(config.get("logs")))

        cls._config = config
        return cls(command)
