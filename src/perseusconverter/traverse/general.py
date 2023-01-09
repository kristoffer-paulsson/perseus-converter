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
"""General traverser without specific purpose."""
from typing import List, Tuple

from lxml.etree import Element

from greektextify.nlp.debug import Debugger
from greektextify.text.standardize import Standardize
from perseusconverter.traverse.xml import AbstractXmlTraverser


EXCEPTIONS = {
    'tlg7000.tlg001.perseus-grc5.xml': (
        '/TEI.2/text/body/div1[1]/div2[29]/label/title',
    ),
    'tlg0060.tlg001.perseus-grc3.xml': (
        '/TEI.2/text/body/div1[7]/argument/p[9]/title',
    ),
    'tlg0086.tlg035.perseus-grc1.xml': (
        '/TEI.2/text/body/div[114]/p/title'
    ),
    'tlg0086.tlg010.perseus-grc1.xml': (
        '/TEI.2/text/body/div[126]/p[1]/head'
    )
}


class GeneralTraverser(AbstractXmlTraverser):

    def __init__(self, path, ignore: Tuple[str]):
        AbstractXmlTraverser.__init__(self, path, ignore)
        self._states = set()

    def general(self, xml: Element, skip: bool):
        if not isinstance(xml.tag, str) or skip:
            return
        if self._do_skip(xml):
            if xml.text:
                self._tokenize(xml.tail, xml)
        else:
            self._tokenize(xml.text, xml)
            self._tokenize(xml.tail, xml)

    @property
    def states(self) -> set:
        return self._states

    def _tokenize(self, text: str, e: Element) -> List[str]:
        if text is not None:
            std = Standardize.pdl(text.strip())
            if std != '':
                try:
                    # print("TEXT", std)
                    # print(self._tokenizer.tokenize(std))
                    tokens = self._tokenizer.tokenize(std)
                    for token in tokens:
                        if token.startswith('\u1F50\u03C0\u03B1'):
                            print(1, tokens)
                            exit()
                        if '\u03C5\u03C0\u03B1' in token:
                            print(2, token, tokens)
                            exit()
                    # self._tokenizer.tokenize(std)
                except RuntimeWarning:
                    print(self._tree.getpath(e))
                    print("TEXT", std)
                    print("ORIG", text)
                    print('\n'.join(Debugger.glyph(std)))
                    exit()
