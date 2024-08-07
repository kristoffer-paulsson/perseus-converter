#
# Copyright (c) 2024 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Printing grammar targeting among others Latex."""
from pathlib import PosixPath
from typing import Tuple, List

from greekparsify.inflect import Inflect
from greektextify.text.glyph import GreekGlyph
from greektextify.text.prnt import PrintGreek


class PrintGrammar(PrintGreek):

    def location(self) -> PosixPath:
        return PosixPath(__file__).parent.joinpath('src')

    def load_tmpl(self, text: str) -> str:
        base = self.location()
        print(base)
        begin_tmpl = base.joinpath('start.tex.tmpl').read_text()
        end_tmpl = base.joinpath('end.tex.tmpl').read_text()
        return begin_tmpl + text + end_tmpl

    def save_tex(self, text: str, name: str):
        base = self.location()
        base.joinpath(name + '.tex').write_text(text)

    @classmethod
    def tex_grc(cls, word: Tuple[GreekGlyph]) -> str:
        return "\\grc{{{0}}}".format(cls.format(word))

    @classmethod
    def tex_token_list(cls, tokens: List[Tuple[int, ...]]) -> str:
        tex = ''
        for idx, data in enumerate(tokens):
            if data[0] == 0:
                tt, token, inf = data
                wrd_tex = cls.tex_grc(token)
                inf_tex = ' '.join(["\\tsc{{{0}}}".format(i.capitalize()) for i in Inflect.tex_format_inf(inf)])
                tex += " \\gunderset{{\\scriptsize{{{0}}} }}{{{1}}}".format(str(inf_tex), wrd_tex)
            elif data[0] == 2:
                tt, token = data
                tex += token
        tex += ' \\\\ \\medskip'
        return tex