#
# Copyright (c) 2023 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Contextual description and error reporting of tokenization and other operations."""
import unicodedata
from abc import ABCMeta, abstractmethod
import contextlib
from contextvars import ContextVar
from typing import Tuple, List
from logging import Logger

from greektextify.nlp.debug import Debugger

nlp_ctx = ContextVar("nlp", default=None)


class ContextObject(metaclass=ABCMeta):
    __err: list

    def __init__(self):
        self.__err = list()

    @property
    def err(self) -> List:
        return self.__err

    @abstractmethod
    def location(self) -> Tuple:
        return NotImplemented


class NlpWarning(UserWarning):
    """Warning about a problem while processing an NLP operation."""
    TOKENIZE_ERROR = ("Failed to tokenize", 100)
    NON_GREEK_GLYPH = ("Not a greek glyph", 101)

    code: int
    info: dict

    def __init__(self, msg: str, code: int, info: dict):
        super(UserWarning, self).__init__(msg)
        self.code = code
        self.info = info


class NlpOperation(contextlib.ContextDecorator):
    """Use as decorator for context functions to catch results from."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return False

        context = nlp_ctx.get()
        if isinstance(context, ContextObject) and isinstance(exc_type, type(NlpWarning)):
            context.err.append((exc_val, "_".join(list(context.location()))))
            return True

        return False


class NlpContext(contextlib.AbstractContextManager):
    """Context describing the current position of a process in an operation."""

    def __init__(self, context: ContextObject, logger: Logger = None):
        self.__logger = logger
        self.__token = nlp_ctx.set(context)

    def __analyze(self, context: ContextObject):
        for err, loc in context.err:

            print("\n{}, {}".format(err, loc))
            if err.code == NlpWarning.TOKENIZE_ERROR[1]:
                debug_glyph(err.info.get("line"), err.info.get("pos"))
            elif err.code == NlpWarning.NON_GREEK_GLYPH[1]:
                debug_glyph(err.info.get("char"))

            if self.__logger:
                self.__logger.error("Nlp error {} '{}', info: {}".format(err.code, err, err.info))

    def __enter__(self):
        return nlp_ctx.get()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise exc_type

        context = nlp_ctx.get()
        self.__analyze(context)
        nlp_ctx.reset(self.__token)

        return None


def debug_glyph(text: str, pos: int = None):
    if pos is None:
        pos = 0
        noprint = True
    else:
        noprint = False

    start = max(0, pos-19)
    end = min(len(text)-1, pos+19)
    cur = pos - start
    debug = Debugger.glyph(text[start:end])

    if noprint:
        print("Issue in, w/o specific position '{}'".format(text))
    else:
        print("At position {} with {}\nIssue in '{}'".format(pos, unicodedata.name(text[pos]), text))

    for index in range(0, end-start):
        if index != cur or noprint:
            print(debug[index])
        else:
            print("\u001b[33m" + debug[index] + "\u001b[0m")
