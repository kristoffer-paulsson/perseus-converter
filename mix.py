from greekparsify.modify import Articles
from greekparsify.prepos import Prepositions
from greektextify.beta.word import BetaWord
from greektextify.nlp.debug import Debugger
from greektextify.nlp.detoken import Detokenizer
from greektextify.text.word import GreekWord


def main():
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
