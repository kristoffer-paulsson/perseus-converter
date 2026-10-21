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
from typing import Dict, Set, Tuple

from perseusconverter.util.utils import Counter, BRef


class Collector:

    def __init__(self, iterator):
        self._iterator = iterator
        self._bible = dict()
        self._sub_verses = list()
        self._missing = dict()

    def collect(self):
        chapter_cnt = Counter()
        verse_cnt = Counter()

        for bref in self._iterator:
            if isinstance(bref, BRef):
                if bref.book not in self._bible:
                    self._bible[bref.book] = dict()
                    chapter_cnt.reset()
                if chapter_cnt.current() < bref.chapter:
                    while bref.chapter - chapter_cnt.current() > 1:
                        chapter_cnt.increment()
                        self._add_missing(BRef(bref.book, chapter_cnt.current(), -1, -1))
                    chapter_cnt.increment()
                    if chapter_cnt.current() != bref.chapter:
                        raise RuntimeError("Chapter mismatch {} / {}".format(chapter_cnt.current(), bref.chapter))
                    verse_cnt.reset()
                if verse_cnt.current() < bref.verse and bref.sub == -1:
                    while bref.verse - verse_cnt.current() > 1:
                        verse_cnt.increment()
                        self._add_missing(BRef(bref.book, bref.chapter, verse_cnt.current(), -1))
                    if bref.chapter not in self._bible[bref.book]:
                        self._bible[bref.book][bref.chapter] = list()
                    self._bible[bref.book][bref.chapter].append(bref.verse)
                    verse_cnt.increment()
                if bref.sub != -1:
                    self._sub_verses.append(str(bref))

    def _add_missing(self, ref: BRef):
        if ref.book not in self._missing:
            self._missing[ref.book] = dict()
        if ref.chapter not in self._missing[ref.book]:
            self._missing[ref.book][ref.chapter] = list()
        if ref.verse not in self._missing[ref.book][ref.chapter]:
            self._missing[ref.book][ref.chapter].append(ref.verse)

    def analyze(self):
        bible = self._bible.copy()
        for book in bible.keys():
            for chapter in bible[book].keys():
                bible[book][chapter] = max(bible[book][chapter])

        print(list(bible.keys()))
        print(self._bible)
        print(self._sub_verses)
        print(self._missing)

    def _normalize(self) -> Dict[str, Dict[int, Set[int]]]:
        """book → chapter → set of verses.
        Accepts both the original list-of-verses form and the
        post-analyze integer-max form.
        """
        norm: Dict[str, Dict[int, Set[int]]] = {}
        for book, chapters in self._bible.items():
            norm[book] = {}
            for ch, verses in chapters.items():
                if isinstance(verses, (list, set, tuple)):
                    norm[book][ch] = set(verses)
                elif isinstance(verses, int):
                    # already reduced to max-verse
                    norm[book][ch] = {verses} if verses > 0 else set()
                else:
                    raise TypeError(
                        f"Unexpected type for {book} {ch}: {type(verses)}"
                    )
        return norm

    def difference(self, other: "Collector") -> Tuple[Dict[str, Dict[int, Set[int]]], Set[str]]:
        """
        Self − other: books → chapters → verses that exist in self but not in other.
        Same return shape as intersect().
        """
        a = self._normalize()
        b = other._normalize()
        result: Dict[str, Dict[int, Set[int]]] = {}

        # books only in self
        for book in a.keys() - b.keys():
            result[book] = {ch: set(verses) for ch, verses in a[book].items()}

        # common books
        for book in a.keys() & b.keys():
            result[book] = {}
            # chapters only in self
            for ch in a[book].keys() - b[book].keys():
                result[book][ch] = set(a[book][ch])
            # common chapters → verse difference
            for ch in a[book].keys() & b[book].keys():
                diff_verses = a[book][ch] - b[book][ch]
                if diff_verses:
                    result[book][ch] = diff_verses
            if not result[book]:
                del result[book]

        return result, set(self._sub_verses) - set(other._sub_verses)