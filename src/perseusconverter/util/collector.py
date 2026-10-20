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
from perseusconverter.iter.bgmiter import BRef


class Counter:
    def __init__(self, start: int = 0):
        self._start = start
        self._count = self._start

    def increment(self) -> int:
        self._count += 1
        return self._count

    def current(self) -> int:
        return self._count

    def reset(self, start: int = 0) -> None:
        self._start = start
        self._count = start


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
                    self._bible[bref.book][bref.chapter] = list()
                    verse_cnt.reset()
                    chapter_cnt.increment()
                if verse_cnt.current() < bref.verse and bref.sub == -1:
                    while bref.verse - verse_cnt.current() > 1:
                        verse_cnt.increment()
                        self._add_missing(BRef(bref.book, bref.chapter, verse_cnt.current(), -1))
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
        print(self._bible)
        print(self._sub_verses)
        print(self._missing)

    def diff(self, other=None):
        # 1. Befintlig logik för att hitta högsta versen per kapitel i self
        bible_max = self._bible.copy()
        for book in bible_max.keys():
            for chapter in bible_max[book].keys():
                if bible_max[book][chapter]:
                    bible_max[book][chapter] = max(bible_max[book][chapter])

        print("--- Analys av Self ---")
        print("Högsta verser per kapitel:", bible_max)
        print("Sub-verser:", self._sub_verses)
        print("Saknade verser:", self._missing)

        # 2. Om en annan Collector skickas med -> Utför subtraktion (self - other)
        if other is not None and isinstance(other, Collector):
            print("\n--- Differens (Self minus Other) ---")

            # A. Diffa vanliga verser i _bible
            bible_diff = dict()
            for book, chapters in self._bible.items():
                for chapter, verses in chapters.items():
                    # Hämta verser som finns i self men inte i other
                    other_verses = other._bible.get(book, {}).get(chapter, [])
                    diff_verses = [v for v in verses if v not in other_verses]

                    if diff_verses:
                        if book not in bible_diff:
                            bible_diff[book] = dict()
                        bible_diff[book][chapter] = diff_verses
            print("Verser unika för Self:", bible_diff)

            # B. Diffa sub-verser (konverterar till set för snabb och ren mängdlära)
            self_subs = set(self._sub_verses)
            other_subs = set(other._sub_verses)
            sub_diff = sorted(list(self_subs - other_subs))
            print("Sub-verser unika för Self:", sub_diff)

            # C. Diffa saknade verser i _missing
            missing_diff = dict()
            for book, chapters in self._missing.items():
                for chapter, verses in chapters.items():
                    other_missing_verses = other._missing.get(book, {}).get(chapter, [])
                    diff_missing = [v for v in verses if v not in other_missing_verses]

                    if diff_missing:
                        if book not in missing_diff:
                            missing_diff[book] = dict()
                        missing_diff[book][chapter] = diff_missing
            print("Saknade verser unika för Self (ej markerade som saknade i Other):", missing_diff)

            # Returnera resultatet som en dictionary om det behövs i koden
            return {
                "bible_diff": bible_diff,
                "sub_diff": sub_diff,
                "missing_diff": missing_diff
            }


