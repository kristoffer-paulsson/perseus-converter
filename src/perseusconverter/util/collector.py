#
# Copyright (c) 2026 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
from typing import Dict, Set, Tuple, NamedTuple, List

from perseusconverter.util.utils import Counter, BRef

class MutableBStruct(NamedTuple):
    bible: Dict[str, Dict[int, List[int] | Set[int]]]
    sub_verses: List[str]
    missing: Dict[str, Dict[int, List[int] | Set[int]]]

    def add_subverse(self, ref: BRef):
        self.sub_verses.append(str(ref))

    def add_missing(self, ref: BRef):
        if ref.book not in self.missing:
            self.missing[ref.book] = dict()
        if ref.chapter not in self.missing[ref.book]:
            self.missing[ref.book][ref.chapter] = list()
        if ref.verse not in self.missing[ref.book][ref.chapter]:
            self.missing[ref.book][ref.chapter].append(ref.verse)


class BStruct(NamedTuple):
    bible: Dict[str, Dict[int, Tuple[int, ...]]]
    sub_verses: Tuple[str, ...]
    missing: Dict[str, Dict[int, Tuple[int, ...]]]
    duplicates: Tuple[str, ...]
    malplaced: Tuple[str, ...]


class BaseCollector:

    def __init__(self, iterator):
        self._iterator = iterator
        self._model = MutableBStruct(dict(), list(), dict())
        self._duplicates: List[str] = list()
        self._malplaced: List[str] = list()

    def _add_malplaced(self, ref: BRef):
        self._malplaced.append(str(ref))

    def _add_duplicate(self, ref: BRef):
        self._duplicates.append(str(ref))

    def _update_model(self, model: MutableBStruct, bref: BRef, chapter_cnt, verse_cnt) -> bool:
        bible = self._model.bible
        stop = False

        if bref.book not in bible:
            bible[bref.book] = dict()
            chapter_cnt.reset()
        if chapter_cnt.current() < bref.chapter:
            while bref.chapter - chapter_cnt.current() > 1:
                chapter_cnt.increment()
                model.add_missing(BRef(bref.book, chapter_cnt.current(), -1, -1))
            chapter_cnt.increment()
            if chapter_cnt.current() != bref.chapter:
                raise RuntimeError("Chapter mismatch {} / {}".format(chapter_cnt.current(), bref.chapter))
            verse_cnt.reset()
            stop = True
        if bref.sub != -1:
            model.add_subverse(bref)
        elif bref.verse == 0:
            if bref.chapter not in bible[bref.book]:
                bible[bref.book][bref.chapter] = list()
                stop = True
            bible[bref.book][bref.chapter].append(bref.verse)
        elif verse_cnt.current() < bref.verse:
            while bref.verse - verse_cnt.current() > 1:
                verse_cnt.increment()
                model.add_missing(BRef(bref.book, bref.chapter, verse_cnt.current(), -1))
            if bref.chapter not in bible[bref.book]:
                bible[bref.book][bref.chapter] = list()
                stop = True
            else:
                bible[bref.book][bref.chapter].append(bref.verse)
            verse_cnt.increment()
        elif bref.verse in bible[bref.book][bref.chapter]:
            self._add_duplicate(bref)
        else:
            self._add_malplaced(bref)
        return stop

    def _deep_copy(self, orig: Dict[str, Dict[int, List[int] | Set[int]]]) -> Dict[str, Dict[int, Tuple[int, ...]]]:
            """book → chapter → set of verses.
            Accepts both the original list-of-verses form and the
            post-analyze integer-max form.
            """
            deep: Dict[str, Dict[int, Tuple[int, ...]]] = {}
            for book, chapters in orig.items():
                deep[book] = {}
                for ch, verses in chapters.items():
                    if len(verses) > 1 and -1 in verses:
                        verses.remove(-1)
                    deep[book][ch] = tuple(sorted(verses))
            return deep

    def export(self) -> BStruct:
        return BStruct(
            self._deep_copy(self._model.bible),
            tuple(sorted(self._model.sub_verses)),
            self._deep_copy(self._model.missing),
            tuple(sorted(self._duplicates)),
            tuple(sorted(self._malplaced))
        )


class Collector(BaseCollector):

    def __init__(self, iterator):
        super().__init__(iterator)

    def collect(self):
        chapter_cnt = Counter()
        verse_cnt = Counter()

        for bref in self._iterator:
            if isinstance(bref, BRef):
                self._update_model(self._model, bref, chapter_cnt, verse_cnt)

    def _add_malplaced(self, ref: BRef):
        self._malplaced.append(str(ref))

    def _add_duplicate(self, ref: BRef):
        self._duplicates.append(str(ref))

    def analyze(self):
        model = self.export() #self._bible.copy()
        bible = model.bible
        b2 = dict()

        for book in bible.keys():
            b2[book] = dict()
            for chapter in bible[book].keys():
                b2[book][chapter] = max(bible[book][chapter])

        print(list(bible.keys()))
        print(b2)
        print(model.sub_verses)
        print(model.missing)
        print(model.duplicates)
        print(model.malplaced)

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

    def difference(self, other: "BaseCollector") -> Tuple[Dict[str, Dict[int, Set[int]]], Set[str]]:
        """
        Self − other: books → chapters → verses that exist in self but not in other.
        Same return shape as intersect().
        """
        ma = self.export()
        mb = other.export()
        a = ma.bible
        b = mb.bible
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
                diff_verses = set(a[book][ch]) - set(b[book][ch])
                if diff_verses:
                    result[book][ch] = diff_verses
            if not result[book]:
                del result[book]

        return result, set(ma.sub_verses) - set(mb.sub_verses)