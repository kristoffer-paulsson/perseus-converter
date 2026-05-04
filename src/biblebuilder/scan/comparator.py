#
# Copyright (c) 2026 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
from .bgm import BGMScanner
from .ognt import OGNTScanner
from .scanner import ScanIter, Token, Reference
import unicodedata

class LexemeComparator:
    pass


class OGNT2BGMComparator(LexemeComparator):

    def __init__(self, bgmScanner: BGMScanner, ogntScanner: OGNTScanner, start: Reference):
        """Initialize the comparator with scanners for both corpora."""
        self.ogntScanner = ScanIter(ogntScanner, start)
        self.bgmScanner = ScanIter(bgmScanner, start)
        self.errors = dict()

    def error_token(self, token: Token, msg: str) -> Token:
        return Token(token.book, token.chapter, token.verse, token.index, 'error-' + msg)

    def iter(self):

        choices = {}
        """choices = {
            ('οὕτως', 'οὕτω, οὕτως'): (1, "Left exists inside right side"),
            ('τέ', 'τε'): (1, "Same word, use left accentuation"),
            ('καί+ἐγώ', 'κἀγώ'): (2, "Left is weird data, use right side"),
            ('οἶδα', 'εἴδω'): (1, "eido seems confluence, use right"),
            ('ὁράω', 'εἴδω'): (1, "eido seems confluence, use right"),
            ('Δαυίδ', 'Δαυείδ, Δαυίδ, Δαβίδ'): (1, "Left exists inside right side"),
            ('Βαρναβᾶς', 'Βαρνάβας'): (1, "Same word, use left accentuation"),
            ('Σιλᾶς', 'Σίλας'): (1, "Same word, use left accentuation"),
            ('Ἁνανίας', 'Ἀνανίας'): (1, "Same word, use left accentuation"),
            ('καί+ἐάν', 'κἄν'): (2, "Left is weird data, use right side"),
            ('καί+ἐκεῖνος', 'κἀκεῖνος'): (2, "Left is weird data, use right side"),
            ('βαπτιστής', 'Βαπτιστής'): (1, "Same word, use left accentuation"),
            ('Μᾶρκος', 'Μάρκος'): (1, "Same word, use left accentuation"),
            ('δάκρυον', 'δάκρυ, δάκρυον'): (1, "Left exists inside right side"),
            ('καί+ἐκεῖθεν', 'κἀκεῖθεν'): (2, "Left is weird data, use right side"),
            ('ἄρσην', 'ἄρρην, ἄρσην'): (1, "Left exists inside right side"),
            ('ᾅδης', 'ᾍδης'): (1, "Different capitalization, use left accentuation"),
            ('καί+ἐκεῖ', 'κἀκεῖ'): (2, "Left is weird data, use right side"),
            ('Ἁλφαῖος', 'Ἀλφαῖος'): (1, "Same word, use left accentuation"),

            ('λέγω', 'ἔπω, ἐρῶ, εἶπον'): (-1, "Different word, decide later"),
            ('δεῖ', 'δέω'): (-1, "Different word, must be fixed"),
            ('εὐαγγελίζω', 'εὐαγγελίζομαι'): (-1, "Different nuance, fix later"),
            ('εὐθύς', 'εὐθέως'): (-1, "Different nuance, fix later"),
            ('ὁράω', 'ἴδε'): (-1, "Different nuance, must be fixed"),
            ('πολύς', 'πλείων, πλεῖον'): (-1, "Different word, fix later"),
            ('χρυσοῦς', 'χρύσεος'): (-1, "Different nuance, fix later"),
            ('λοιπός', 'λοιπόν'): (-1, "Different nuance, fix later"),
            ('ἑκατοντάρχης', 'ἑκατόνταρχος'): (-1, "Different nuance, fix later"),
            ('Καφαρναούμ', 'Καπερναούμ'): (-1, "Different nuance, fix later"),
            ('Καφαρναούμ', 'Καπερναούμ'): (-1, "Different nuance, fix later"),
            ('ἐλαχύς', 'ἐλάχιστος'): (-1, "Different nuance, fix later"),
            ('ταχύς', 'ταχύ'): (-1, "Different nuance, fix later"),
            ('προλέγω', 'προερέω'): (-1, "Different nuance, fix later"),
            ('μεταμέλομαι', 'μεταμέλλομαι'): (-1, "Different nuance, fix later"),
            ('στρωννύω', 'στρώννυμι'): (-1, "Different nuance, fix later"),
            ('σέβω', 'σέβομαι'): (-1, "Different nuance, fix later"),
            ('ἀποκαθιστάνω', 'ἀποκαθίστημι'): (-1, "Different nuance, fix later"),
            ('Σαμαρίτης', 'Σαμαρείτης'): (-1, "Different nuance, fix later"),
            ('τεσσεράκοντα', 'τεσσαράκοντα'): (-1, "Different nuance, fix later"),
            ('ἐξομολογέω', 'ἐξομολογέομαι'): (-1, "Different nuance, fix later"),
            ('σιδηροῦς', 'σιδήρεος'): (-1, "Different nuance, fix later"),
            ('ἐμπίπλημι', 'ἐμπίμπλημι'): (-1, "Different nuance, fix later"),
            ('συσταυρόω', 'συσταυρόομαι'): (-1, "Different nuance, fix later"),
        }"""

        ognt = iter(self.ogntScanner)
        crash = 0
        diff_cnt = 0
        chosen = None
        for token in self.bgmScanner:
            ogntToken = next(ognt)
            #if not (token.book == ogntToken.book and token.chapter == ogntToken.chapter and token.verse == ogntToken.verse and token.index == ogntToken.index):
            #    print(f"Reference mismatch: BGM {token.book} {token.chapter}:{token.verse} [{token.index}] vs OGNT {ogntToken.book} {ogntToken.chapter}:{ogntToken.verse} [{ogntToken.index}] {token} {ogntToken}")
            #    exit(1)
            token1 = unicodedata.normalize('NFD', token.token)
            token2 = unicodedata.normalize('NFD', ogntToken.token)
            if token1 > token2:
                key = (str(token1), str(token2))
                if key in choices.keys():
                    select = choices[key][0]
                    if select == 1:
                        chosen = token
                    elif select == 2:
                        chosen = ogntToken
                    else:
                        chosen = self.error_token(token, 'suppressed')
                else:
                    if not key in self.errors:
                        self.errors[key] = list()
                    self.errors[key].append((token.book, token.chapter, token.verse, token.index))
                    crash += 1
                    diff_cnt += 1
                    chosen = self.error_token(token, 'unhandled')
            else:
                crash = 0
                chosen = token
            yield chosen
            if crash > 10:
                break
        try:
            next(ognt)
        except StopIteration:
            pass
        else:
            raise RuntimeError("OGNT scanner has more tokens than BGM scanner")

    def get_errors(self, threshold: int):
        for key in self.errors:
            if len(self.errors[key]) > threshold:
                print(f"{key}:")
                for ref in self.errors[key]:
                    print(f"  {ref}")

    def get_error_cnt(self):
        for key in self.errors:
            print(f"{key}: {len(self.errors[key])}")
        print(f"Total unique errors: {len(self.errors)}")
        print(f"Total error occurrences: {sum(len(refs) for refs in self.errors.values())}")
