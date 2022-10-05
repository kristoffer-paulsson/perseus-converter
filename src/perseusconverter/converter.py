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
import html
import re
import textwrap
import unicodedata
from pathlib import PosixPath
from typing import Tuple


from betacode.conv import beta_to_uni
from bs4 import BeautifulSoup
from slugify import slugify


class Converter:
    LANG_GREEK = """Greek"""
    LANG_LATIN = """Latin"""

    def __init__(self, file: PosixPath, nodes: Tuple = ()):
        self.file = file
        self.xml = None
        self.nodes = nodes

    def get_lxml(self) -> BeautifulSoup:
        if self.xml is None:
            with open(self.file) as text:
                # Classics/Plutarch/opensource/plut.lyc_gk.xml
                # Classics/Plutarch/opensource/plut.num_gk.xml
                # Classics/Plutarch/opensource/plut.pyrrh_gk.xml
                # Classics/Plutarch/opensource/plut.mar_gk.xml
                # text = str(text).replace("type=\"sork\"", "type=\"work\"")
                self.xml = BeautifulSoup(text, "lxml")
        return self.xml

    def get_filename(self) -> str:
        xml = self.get_lxml()
        title = xml.find("title", attrs={"type": "work"})
        if title is not None:
            title = title.text
        else:
            title = xml.title.text.replace("(Greek)", "").split(".")[0].strip()

        author = xml.author
        if author:
            author = author.getText().strip()

        return slugify(str(author)) + "_" + slugify(str(title))

    def is_koine(self) -> bool:
        try:
            return self.get_lxml().language.getText().strip().title() == self.LANG_GREEK
        except AttributeError:
            return False

    def is_latin(self) -> bool:
        try:
            return self.get_lxml().language.getText().strip().title() == self.LANG_LATIN
        except AttributeError:
            return False

    def remove_nodes(self):
        xml = self.get_lxml()
        for node in self.nodes:
            for element in self.get_lxml().select(node):
                element.extract()

    def export(self, path: PosixPath, name: str, koine: bool = False):
        with open(path.joinpath(name), "x+") as corpus:
            self.remove_nodes()
            text = self.get_lxml().find("text").getText()
            text = html.unescape(text)
            if koine:
                text = beta_to_uni(text)
            text = re.sub("\W+", " ", text).strip()
            text = unicodedata.normalize("NFD", text)
            column = ""
            for line in text.splitlines():
                for token in line.split(" "):
                    vacuumed = token.strip(" ")
                    if vacuumed:
                        column += vacuumed + " "
            corpus.write(textwrap.fill(text, break_long_words=False, break_on_hyphens=False, expand_tabs=False))
