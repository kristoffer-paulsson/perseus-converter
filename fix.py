from pathlib import PurePath, PosixPath
from typing import Tuple

import regex

from greekparsify.grammar import GreekGrammar
from greekparsify.parsing import GreekParsing
from greekparsify.prepos import Prepositions
from greektextify.text.prnt import PrintGreek


CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≡ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"
NOT_CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≈ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"


FILTER = (' ', '\n', 'GREEK', 'LETTER', 'WITH', 'AND')


TEXT = """
[3] Θέλω δὲ ὑμᾶς εἰδέναι ὅτι παντὸς ἀνδρὸς ἡ κεφαλὴ ὁ Χριστός ἐστιν, κεφαλὴ δὲ γυναικὸς ὁ ἀνήρ, κεφαλὴ δὲ τοῦ Χριστοῦ 
ὁ θεός. [4] πᾶς ἀνὴρ προσευχόμενος ἢ προφητεύων κατὰ κεφαλῆς ἔχων καταισχύνει τὴν κεφαλὴν αὐτοῦ. [5] πᾶσα δὲ γυνὴ 
προσευχομένη ἢ προφητεύουσα ἀκατακαλύπτῳ τῇ κεφαλῇ καταισχύνει τὴν κεφαλὴν αὐτῆς· ἓν γάρ ἐστιν καὶ τὸ αὐτὸ 
τῇ ἐξυρημένῃ. [6] εἰ γὰρ οὐ κατακαλύπτεται γυνή, καὶ κειράσθω· εἰ δὲ αἰσχρὸν γυναικὶ τὸ κείρασθαι ἢ ξυρᾶσθαι, 
κατακαλυπτέσθω. [7] Ἀνὴρ μὲν γὰρ οὐκ ὀφείλει κατακαλύπτεσθαι τὴν κεφαλὴν εἰκὼν καὶ δόξα θεοῦ ὑπάρχων· ἡ γυνὴ δὲ 
δόξα ἀνδρός ἐστιν. [8] οὐ γάρ ἐστιν ἀνὴρ ἐκ γυναικὸς ἀλλὰ γυνὴ ἐξ ἀνδρός· [9] καὶ γὰρ οὐκ ἐκτίσθη ἀνὴρ διὰ τὴν 
γυναῖκα ἀλλὰ γυνὴ διὰ τὸν ἄνδρα. [10] διὰ τοῦτο ὀφείλει ἡ γυνὴ ἐξουσίαν ἔχειν ἐπὶ τῆς κεφαλῆς διὰ τοὺς ἀγγέλους. 
[11] πλὴν οὔτε γυνὴ χωρὶς ἀνδρὸς οὔτε ἀνὴρ χωρὶς γυναικὸς ἐν κυρίῳ· [12] ὥσπερ γὰρ ἡ γυνὴ ἐκ τοῦ ἀνδρός, οὕτως 
καὶ ὁ ἀνὴρ διὰ τῆς γυναικός· τὰ δὲ πάντα ἐκ τοῦ θεοῦ. [13] Ἐν ὑμῖν αὐτοῖς κρίνατε· πρέπον ἐστὶν γυναῖκα ἀκατακάλυπτον 
τῷ θεῷ προσεύχεσθαι; [14] οὐδὲ ἡ φύσις αὐτὴ διδάσκει ὑμᾶς ὅτι ἀνὴρ μὲν ἐὰν κομᾷ ἀτιμία αὐτῷ ἐστιν, 
[15] γυνὴ δὲ ἐὰν κομᾷ δόξα αὐτῇ ἐστιν; ὅτι ἡ κόμη ἀντὶ περιβολαίου δέδοται [αὐτῇ]. 
"""


def main():
    tknzr = GreekParsing(TEXT)
    tokens = tknzr.tokenize()
    grammar = GreekGrammar(tokens)
    grammar.analyze(Prepositions)


def main3():
    tknzr = GreekParsing(TEXT)
    tokens = tknzr.tokenize()
    text = ''
    for tt, token in tokens:
        if tt == 0:
            if Prepositions.is_preposition(token):
                text += '\\underline{\\grc{' + PrintGreek.format(token) + '}}'
            else:
                text += '\\grc{' + PrintGreek.format(token) + '}'
            # print(PrintGreekRoman.format(token), end='', sep='')
        elif tt == 4:
            text += ' '
        else:
            text += token

    tknzr.save_tex(tknzr.load_tmpl(text), 'prepos')


def main2():
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
