from greektextify.beta.word import BetaWord


def main():
    WORD = "a)nekla/lhta"
    print(WORD)
    BetaWord.glyphen(WORD.upper())


if __name__ == '__main__':
    main()
