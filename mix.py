from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.combinations import GreekCombinations
from greektextify.text.extended import GreekExtended
from greektextify.text.midway import GreekMidway


def main():
    combos = list()
    for ch in GreekAlphabet.CASE_LOWER:
        combos.append(GreekCombinations.set_diacritics(ch))

    for ch in GreekAlphabet.CASE_UPPER:
        combos.append(GreekCombinations.set_diacritics(ch))

    for ch in GreekMidway.EXPANDABLE_LETTERS.values():
        combos.append(GreekCombinations.set_diacritics(ch))

    for ch in GreekExtended.EXPANDABLE_LETTERS.values():
        combos.append(GreekCombinations.set_diacritics(ch))

    combos.sort()
    for combo in combos:
        print(combo, ',')


if __name__ == '__main__':
    main()
