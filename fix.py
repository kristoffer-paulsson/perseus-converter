from pathlib import PurePath
from typing import Tuple

import regex

from greekparsify.parsing import GreekParsing
from greektextify.text.prnt import PrintGreek
from parse.prnt import PrintGreekRoman

CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≡ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"
NOT_CORE = r"(([0-9A-F]{4}) \S ([A-Z \n]+)\n≈ ([0-9A-F]{4}) \S  ([0-9A-F]{4}))+"


FILTER = (' ', '\n', 'GREEK', 'LETTER', 'WITH', 'AND')


TEXT = """
Ἦν δὲ ἄνθρωπος ἐκ τῶν Φαρισαίων, Νικόδημος ὄνομα αὐτῷ, ἄρχων τῶν Ἰουδαίων· [2] οὗτος ἦλθεν πρὸς αὐτὸν νυκτὸς 
καὶ εἶπεν αὐτῷ Ῥαββεί, οἴδαμεν ὅτι ἀπὸ θεοῦ ἐλήλυθας διδάσκαλος· οὐδεὶς γὰρ δύναται ταῦτα τὰ σημεῖα ποιεῖν ἃ 
σὺ ποιεῖς, ἐὰν μὴ ᾖ ὁ θεὸς μετ᾽ αὐτοῦ. [3] ἀπεκρίθη Ἰησοῦς καὶ εἶπεν αὐτῷ Ἀμὴν ἀμὴν λέγω σοι, ἐὰν μή τις γεννηθῇ 
ἄνωθεν, οὐ δύναται ἰδεῖν τὴν βασιλείαν τοῦ θεοῦ. [4] λέγει πρὸς αὐτὸν [ὁ] Νικόδημος Πῶς δύναται ἄνθρωπος γεννηθῆναι 
γέρων ὤν; μὴ δύναται εἰς τὴν κοιλίαν τῆς μητρὸς αὐτοῦ δεύτερον εἰσελθεῖν καὶ γεννηθῆναι; [5] ἀπεκρίθη [ὁ] Ἰησοῦς 
Ἀμὴν ἀμὴν λέγω σοι, ἐὰν μή τις γεννηθῇ ἐξ ὕδατος καὶ πνεύματος, οὐ δύναται εἰσελθεῖν εἰς τὴν βασιλείαν τοῦ θεοῦ. 
[6] τὸ γεγεννημένον ἐκ τῆς σαρκὸς σάρξ ἐστιν, καὶ τὸ γεγεννημένον ἐκ τοῦ πνεύματος πνεῦμά ἐστιν. [7] μὴ θαυμάσῃς 
ὅτι εἶπόν σοι Δεῖ ὑμᾶς γεννηθῆναι ἄνωθεν. [8] τὸ πνεῦμα ὅπου θέλει πνεῖ, καὶ τὴν φωνὴν αὐτοῦ ἀκούεις, ἀλλ᾽ οὐκ 
οἶδας πόθεν ἔρχεται καὶ ποῦ ὑπάγει· οὕτως ἐστὶν πᾶς ὁ γεγεννημένος ἐκ τοῦ πνεύματος. [9] ἀπεκρίθη Νικόδημος καὶ 
εἶπεν αὐτῷ Πῶς δύναται ταῦτα γενέσθαι; [10] ἀπεκρίθη Ἰησοῦς καὶ εἶπεν αὐτῷ Σὺ εἶ ὁ διδάσκαλος τοῦ Ἰσραὴλ καὶ 
ταῦτα οὐ γινώσκεις; [11] ἀμὴν ἀμὴν λέγω σοι ὅτι ὃ οἴδαμεν λαλοῦμεν καὶ ὃ ἑωράκαμεν μαρτυροῦμεν, καὶ τὴν μαρτυρίαν
ἡμῶν οὐ λαμβάνετε. [12] εἰ τὰ ἐπίγεια εἶπον ὑμῖν καὶ οὐ πιστεύετε, πῶς ἐὰν εἴπω ὑμῖν τὰ ἐπουράνια πιστεύσετε; 
[13] καὶ οὐδεὶς ἀναβέβηκεν εἰς τὸν οὐρανὸν εἰ μὴ ὁ ἐκ τοῦ οὐρανοῦ καταβάς, ὁ υἱὸς τοῦ ἀνθρώπου. [14] καὶ καθὼς 
Μωυσῆς ὕψωσεν τὸν ὄφιν ἐν τῇ ἐρήμῳ, οὕτως ὑψωθῆναι δεῖ τὸν υἱὸν τοῦ ἀνθρώπου, [15] ἵνα πᾶς ὁ πιστεύων ἐν αὐτῷ 
ἔχῃ ζωὴν αἰώνιον. [16] Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον ὥστε τὸν υἱὸν τὸν μονογενῆ ἔδωκεν, ἵνα πᾶς ὁ πιστεύων 
εἰς αὐτὸν μὴ ἀπόληται ἀλλὰ ἔχῃ ζωὴν αἰώνιον. [17] οὐ γὰρ ἀπέστειλεν ὁ θεὸς τὸν υἱὸν εἰς τὸν κόσμον ἵνα κρίνῃ τὸν 
κόσμον, ἀλλ᾽ ἵνα σωθῇ ὁ κόσμος δι᾽ αὐτοῦ. [18] ὁ πιστεύων εἰς αὐτὸν οὐ κρίνεται. ὁ μὴ πιστεύων ἤδη κέκριται, ὅτι 
μὴ πεπίστευκεν εἰς τὸ ὄνομα τοῦ μονογενοῦς υἱοῦ τοῦ θεοῦ. [19] αὕτη δέ ἐστιν ἡ κρίσις ὅτι τὸ φῶς ἐλήλυθεν εἰς 
τὸν κόσμον καὶ ἠγάπησαν οἱ ἄνθρωποι μᾶλλον τὸ σκότος ἢ τὸ φῶς, ἦν γὰρ αὐτῶν πονηρὰ τὰ ἔργα. [20] πᾶς γὰρ ὁ φαῦλα 
πράσσων μισεῖ τὸ φῶς καὶ οὐκ ἔρχεται πρὸς τὸ φῶς, ἵνα μὴ ἐλεγχθῇ τὰ ἔργα αὐτοῦ· [21] ὁ δὲ ποιῶν τὴν ἀλήθειαν ἔρχεται 
πρὸς τὸ φῶς, ἵνα φανερωθῇ αὐτοῦ τὰ ἔργα ὅτι ἐν θεῷ ἐστὶν εἰργασμένα.
"""


def main():
    tknzr = GreekParsing(TEXT)
    tokens = tknzr.tokenize()
    for tt, token in tokens:
        if tt == 0:
            print(PrintGreek.format(token), PrintGreekRoman.format(token))
        elif tt == 4:
            print(' ')
        else:
            print(token)


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
