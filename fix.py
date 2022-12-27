from pathlib import PurePath

import regex

CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≡ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"
NOT_CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≈ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"


FILTER = (' ', '\n', 'GREEK', 'LETTER', 'WITH', 'AND')

def main():
    path = PurePath('meta/midway.txt')
    with open(path) as fobj:
        text = fobj.read()
        matches = regex.findall(CORE, text)
        constants = dict()
        expands = dict()
        for match in matches:
            original = match[1]
            first = match[3]
            second = match[4]
            parts = regex.split('( |\n)', match[2])
            name = '_'.join([part for part in parts if part not in FILTER])
            # print(name)
            constants[name] = (original, first, second)

        expandable_letters = list()
        expandable_diacritics = list()
        for key, value in constants.items():
            print('{} = \'\\u{}\','.format(key, value[0]))
            output = key + ': '
            letter = regex.findall('(SMALL_[A-Z]+|CAPITAL_[A-Z]+)', key)
            if len(letter) == 1:
                letter = letter[0].replace('SMALL', 'LOWER').replace('CAPITAL', 'UPPER')
                output += 'GreekAlphabet.' + letter
                diacritics = ''
                for diacritic in key.split('_')[2:]:
                    diacritics += ' + GreekDiacritic.COMBINING_' + diacritic
                output += ''.join(diacritics) + ','
                expandable_letters.append(output)
            else:
                diacritics = list()
                for diacritic in key.split('_'):
                    diacritics.append('GreekDiacritic.COMBINING_' + diacritic)
                output += ' + '.join(diacritics) + ','
                expandable_diacritics.append(output)

        for letters in expandable_letters:
            print(letters)
        for diacritics in expandable_diacritics:
            print(diacritics)


if __name__ == '__main__':
    main()
