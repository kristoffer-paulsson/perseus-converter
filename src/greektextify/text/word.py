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
"""Greek word class segment."""
from typing import Tuple

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.extended import GreekExtended
from greektextify.text.glyph import GreekGlyph
from greektextify.text.immaterializer import TokenImmaterializableMixin
from greektextify.text.midway import GreekMidway


class GreekWord(TokenImmaterializableMixin):
    """Greek word analyzer and parsers."""

    # Smyth grammar 1.1.2 *6 -> ei and ou counts as genuine if having diaresis, else if without as spurious.
    # Smyth grammar 1.1.2 *6 + *7 -> learn
    # Smyth grammar 1.1.2 *8 -> dipthongs ending in iota or upsilon with diaeresis are not diphtongs!
    DIPHTHONGS_PROPER = (
        GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_ETA + GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_UPSILON + GreekAlphabet.LOWER_IOTA
    )

    DIPHTHONGS_IMPROPER = (
        GreekAlphabet.LOWER_ALPHA + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
        GreekAlphabet.LOWER_ETA + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
        GreekAlphabet.LOWER_OMICRON + GreekDiacritic.COMBINING_YPOGEGRAMMENI,
    )

    DIPHTHONGS = DIPHTHONGS_IMPROPER + DIPHTHONGS_IMPROPER

    DIPHTHONG_IONIC = (GreekAlphabet.LOWER_OMEGA + GreekAlphabet.LOWER_UPSILON,)

    # Smyth grammar 1.1.3 *9 -> All initial vowels and diphthongs must have any breathing mark.

    WORD_CHARS = frozenset(
        set(GreekExtended.LETTERS) | set(GreekExtended.DIACRITICS) | set(GreekMidway.LETTERS) |
        set(GreekAlphabet.ALPHABET) | set(GreekDiacritic.DIACRITICS) |
        set(GreekMidway.MODIFIERS) # | set(GreekMidway.APOSTROPHE)
    )

    def __init__(self, word: str):
        self._word = word
        self._glyphs = self.glyphen(word)

    @property
    def glyphs(self) -> Tuple[GreekGlyph]:
        return self._glyphs

    @property
    def hyphen(self) -> bool:
        return GreekAlphabet.HYPHEN_MINUS in self._word

    @property
    def apostrophe(self) -> bool:
        return self._word[-1] == GreekMidway.APOSTROPHE

    @classmethod
    def immaterialize(cls, text: str) -> Tuple[str, ...]:
        token = list()
        for ch in text:
            if ch in cls.WORD_CHARS:
                token.append(ch)
            else:
                break

        if len(token) == 0:
            return tuple()
        elif token[-1] == GreekAlphabet.HYPHEN_MINUS:
            return tuple(token[:-1])
        elif token[0] == GreekAlphabet.HYPHEN_MINUS:
            return tuple()
        else:
            return tuple(token)

    @classmethod
    def glyphen(cls, word: str) -> Tuple[GreekGlyph]:
        apostrophe = word[-1] == GreekMidway.APOSTROPHE
        position = 0
        length = len(word)-1 if apostrophe else len(word)
        glyphs = list()

        while position != length:
            glyph, size = GreekGlyph.glyphen(word[position:])
            glyphs.append(glyph)
            position += size

        if apostrophe:
            glyphs.append(GreekGlyph(GreekMidway.APOSTROPHE, False, False, False, False, False, False, False, False, False))

        return tuple(glyphs)

    @classmethod
    def cmp_all(cls, word: Tuple[GreekGlyph], other: Tuple[GreekGlyph], ignore_case: bool = False) -> bool:
        if len(word) != len(other):
            return False
        else:
            same = True
            for w, o in zip(word, other):
                same = same if w.cmp_all(o, ignore_case) else False
            return same

    @classmethod
    def cmp_semi(cls, word: Tuple[GreekGlyph], other: Tuple[GreekGlyph], ignore_case: bool = False) -> bool:
        if len(word) != len(other):
            return False
        else:
            same = True
            for w, o in zip(word, other):
                same = same if w.cmp_semi(o, ignore_case) else False
            return same

    @classmethod
    def cmp_case(cls, word: Tuple[GreekGlyph], other: Tuple[GreekGlyph], ignore_case: bool = False) -> bool:
        if len(word) != len(other):
            return False
        else:
            same = True
            for w, o in zip(word, other):
                same = same if w.cmp_case(o, ignore_case) else False
            return same




