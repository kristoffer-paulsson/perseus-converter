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
from pathlib import PosixPath

from bs4 import BeautifulSoup, BeautifulStoneSoup
from slugify import slugify


class Converter:
    def __init__(self, file: PosixPath):
        self.file = file
        self.xml = None

    def get_lxml(self) -> BeautifulSoup:
        if self.xml is None:
            with open(self.file) as tei:
                self.xml = BeautifulSoup(tei, "lxml")
        return self.xml


class Classifier:
    LANG_GREEK = """Greek"""

    def classify_tei(self, tei: BeautifulSoup, lang: str) -> bool:
        return tei.language.getText().strip().title() == lang

    # Classics/Plutarch/opensource/plut.lyc_gk.xml
    # Classics/Plutarch/opensource/plut.num_gk.xml
    # Classics/Plutarch/opensource/plut.pyrrh_gk.xml
    # Classics/Plutarch/opensource/plut.mar_gk.xml
    def get_title(self, tei: BeautifulSoup) -> str:
        title = tei.find("title", attrs={"type": "work"})
        if title is not None:
            title = title.text
        else:
            title = tei.title.text.replace("(Greek)", "").split(".")[0].strip()
        # title = title.

        return title

    def get_author(self, tei: BeautifulSoup) -> str:
        author = tei.author
        if author:
            author = author.getText().strip()
        return author

    def filename(self, tei: BeautifulSoup) -> str:
        return slugify(str(self.get_author(tei))) + "_" + slugify(str(self.get_title(tei))) + ".txt"
