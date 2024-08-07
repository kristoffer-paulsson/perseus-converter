import unicodedata
from types import MappingProxyType

from greekparsify.inflect import Inflect
from greekparsify.modify import Articles
from greekparsify.prepos import Prepositions
from greektextify.beta.word import BetaWord
from greektextify.nlp.debug import Debugger
from greektextify.nlp.detoken import Detokenizer
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.database import GreekDatabase
from greektextify.text.extended import GreekExtended
from greektextify.text.glyph import GREEK_GLYPH_COMBO, GreekGlyph
from greektextify.text.midway import GreekMidway
from greektextify.text.prnt import PrintGreek
from greektextify.text.word import GreekWord
from parse.prnt import PrintGreekRoman


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
    for w, t in Prepositions.PREP:
        w1 = GreekWord.glyphen(w[0])
        print('\\grc{' + PrintGreek.format(w1) + '} \\trc{' + PrintGreekRoman.format(w1) + '} & ', end='', sep='')
        short = list()
        for w2 in w[1:]:
            w2a = GreekWord.glyphen(w2)
            short.append('\\grc{' + PrintGreek.format(w2a) + '}')
        if short:
            print(', '.join(short), end='', sep='')
        print(' & ', end='', sep='')
        case = list()
        for t2 in t.split('_'):
            case.append('\\tsc{' + t2.capitalize() + '}')
        if case:
            print(', '.join(case), end='', sep='')
        print(' \\\\')


def main8():
    for l in sorted(list(set(Articles.STRUCTS.keys()))):
        print(PrintGreek.format(l))
    #for l in sorted(list(set(Prepositions.PREPOS.keys()))):
    #    print(PrintGreek.format(l))


def main7():
    db = MappingProxyType(dict(GreekDatabase.ALL_UTF_LETTERS))
    da_set = set()
    pdb = dict()

    for l in list(GreekAlphabet.CASE_LOWER | GreekAlphabet.CASE_UPPER):
        g = db[l]
        da_set.add(g)

        gl = str(g)
        s = write_prog(gl[15])
        gl = gl[:14] + s + gl[17:]

        print(naming(l) + " = (" + gl + ", " + write_prog(l) + ")")

    for l in GreekExtended.EXPANDABLE_LETTERS.keys():
        g = db[l]
        if g not in da_set:
            da_set.add(g)
            gl = str(g)
            s = write_prog(gl[15])
            gl = gl[:14] + s + gl[17:]

            print(naming(l) + " = (" + gl + ", " + write_prog(l) + ")")

    for l in GreekMidway.EXPANDABLE_LETTERS.keys():
        g = db[l]
        if g not in da_set:
            da_set.add(g)
            gl = str(g)
            s = write_prog(gl[15])
            gl = gl[:14] + s + gl[17:]

            print(naming(l) + " = (" + gl + ", " + write_prog(l) + ")")


def main6():
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
        print(PrintGreek.format(w) + ' (' + PrintGreekRoman.format(w) + ') ' + ', '.join(["{}-{}-{}".format(Inflect.CASE[c], Inflect.GENDER[g], Inflect.NUMBER[n]) for c, g, n in t]))


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
