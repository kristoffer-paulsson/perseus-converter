import unicodedata

from greekparsify.modify import Articles
from greekparsify.prepos import Prepositions
from greektextify.beta.word import BetaWord
from greektextify.nlp.debug import Debugger
from greektextify.nlp.detoken import Detokenizer
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.extended import GreekExtended
from greektextify.text.glyph import GREEK_GLYPH_COMBO, GreekGlyph
from greektextify.text.midway import GreekMidway
from greektextify.text.word import GreekWord


def naming(letter: str) -> str:
    """Naming Greek character correctly."""
    name = unicodedata.name(letter)
    if letter in GreekAlphabet.CASE_UPPER: name = name.replace('CAPITAL', 'UPPER')
    if letter in GreekAlphabet.CASE_LOWER: name = name.replace('SMALL', 'LOWER')
    return '_'.join(filter(lambda x: x not in ('GREEK', 'LETTER', 'WITH', 'AND'), name.split(' ')))


def write_prog(letter: str) -> str:
    name = naming(letter)
    kls = ''
    if letter in GreekAlphabet.ALPHABET: kls = 'GreekAlphabet.'
    elif letter in GreekExtended.LETTERS: kls = 'GreekExtended.'
    # elif letter in GreekExtended.DIACRITICS: kls = 'GreekExtended.'
    elif letter in GreekMidway.LETTERS: kls = 'GreekMidway.'
    # elif letter in GreekDiacritic: kls = 'GreekDiacritic.'

    return kls + name


def main():
    all = GreekAlphabet.CASE_LOWER | GreekAlphabet.CASE_UPPER | GreekMidway.EXPANDABLE_LETTERS.keys() | GreekExtended.EXPANDABLE_LETTERS.keys()
    test = set([GreekGlyph.glyphen(l) for l in all])
    for letter in all:
        print(letter)
    print(len(all))
    print(len(test))
    print(len(GREEK_GLYPH_COMBO))

    da_set = set()

    for l in list(GreekAlphabet.CASE_LOWER | GreekAlphabet.CASE_UPPER):
        g = GreekGlyph.glyphen(l)[0]
        da_set.add(g)

        # gl = str(g)
        # s = write_prog(gl[15])
        # gl = gl[:14] + s + gl[17:]
        # print(naming(l) + " = (" + write_prog(l) + ", " + gl + ")")
        print(naming(l))

        # print((g, "\\u" + "{:04x}".format(ord(l[0]))), ',', naming(l))

    for l in GreekExtended.EXPANDABLE_LETTERS.keys():
        g = GreekGlyph.glyphen(l)[0]
        if g not in da_set:
            da_set.add(g)

        # gl = str(g)
        # s = write_prog(gl[15])
        # gl = gl[:14] + s + gl[17:]
        # print(naming(l) + " = (" + write_prog(l) + ", " + gl + ")")
        print(naming(l))

        # print((g, "\\u" + "{:04x}".format(ord(l[0]))), ',', naming(l))

    for l in GreekMidway.EXPANDABLE_LETTERS.keys():
        g = GreekGlyph.glyphen(l)[0]
        if g not in da_set:
            da_set.add(g)

        # gl = str(g)
        # s = write_prog(gl[15])
        # gl = gl[:14] + s + gl[17:]
        # print(naming(l) + " = (" + write_prog(l) + ", " + gl + ")")
        print(naming(l))

        # print((g, "\\u" + "{:04x}".format(ord(l[0]))), ',', naming(l))

    print(len(da_set))


def main5():
    for w, t in Prepositions.PREPOS.items():
        print(w)
        print(t)


def main4():
    for w, t in Articles.STRUCTS.items():
        print(w, t)


def mai3():
    for article in Articles.MODIFIERS.values():
        print(Detokenizer.build_word(GreekWord.glyphen(article)))
        print(GreekWord.glyphen(article))
        for row in Debugger.glyph(article):
            print(row)
        print()


def main2():
    WORD = "a)nekla/lhta"
    print(WORD)
    print(BetaWord.glyphen(WORD.upper()))


if __name__ == '__main__':
    main()
