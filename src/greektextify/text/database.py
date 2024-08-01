#
# Copyright (c) 2024 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""All legal or valid glyphs for printing and using instead of duplicates."""
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diacritic import GreekDiacritic
from greektextify.text.extended import GreekExtended
from greektextify.text.glyph import GreekGlyph
from greektextify.text.midway import GreekMidway


class GreekDatabase:
    APOSTROPHE = (GreekMidway.APOSTROPHE,
                  GreekGlyph(ch=GreekMidway.APOSTROPHE, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False)),
    HYPHEN_MINUS = (GreekAlphabet.HYPHEN_MINUS,
                    GreekGlyph(ch=GreekAlphabet.HYPHEN_MINUS, psili=False, dasia=False, ypogegrammeni=False,
                               varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))

    LOWER_IOTA = (GreekAlphabet.LOWER_IOTA,
                  GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_PI = (GreekAlphabet.LOWER_PI,
                GreekGlyph(ch=GreekAlphabet.LOWER_PI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_RHO = (GreekAlphabet.LOWER_RHO,
                 GreekGlyph(ch=GreekAlphabet.LOWER_RHO, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_PI = (GreekAlphabet.UPPER_PI,
                GreekGlyph(ch=GreekAlphabet.UPPER_PI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_FINAL_SIGMA = (GreekAlphabet.LOWER_FINAL_SIGMA,
                         GreekGlyph(ch=GreekAlphabet.LOWER_FINAL_SIGMA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    UPPER_RHO = (GreekAlphabet.UPPER_RHO,
                 GreekGlyph(ch=GreekAlphabet.UPPER_RHO, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_CHI = (GreekAlphabet.UPPER_CHI,
                 GreekGlyph(ch=GreekAlphabet.UPPER_CHI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_KAPPA = (GreekAlphabet.UPPER_KAPPA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_KAPPA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_BETA = (GreekAlphabet.UPPER_BETA,
                  GreekGlyph(ch=GreekAlphabet.UPPER_BETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_GAMMA = (GreekAlphabet.LOWER_GAMMA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_GAMMA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_ETA = (GreekAlphabet.LOWER_ETA,
                 GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_CHI = (GreekAlphabet.LOWER_CHI,
                 GreekGlyph(ch=GreekAlphabet.LOWER_CHI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_PSI = (GreekAlphabet.UPPER_PSI,
                 GreekGlyph(ch=GreekAlphabet.UPPER_PSI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_XI = (GreekAlphabet.LOWER_XI,
                GreekGlyph(ch=GreekAlphabet.LOWER_XI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_LAMDA = (GreekAlphabet.UPPER_LAMDA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_LAMDA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_DELTA = (GreekAlphabet.LOWER_DELTA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_DELTA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_DIGAMMA = (GreekAlphabet.LOWER_DIGAMMA,
                     GreekGlyph(ch=GreekAlphabet.LOWER_DIGAMMA, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    UPPER_TAU = (GreekAlphabet.UPPER_TAU,
                 GreekGlyph(ch=GreekAlphabet.UPPER_TAU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_OMEGA = (GreekAlphabet.LOWER_OMEGA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_XI = (GreekAlphabet.UPPER_XI,
                GreekGlyph(ch=GreekAlphabet.UPPER_XI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    DIGAMMA = (GreekAlphabet.DIGAMMA,
               GreekGlyph(ch=GreekAlphabet.DIGAMMA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                          oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_NU = (GreekAlphabet.LOWER_NU,
                GreekGlyph(ch=GreekAlphabet.LOWER_NU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_ZETA = (GreekAlphabet.UPPER_ZETA,
                  GreekGlyph(ch=GreekAlphabet.UPPER_ZETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_ALPHA = (GreekAlphabet.UPPER_ALPHA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_GAMMA = (GreekAlphabet.UPPER_GAMMA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_GAMMA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_IOTA = (GreekAlphabet.UPPER_IOTA,
                  GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_UPSILON = (GreekAlphabet.UPPER_UPSILON,
                     GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    LOWER_PSI = (GreekAlphabet.LOWER_PSI,
                 GreekGlyph(ch=GreekAlphabet.LOWER_PSI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_LAMDA = (GreekAlphabet.LOWER_LAMDA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_LAMDA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_UPSILON = (GreekAlphabet.LOWER_UPSILON,
                     GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    LOWER_MU = (GreekAlphabet.LOWER_MU,
                GreekGlyph(ch=GreekAlphabet.LOWER_MU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_EPSILON = (GreekAlphabet.LOWER_EPSILON,
                     GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    LOWER_ALPHA = (GreekAlphabet.LOWER_ALPHA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_ZETA = (GreekAlphabet.LOWER_ZETA,
                  GreekGlyph(ch=GreekAlphabet.LOWER_ZETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_NU = (GreekAlphabet.UPPER_NU,
                GreekGlyph(ch=GreekAlphabet.UPPER_NU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_THETA = (GreekAlphabet.UPPER_THETA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_THETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_OMICRON = (GreekAlphabet.LOWER_OMICRON,
                     GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    LOWER_KAPPA = (GreekAlphabet.LOWER_KAPPA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_KAPPA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_PHI = (GreekAlphabet.LOWER_PHI,
                 GreekGlyph(ch=GreekAlphabet.LOWER_PHI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_EPSILON = (GreekAlphabet.UPPER_EPSILON,
                     GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    LOWER_SIGMA = (GreekAlphabet.LOWER_SIGMA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_SIGMA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_SIGMA = (GreekAlphabet.UPPER_SIGMA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_SIGMA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_PHI = (GreekAlphabet.UPPER_PHI,
                 GreekGlyph(ch=GreekAlphabet.UPPER_PHI, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_TAU = (GreekAlphabet.LOWER_TAU,
                 GreekGlyph(ch=GreekAlphabet.LOWER_TAU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_OMICRON = (GreekAlphabet.UPPER_OMICRON,
                     GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                macron=False))
    UPPER_OMEGA = (GreekAlphabet.UPPER_OMEGA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_BETA = (GreekAlphabet.LOWER_BETA,
                  GreekGlyph(ch=GreekAlphabet.LOWER_BETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                             oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_ETA = (GreekAlphabet.UPPER_ETA,
                 GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                            oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    LOWER_THETA = (GreekAlphabet.LOWER_THETA,
                   GreekGlyph(ch=GreekAlphabet.LOWER_THETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_DELTA = (GreekAlphabet.UPPER_DELTA,
                   GreekGlyph(ch=GreekAlphabet.UPPER_DELTA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                              oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    UPPER_MU = (GreekAlphabet.UPPER_MU,
                GreekGlyph(ch=GreekAlphabet.UPPER_MU, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                           oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_PSILI = (GreekExtended.SMALL_ALPHA_PSILI,
                         GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_ALPHA_DASIA = (GreekExtended.SMALL_ALPHA_DASIA,
                         GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_ALPHA_PSILI_VARIA = (GreekExtended.SMALL_ALPHA_PSILI_VARIA,
                               GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_ALPHA_DASIA_VARIA = (GreekExtended.SMALL_ALPHA_DASIA_VARIA,
                               GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_ALPHA_PSILI_OXIA = (GreekExtended.SMALL_ALPHA_PSILI_OXIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_ALPHA_DASIA_OXIA = (GreekExtended.SMALL_ALPHA_DASIA_OXIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_ALPHA_PSILI_PERISPOMENI = (GreekExtended.SMALL_ALPHA_PSILI_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_DASIA_PERISPOMENI = (GreekExtended.SMALL_ALPHA_DASIA_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_PSILI = (GreekExtended.CAPITAL_ALPHA_PSILI,
                           GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_ALPHA_DASIA = (GreekExtended.CAPITAL_ALPHA_DASIA,
                           GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_ALPHA_PSILI_VARIA = (GreekExtended.CAPITAL_ALPHA_PSILI_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                            varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    CAPITAL_ALPHA_DASIA_VARIA = (GreekExtended.CAPITAL_ALPHA_DASIA_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                            varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    CAPITAL_ALPHA_PSILI_OXIA = (GreekExtended.CAPITAL_ALPHA_PSILI_OXIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_ALPHA_DASIA_OXIA = (GreekExtended.CAPITAL_ALPHA_DASIA_OXIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_ALPHA_PSILI_PERISPOMENI = (GreekExtended.CAPITAL_ALPHA_PSILI_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_DASIA_PERISPOMENI = (GreekExtended.CAPITAL_ALPHA_DASIA_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_EPSILON_PSILI = (GreekExtended.SMALL_EPSILON_PSILI,
                           GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=True, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_EPSILON_DASIA = (GreekExtended.SMALL_EPSILON_DASIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_EPSILON_PSILI_VARIA = (GreekExtended.SMALL_EPSILON_PSILI_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=True, dasia=False,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_EPSILON_DASIA_VARIA = (GreekExtended.SMALL_EPSILON_DASIA_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=True,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_EPSILON_PSILI_OXIA = (GreekExtended.SMALL_EPSILON_PSILI_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    SMALL_EPSILON_DASIA_OXIA = (GreekExtended.SMALL_EPSILON_DASIA_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_EPSILON_PSILI = (GreekExtended.CAPITAL_EPSILON_PSILI,
                             GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=True, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_EPSILON_DASIA = (GreekExtended.CAPITAL_EPSILON_DASIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_EPSILON_PSILI_VARIA = (GreekExtended.CAPITAL_EPSILON_PSILI_VARIA,
                                   GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=True, dasia=False,
                                              ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                              dialytika=False, vrachy=False, macron=False))
    CAPITAL_EPSILON_DASIA_VARIA = (GreekExtended.CAPITAL_EPSILON_DASIA_VARIA,
                                   GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=True,
                                              ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                              dialytika=False, vrachy=False, macron=False))
    CAPITAL_EPSILON_PSILI_OXIA = (GreekExtended.CAPITAL_EPSILON_PSILI_OXIA,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=True, dasia=False,
                                             ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                             dialytika=False, vrachy=False, macron=False))
    CAPITAL_EPSILON_DASIA_OXIA = (GreekExtended.CAPITAL_EPSILON_DASIA_OXIA,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=True,
                                             ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                             dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_PSILI = (GreekExtended.SMALL_ETA_PSILI,
                       GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False, ypogegrammeni=False, varia=False,
                                  oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_DASIA = (GreekExtended.SMALL_ETA_DASIA,
                       GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True, ypogegrammeni=False, varia=False,
                                  oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_PSILI_VARIA = (GreekExtended.SMALL_ETA_PSILI_VARIA,
                             GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                        varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    SMALL_ETA_DASIA_VARIA = (GreekExtended.SMALL_ETA_DASIA_VARIA,
                             GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                        varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    SMALL_ETA_PSILI_OXIA = (GreekExtended.SMALL_ETA_PSILI_OXIA,
                            GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=False))
    SMALL_ETA_DASIA_OXIA = (GreekExtended.SMALL_ETA_DASIA_OXIA,
                            GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                       varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=False))
    SMALL_ETA_PSILI_PERISPOMENI = (GreekExtended.SMALL_ETA_PSILI_PERISPOMENI,
                                   GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                              varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                              macron=False))
    SMALL_ETA_DASIA_PERISPOMENI = (GreekExtended.SMALL_ETA_DASIA_PERISPOMENI,
                                   GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                              varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                              macron=False))
    CAPITAL_ETA_PSILI = (GreekExtended.CAPITAL_ETA_PSILI,
                         GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    CAPITAL_ETA_DASIA = (GreekExtended.CAPITAL_ETA_DASIA,
                         GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    CAPITAL_ETA_PSILI_VARIA = (GreekExtended.CAPITAL_ETA_PSILI_VARIA,
                               GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    CAPITAL_ETA_DASIA_VARIA = (GreekExtended.CAPITAL_ETA_DASIA_VARIA,
                               GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    CAPITAL_ETA_PSILI_OXIA = (GreekExtended.CAPITAL_ETA_PSILI_OXIA,
                              GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    CAPITAL_ETA_DASIA_OXIA = (GreekExtended.CAPITAL_ETA_DASIA_OXIA,
                              GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    CAPITAL_ETA_PSILI_PERISPOMENI = (GreekExtended.CAPITAL_ETA_PSILI_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_DASIA_PERISPOMENI = (GreekExtended.CAPITAL_ETA_DASIA_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    SMALL_IOTA_PSILI = (GreekExtended.SMALL_IOTA_PSILI,
                        GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                   varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_IOTA_DASIA = (GreekExtended.SMALL_IOTA_DASIA,
                        GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                   varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_IOTA_PSILI_VARIA = (GreekExtended.SMALL_IOTA_PSILI_VARIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                         varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_IOTA_DASIA_VARIA = (GreekExtended.SMALL_IOTA_DASIA_VARIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                         varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_IOTA_PSILI_OXIA = (GreekExtended.SMALL_IOTA_PSILI_OXIA,
                             GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    SMALL_IOTA_DASIA_OXIA = (GreekExtended.SMALL_IOTA_DASIA_OXIA,
                             GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                        varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    SMALL_IOTA_PSILI_PERISPOMENI = (GreekExtended.SMALL_IOTA_PSILI_PERISPOMENI,
                                    GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=True, dasia=False,
                                               ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                               dialytika=False, vrachy=False, macron=False))
    SMALL_IOTA_DASIA_PERISPOMENI = (GreekExtended.SMALL_IOTA_DASIA_PERISPOMENI,
                                    GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=True,
                                               ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                               dialytika=False, vrachy=False, macron=False))
    CAPITAL_IOTA_PSILI = (GreekExtended.CAPITAL_IOTA_PSILI,
                          GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_IOTA_DASIA = (GreekExtended.CAPITAL_IOTA_DASIA,
                          GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                     varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_IOTA_PSILI_VARIA = (GreekExtended.CAPITAL_IOTA_PSILI_VARIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_IOTA_DASIA_VARIA = (GreekExtended.CAPITAL_IOTA_DASIA_VARIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_IOTA_PSILI_OXIA = (GreekExtended.CAPITAL_IOTA_PSILI_OXIA,
                               GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=True, dasia=False, ypogegrammeni=False,
                                          varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    CAPITAL_IOTA_DASIA_OXIA = (GreekExtended.CAPITAL_IOTA_DASIA_OXIA,
                               GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=True, ypogegrammeni=False,
                                          varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    CAPITAL_IOTA_PSILI_PERISPOMENI = (GreekExtended.CAPITAL_IOTA_PSILI_PERISPOMENI,
                                      GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=True, dasia=False,
                                                 ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                 dialytika=False, vrachy=False, macron=False))
    CAPITAL_IOTA_DASIA_PERISPOMENI = (GreekExtended.CAPITAL_IOTA_DASIA_PERISPOMENI,
                                      GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=True,
                                                 ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                 dialytika=False, vrachy=False, macron=False))
    SMALL_OMICRON_PSILI = (GreekExtended.SMALL_OMICRON_PSILI,
                           GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=True, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_OMICRON_DASIA = (GreekExtended.SMALL_OMICRON_DASIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=True, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_OMICRON_PSILI_VARIA = (GreekExtended.SMALL_OMICRON_PSILI_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=True, dasia=False,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_OMICRON_DASIA_VARIA = (GreekExtended.SMALL_OMICRON_DASIA_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=True,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_OMICRON_PSILI_OXIA = (GreekExtended.SMALL_OMICRON_PSILI_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    SMALL_OMICRON_DASIA_OXIA = (GreekExtended.SMALL_OMICRON_DASIA_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_OMICRON_PSILI = (GreekExtended.CAPITAL_OMICRON_PSILI,
                             GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=True, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_OMICRON_DASIA = (GreekExtended.CAPITAL_OMICRON_DASIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=True, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_OMICRON_PSILI_VARIA = (GreekExtended.CAPITAL_OMICRON_PSILI_VARIA,
                                   GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=True, dasia=False,
                                              ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                              dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMICRON_DASIA_VARIA = (GreekExtended.CAPITAL_OMICRON_DASIA_VARIA,
                                   GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=True,
                                              ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                              dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMICRON_PSILI_OXIA = (GreekExtended.CAPITAL_OMICRON_PSILI_OXIA,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=True, dasia=False,
                                             ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                             dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMICRON_DASIA_OXIA = (GreekExtended.CAPITAL_OMICRON_DASIA_OXIA,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=True,
                                             ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                             dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_PSILI = (GreekExtended.SMALL_UPSILON_PSILI,
                           GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=True, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_UPSILON_DASIA = (GreekExtended.SMALL_UPSILON_DASIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_UPSILON_PSILI_VARIA = (GreekExtended.SMALL_UPSILON_PSILI_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=True, dasia=False,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_DASIA_VARIA = (GreekExtended.SMALL_UPSILON_DASIA_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=True,
                                            ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_PSILI_OXIA = (GreekExtended.SMALL_UPSILON_PSILI_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    SMALL_UPSILON_DASIA_OXIA = (GreekExtended.SMALL_UPSILON_DASIA_OXIA,
                                GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    SMALL_UPSILON_PSILI_PERISPOMENI = (GreekExtended.SMALL_UPSILON_PSILI_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=True, dasia=False,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_DASIA_PERISPOMENI = (GreekExtended.SMALL_UPSILON_DASIA_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=True,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    CAPITAL_UPSILON_DASIA = (GreekExtended.CAPITAL_UPSILON_DASIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=True, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_UPSILON_DASIA_VARIA = (GreekExtended.CAPITAL_UPSILON_DASIA_VARIA,
                                   GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=True,
                                              ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                              dialytika=False, vrachy=False, macron=False))
    CAPITAL_UPSILON_DASIA_OXIA = (GreekExtended.CAPITAL_UPSILON_DASIA_OXIA,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=True,
                                             ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                             dialytika=False, vrachy=False, macron=False))
    CAPITAL_UPSILON_DASIA_PERISPOMENI = (GreekExtended.CAPITAL_UPSILON_DASIA_PERISPOMENI,
                                         GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=True,
                                                    ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                    dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_PSILI = (GreekExtended.SMALL_OMEGA_PSILI,
                         GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_OMEGA_DASIA = (GreekExtended.SMALL_OMEGA_DASIA,
                         GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_OMEGA_PSILI_VARIA = (GreekExtended.SMALL_OMEGA_PSILI_VARIA,
                               GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_OMEGA_DASIA_VARIA = (GreekExtended.SMALL_OMEGA_DASIA_VARIA,
                               GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                          varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_OMEGA_PSILI_OXIA = (GreekExtended.SMALL_OMEGA_PSILI_OXIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_OMEGA_DASIA_OXIA = (GreekExtended.SMALL_OMEGA_DASIA_OXIA,
                              GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                         varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_OMEGA_PSILI_PERISPOMENI = (GreekExtended.SMALL_OMEGA_PSILI_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_DASIA_PERISPOMENI = (GreekExtended.SMALL_OMEGA_DASIA_PERISPOMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True,
                                                ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_PSILI = (GreekExtended.CAPITAL_OMEGA_PSILI,
                           GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_OMEGA_DASIA = (GreekExtended.CAPITAL_OMEGA_DASIA,
                           GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_OMEGA_PSILI_VARIA = (GreekExtended.CAPITAL_OMEGA_PSILI_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                            varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    CAPITAL_OMEGA_DASIA_VARIA = (GreekExtended.CAPITAL_OMEGA_DASIA_VARIA,
                                 GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                            varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    CAPITAL_OMEGA_PSILI_OXIA = (GreekExtended.CAPITAL_OMEGA_PSILI_OXIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_OMEGA_DASIA_OXIA = (GreekExtended.CAPITAL_OMEGA_DASIA_OXIA,
                                GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True, ypogegrammeni=False,
                                           varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                           macron=False))
    CAPITAL_OMEGA_PSILI_PERISPOMENI = (GreekExtended.CAPITAL_OMEGA_PSILI_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_DASIA_PERISPOMENI = (GreekExtended.CAPITAL_OMEGA_DASIA_PERISPOMENI,
                                       GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True,
                                                  ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_VARIA = (GreekExtended.SMALL_ALPHA_VARIA,
                         GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_ALPHA_OXIA = (GreekExtended.SMALL_ALPHA_OXIA,
                        GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                   varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_EPSILON_VARIA = (GreekExtended.SMALL_EPSILON_VARIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_EPSILON_OXIA = (GreekExtended.SMALL_EPSILON_OXIA,
                          GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    SMALL_ETA_VARIA = (GreekExtended.SMALL_ETA_VARIA,
                       GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=False, varia=True,
                                  oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_OXIA = (GreekExtended.SMALL_ETA_OXIA,
                      GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=False, varia=False,
                                 oxia=True, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_IOTA_VARIA = (GreekExtended.SMALL_IOTA_VARIA,
                        GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                   varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_IOTA_OXIA = (GreekExtended.SMALL_IOTA_OXIA,
                       GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                  varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                  macron=False))
    SMALL_OMICRON_VARIA = (GreekExtended.SMALL_OMICRON_VARIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_OMICRON_OXIA = (GreekExtended.SMALL_OMICRON_OXIA,
                          GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    SMALL_UPSILON_VARIA = (GreekExtended.SMALL_UPSILON_VARIA,
                           GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_UPSILON_OXIA = (GreekExtended.SMALL_UPSILON_OXIA,
                          GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    SMALL_OMEGA_VARIA = (GreekExtended.SMALL_OMEGA_VARIA,
                         GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_OMEGA_OXIA = (GreekExtended.SMALL_OMEGA_OXIA,
                        GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                   varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_ALPHA_PSILI_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_PSILI_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False,
                                                  ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_DASIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_DASIA_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True,
                                                  ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_PSILI_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_PSILI_VARIA_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False,
                                                        ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_DASIA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_DASIA_VARIA_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True,
                                                        ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_PSILI_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_PSILI_OXIA_YPOGEGRAMMENI,
                                            GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False,
                                                       ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                       dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_DASIA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_DASIA_OXIA_YPOGEGRAMMENI,
                                            GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True,
                                                       ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                       dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_PSILI_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_PSILI_PERISPOMENI_YPOGEGRAMMENI,
                                                   GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=True, dasia=False,
                                                              ypogegrammeni=True, varia=False, oxia=False,
                                                              perispomeni=True, dialytika=False, vrachy=False,
                                                              macron=False))
    SMALL_ALPHA_DASIA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
                                                   GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=True,
                                                              ypogegrammeni=True, varia=False, oxia=False,
                                                              perispomeni=True, dialytika=False, vrachy=False,
                                                              macron=False))
    CAPITAL_ALPHA_PSILI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_PSILI_PROSGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False,
                                                     ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_DASIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_DASIA_PROSGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True,
                                                     ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_PSILI_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_PSILI_VARIA_PROSGEGRAMMENI,
                                                GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False,
                                                           ypogegrammeni=True, varia=True, oxia=False,
                                                           perispomeni=False, dialytika=False, vrachy=False,
                                                           macron=False))
    CAPITAL_ALPHA_DASIA_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_DASIA_VARIA_PROSGEGRAMMENI,
                                                GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True,
                                                           ypogegrammeni=True, varia=True, oxia=False,
                                                           perispomeni=False, dialytika=False, vrachy=False,
                                                           macron=False))
    CAPITAL_ALPHA_PSILI_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_PSILI_OXIA_PROSGEGRAMMENI,
                                               GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False,
                                                          ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                          dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_DASIA_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_DASIA_OXIA_PROSGEGRAMMENI,
                                               GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True,
                                                          ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                          dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_PSILI_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_PSILI_PERISPOMENI_PROSGEGRAMMENI,
                                                      GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=True, dasia=False,
                                                                 ypogegrammeni=True, varia=False, oxia=False,
                                                                 perispomeni=True, dialytika=False, vrachy=False,
                                                                 macron=False))
    CAPITAL_ALPHA_DASIA_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_DASIA_PERISPOMENI_PROSGEGRAMMENI,
                                                      GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=True,
                                                                 ypogegrammeni=True, varia=False, oxia=False,
                                                                 perispomeni=True, dialytika=False, vrachy=False,
                                                                 macron=False))
    SMALL_ETA_PSILI_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_PSILI_YPOGEGRAMMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False, ypogegrammeni=True,
                                                varia=False, oxia=False, perispomeni=False, dialytika=False,
                                                vrachy=False, macron=False))
    SMALL_ETA_DASIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_DASIA_YPOGEGRAMMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True, ypogegrammeni=True,
                                                varia=False, oxia=False, perispomeni=False, dialytika=False,
                                                vrachy=False, macron=False))
    SMALL_ETA_PSILI_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_PSILI_VARIA_YPOGEGRAMMENI,
                                           GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False,
                                                      ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                      dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_DASIA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_DASIA_VARIA_YPOGEGRAMMENI,
                                           GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True,
                                                      ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                      dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_PSILI_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_PSILI_OXIA_YPOGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False,
                                                     ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_DASIA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_DASIA_OXIA_YPOGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True,
                                                     ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_PSILI_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_PSILI_PERISPOMENI_YPOGEGRAMMENI,
                                                 GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=True, dasia=False,
                                                            ypogegrammeni=True, varia=False, oxia=False,
                                                            perispomeni=True, dialytika=False, vrachy=False,
                                                            macron=False))
    SMALL_ETA_DASIA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
                                                 GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=True,
                                                            ypogegrammeni=True, varia=False, oxia=False,
                                                            perispomeni=True, dialytika=False, vrachy=False,
                                                            macron=False))
    CAPITAL_ETA_PSILI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_PSILI_PROSGEGRAMMENI,
                                        GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False,
                                                   ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                   dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_DASIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_DASIA_PROSGEGRAMMENI,
                                        GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True,
                                                   ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                   dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_PSILI_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_PSILI_VARIA_PROSGEGRAMMENI,
                                              GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False,
                                                         ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                         dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_DASIA_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_DASIA_VARIA_PROSGEGRAMMENI,
                                              GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True,
                                                         ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                         dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_PSILI_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_PSILI_OXIA_PROSGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False,
                                                        ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_DASIA_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_DASIA_OXIA_PROSGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True,
                                                        ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    CAPITAL_ETA_PSILI_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_PSILI_PERISPOMENI_PROSGEGRAMMENI,
                                                    GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=True, dasia=False,
                                                               ypogegrammeni=True, varia=False, oxia=False,
                                                               perispomeni=True, dialytika=False, vrachy=False,
                                                               macron=False))
    CAPITAL_ETA_DASIA_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_DASIA_PERISPOMENI_PROSGEGRAMMENI,
                                                    GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=True,
                                                               ypogegrammeni=True, varia=False, oxia=False,
                                                               perispomeni=True, dialytika=False, vrachy=False,
                                                               macron=False))
    SMALL_OMEGA_PSILI_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_PSILI_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False,
                                                  ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_DASIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_DASIA_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True,
                                                  ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_PSILI_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_PSILI_VARIA_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False,
                                                        ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_DASIA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_DASIA_VARIA_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True,
                                                        ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                        dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_PSILI_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_PSILI_OXIA_YPOGEGRAMMENI,
                                            GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False,
                                                       ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                       dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_DASIA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_DASIA_OXIA_YPOGEGRAMMENI,
                                            GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True,
                                                       ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                       dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_PSILI_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_PSILI_PERISPOMENI_YPOGEGRAMMENI,
                                                   GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=True, dasia=False,
                                                              ypogegrammeni=True, varia=False, oxia=False,
                                                              perispomeni=True, dialytika=False, vrachy=False,
                                                              macron=False))
    SMALL_OMEGA_DASIA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
                                                   GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=True,
                                                              ypogegrammeni=True, varia=False, oxia=False,
                                                              perispomeni=True, dialytika=False, vrachy=False,
                                                              macron=False))
    CAPITAL_OMEGA_PSILI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_PSILI_PROSGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False,
                                                     ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_DASIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_DASIA_PROSGEGRAMMENI,
                                          GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True,
                                                     ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                                     dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_PSILI_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_PSILI_VARIA_PROSGEGRAMMENI,
                                                GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False,
                                                           ypogegrammeni=True, varia=True, oxia=False,
                                                           perispomeni=False, dialytika=False, vrachy=False,
                                                           macron=False))
    CAPITAL_OMEGA_DASIA_VARIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_DASIA_VARIA_PROSGEGRAMMENI,
                                                GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True,
                                                           ypogegrammeni=True, varia=True, oxia=False,
                                                           perispomeni=False, dialytika=False, vrachy=False,
                                                           macron=False))
    CAPITAL_OMEGA_PSILI_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_PSILI_OXIA_PROSGEGRAMMENI,
                                               GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False,
                                                          ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                          dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_DASIA_OXIA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_DASIA_OXIA_PROSGEGRAMMENI,
                                               GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True,
                                                          ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                          dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMEGA_PSILI_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_PSILI_PERISPOMENI_PROSGEGRAMMENI,
                                                      GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=True, dasia=False,
                                                                 ypogegrammeni=True, varia=False, oxia=False,
                                                                 perispomeni=True, dialytika=False, vrachy=False,
                                                                 macron=False))
    CAPITAL_OMEGA_DASIA_PERISPOMENI_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_DASIA_PERISPOMENI_PROSGEGRAMMENI,
                                                      GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=True,
                                                                 ypogegrammeni=True, varia=False, oxia=False,
                                                                 perispomeni=True, dialytika=False, vrachy=False,
                                                                 macron=False))
    SMALL_ALPHA_VRACHY = (GreekExtended.SMALL_ALPHA_VRACHY,
                          GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                     macron=False))
    SMALL_ALPHA_MACRON = (GreekExtended.SMALL_ALPHA_MACRON,
                          GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=True))
    SMALL_ALPHA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_VARIA_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False,
                                                  ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_YPOGEGRAMMENI,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=True,
                                            varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    SMALL_ALPHA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_OXIA_YPOGEGRAMMENI,
                                      GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False,
                                                 ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                 dialytika=False, vrachy=False, macron=False))
    SMALL_ALPHA_PERISPOMENI = (GreekExtended.SMALL_ALPHA_PERISPOMENI,
                               GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                          varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_ALPHA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ALPHA_PERISPOMENI_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False,
                                                        ypogegrammeni=True, varia=False, oxia=False, perispomeni=True,
                                                        dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_VRACHY = (GreekExtended.CAPITAL_ALPHA_VRACHY,
                            GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                       macron=False))
    CAPITAL_ALPHA_MACRON = (GreekExtended.CAPITAL_ALPHA_MACRON,
                            GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=True))
    CAPITAL_ALPHA_VARIA = (GreekExtended.CAPITAL_ALPHA_VARIA,
                           GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_ALPHA_OXIA = (GreekExtended.CAPITAL_ALPHA_OXIA,
                          GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_ALPHA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ALPHA_PROSGEGRAMMENI,
                                    GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False,
                                               ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                               dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_VARIA_YPOGEGRAMMENI,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False,
                                                ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                dialytika=False, vrachy=False, macron=False))
    SMALL_ETA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_YPOGEGRAMMENI,
                               GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=True,
                                          varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_ETA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_OXIA_YPOGEGRAMMENI,
                                    GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=True,
                                               varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                               macron=False))
    SMALL_ETA_PERISPOMENI = (GreekExtended.SMALL_ETA_PERISPOMENI,
                             GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                        macron=False))
    SMALL_ETA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_ETA_PERISPOMENI_YPOGEGRAMMENI,
                                           GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False,
                                                      ypogegrammeni=True, varia=False, oxia=False, perispomeni=True,
                                                      dialytika=False, vrachy=False, macron=False))
    CAPITAL_EPSILON_VARIA = (GreekExtended.CAPITAL_EPSILON_VARIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_EPSILON_OXIA = (GreekExtended.CAPITAL_EPSILON_OXIA,
                            GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=False))
    CAPITAL_ETA_VARIA = (GreekExtended.CAPITAL_ETA_VARIA,
                         GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    CAPITAL_ETA_OXIA = (GreekExtended.CAPITAL_ETA_OXIA,
                        GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=False, ypogegrammeni=False,
                                   varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    CAPITAL_ETA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_ETA_PROSGEGRAMMENI,
                                  GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=False, ypogegrammeni=True,
                                             varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                             macron=False))
    SMALL_IOTA_VRACHY = (GreekExtended.SMALL_IOTA_VRACHY,
                         GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                    macron=False))
    SMALL_IOTA_MACRON = (GreekExtended.SMALL_IOTA_MACRON,
                         GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=True))
    SMALL_IOTA_DIALYTIKA_VARIA = (GreekExtended.SMALL_IOTA_DIALYTIKA_VARIA,
                                  GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                             varia=True, oxia=False, perispomeni=False, dialytika=True, vrachy=False,
                                             macron=False))
    SMALL_IOTA_DIALYTIKA_OXIA = (GreekExtended.SMALL_IOTA_DIALYTIKA_OXIA,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                            varia=False, oxia=True, perispomeni=False, dialytika=True, vrachy=False,
                                            macron=False))
    SMALL_IOTA_PERISPOMENI = (GreekExtended.SMALL_IOTA_PERISPOMENI,
                              GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                         macron=False))
    SMALL_IOTA_DIALYTIKA_PERISPOMENI = (GreekExtended.SMALL_IOTA_DIALYTIKA_PERISPOMENI,
                                        GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False,
                                                   ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                   dialytika=True, vrachy=False, macron=False))
    CAPITAL_IOTA_VRACHY = (GreekExtended.CAPITAL_IOTA_VRACHY,
                           GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                      macron=False))
    CAPITAL_IOTA_MACRON = (GreekExtended.CAPITAL_IOTA_MACRON,
                           GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=True))
    CAPITAL_IOTA_VARIA = (GreekExtended.CAPITAL_IOTA_VARIA,
                          GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_IOTA_OXIA = (GreekExtended.CAPITAL_IOTA_OXIA,
                         GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_UPSILON_VRACHY = (GreekExtended.SMALL_UPSILON_VRACHY,
                            GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                       macron=False))
    SMALL_UPSILON_MACRON = (GreekExtended.SMALL_UPSILON_MACRON,
                            GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=True))
    SMALL_UPSILON_DIALYTIKA_VARIA = (GreekExtended.SMALL_UPSILON_DIALYTIKA_VARIA,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False,
                                                ypogegrammeni=False, varia=True, oxia=False, perispomeni=False,
                                                dialytika=True, vrachy=False, macron=False))
    SMALL_UPSILON_DIALYTIKA_OXIA = (GreekExtended.SMALL_UPSILON_DIALYTIKA_OXIA,
                                    GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False,
                                               ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                               dialytika=True, vrachy=False, macron=False))
    SMALL_RHO_PSILI = (GreekExtended.SMALL_RHO_PSILI,
                       GreekGlyph(ch=GreekAlphabet.LOWER_RHO, psili=True, dasia=False, ypogegrammeni=False, varia=False,
                                  oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_RHO_DASIA = (GreekExtended.SMALL_RHO_DASIA,
                       GreekGlyph(ch=GreekAlphabet.LOWER_RHO, psili=False, dasia=True, ypogegrammeni=False, varia=False,
                                  oxia=False, perispomeni=False, dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_PERISPOMENI = (GreekExtended.SMALL_UPSILON_PERISPOMENI,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False,
                                            ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                            dialytika=False, vrachy=False, macron=False))
    SMALL_UPSILON_DIALYTIKA_PERISPOMENI = (GreekExtended.SMALL_UPSILON_DIALYTIKA_PERISPOMENI,
                                           GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False,
                                                      ypogegrammeni=False, varia=False, oxia=False, perispomeni=True,
                                                      dialytika=True, vrachy=False, macron=False))
    CAPITAL_UPSILON_VRACHY = (GreekExtended.CAPITAL_UPSILON_VRACHY,
                              GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=True,
                                         macron=False))
    CAPITAL_UPSILON_MACRON = (GreekExtended.CAPITAL_UPSILON_MACRON,
                              GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                         macron=True))
    CAPITAL_UPSILON_VARIA = (GreekExtended.CAPITAL_UPSILON_VARIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_UPSILON_OXIA = (GreekExtended.CAPITAL_UPSILON_OXIA,
                            GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=False))
    CAPITAL_RHO_DASIA = (GreekExtended.CAPITAL_RHO_DASIA,
                         GreekGlyph(ch=GreekAlphabet.UPPER_RHO, psili=False, dasia=True, ypogegrammeni=False,
                                    varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_OMEGA_VARIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_VARIA_YPOGEGRAMMENI,
                                       GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False,
                                                  ypogegrammeni=True, varia=True, oxia=False, perispomeni=False,
                                                  dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_YPOGEGRAMMENI,
                                 GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=True,
                                            varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                            macron=False))
    SMALL_OMEGA_OXIA_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_OXIA_YPOGEGRAMMENI,
                                      GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False,
                                                 ypogegrammeni=True, varia=False, oxia=True, perispomeni=False,
                                                 dialytika=False, vrachy=False, macron=False))
    SMALL_OMEGA_PERISPOMENI = (GreekExtended.SMALL_OMEGA_PERISPOMENI,
                               GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                          varia=False, oxia=False, perispomeni=True, dialytika=False, vrachy=False,
                                          macron=False))
    SMALL_OMEGA_PERISPOMENI_YPOGEGRAMMENI = (GreekExtended.SMALL_OMEGA_PERISPOMENI_YPOGEGRAMMENI,
                                             GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False,
                                                        ypogegrammeni=True, varia=False, oxia=False, perispomeni=True,
                                                        dialytika=False, vrachy=False, macron=False))
    CAPITAL_OMICRON_VARIA = (GreekExtended.CAPITAL_OMICRON_VARIA,
                             GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_OMICRON_OXIA = (GreekExtended.CAPITAL_OMICRON_OXIA,
                            GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                       macron=False))
    CAPITAL_OMEGA_VARIA = (GreekExtended.CAPITAL_OMEGA_VARIA,
                           GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=True, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_OMEGA_OXIA = (GreekExtended.CAPITAL_OMEGA_OXIA,
                          GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_OMEGA_PROSGEGRAMMENI = (GreekExtended.CAPITAL_OMEGA_PROSGEGRAMMENI,
                                    GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=False,
                                               ypogegrammeni=True, varia=False, oxia=False, perispomeni=False,
                                               dialytika=False, vrachy=False, macron=False))
    CAPITAL_ALPHA_TONOS = (GreekMidway.CAPITAL_ALPHA_TONOS,
                           GreekGlyph(ch=GreekAlphabet.UPPER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    CAPITAL_EPSILON_TONOS = (GreekMidway.CAPITAL_EPSILON_TONOS,
                             GreekGlyph(ch=GreekAlphabet.UPPER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_ETA_TONOS = (GreekMidway.CAPITAL_ETA_TONOS,
                         GreekGlyph(ch=GreekAlphabet.UPPER_ETA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    CAPITAL_IOTA_TONOS = (GreekMidway.CAPITAL_IOTA_TONOS,
                          GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                     varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                     macron=False))
    CAPITAL_OMICRON_TONOS = (GreekMidway.CAPITAL_OMICRON_TONOS,
                             GreekGlyph(ch=GreekAlphabet.UPPER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_UPSILON_TONOS = (GreekMidway.CAPITAL_UPSILON_TONOS,
                             GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                        varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                        macron=False))
    CAPITAL_OMEGA_TONOS = (GreekMidway.CAPITAL_OMEGA_TONOS,
                           GreekGlyph(ch=GreekAlphabet.UPPER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_IOTA_DIALYTIKA_TONOS = (GreekMidway.SMALL_IOTA_DIALYTIKA_TONOS,
                                  GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                             varia=False, oxia=True, perispomeni=False, dialytika=True, vrachy=False,
                                             macron=False))
    CAPITAL_IOTA_DIALYTIKA = (GreekMidway.CAPITAL_IOTA_DIALYTIKA,
                              GreekGlyph(ch=GreekAlphabet.UPPER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                         varia=False, oxia=False, perispomeni=False, dialytika=True, vrachy=False,
                                         macron=False))
    CAPITAL_UPSILON_DIALYTIKA = (GreekMidway.CAPITAL_UPSILON_DIALYTIKA,
                                 GreekGlyph(ch=GreekAlphabet.UPPER_UPSILON, psili=False, dasia=False,
                                            ypogegrammeni=False, varia=False, oxia=False, perispomeni=False,
                                            dialytika=True, vrachy=False, macron=False))
    SMALL_ALPHA_TONOS = (GreekMidway.SMALL_ALPHA_TONOS,
                         GreekGlyph(ch=GreekAlphabet.LOWER_ALPHA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))
    SMALL_EPSILON_TONOS = (GreekMidway.SMALL_EPSILON_TONOS,
                           GreekGlyph(ch=GreekAlphabet.LOWER_EPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_ETA_TONOS = (GreekMidway.SMALL_ETA_TONOS,
                       GreekGlyph(ch=GreekAlphabet.LOWER_ETA, psili=False, dasia=False, ypogegrammeni=False,
                                  varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                  macron=False))
    SMALL_IOTA_TONOS = (GreekMidway.SMALL_IOTA_TONOS,
                        GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                   varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                   macron=False))
    SMALL_UPSILON_DIALYTIKA_TONOS = (GreekMidway.SMALL_UPSILON_DIALYTIKA_TONOS,
                                     GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False,
                                                ypogegrammeni=False, varia=False, oxia=True, perispomeni=False,
                                                dialytika=True, vrachy=False, macron=False))
    SMALL_IOTA_DIALYTIKA = (GreekMidway.SMALL_IOTA_DIALYTIKA,
                            GreekGlyph(ch=GreekAlphabet.LOWER_IOTA, psili=False, dasia=False, ypogegrammeni=False,
                                       varia=False, oxia=False, perispomeni=False, dialytika=True, vrachy=False,
                                       macron=False))
    SMALL_UPSILON_DIALYTIKA = (GreekMidway.SMALL_UPSILON_DIALYTIKA,
                               GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                          varia=False, oxia=False, perispomeni=False, dialytika=True, vrachy=False,
                                          macron=False))
    SMALL_OMICRON_TONOS = (GreekMidway.SMALL_OMICRON_TONOS,
                           GreekGlyph(ch=GreekAlphabet.LOWER_OMICRON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_UPSILON_TONOS = (GreekMidway.SMALL_UPSILON_TONOS,
                           GreekGlyph(ch=GreekAlphabet.LOWER_UPSILON, psili=False, dasia=False, ypogegrammeni=False,
                                      varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                      macron=False))
    SMALL_OMEGA_TONOS = (GreekMidway.SMALL_OMEGA_TONOS,
                         GreekGlyph(ch=GreekAlphabet.LOWER_OMEGA, psili=False, dasia=False, ypogegrammeni=False,
                                    varia=False, oxia=True, perispomeni=False, dialytika=False, vrachy=False,
                                    macron=False))

    ALL_UTF_LETTERS = (
        APOSTROPHE, HYPHEN_MINUS, LOWER_ZETA, LOWER_ALPHA, UPPER_EPSILON, LOWER_DELTA, LOWER_ETA,
        UPPER_CHI, LOWER_PSI, UPPER_PI, LOWER_GAMMA, LOWER_XI, LOWER_EPSILON, LOWER_CHI, UPPER_DELTA, UPPER_NU,
        UPPER_SIGMA, UPPER_OMICRON, LOWER_PHI, LOWER_PI, UPPER_GAMMA, UPPER_ETA, LOWER_SIGMA, LOWER_LAMDA, LOWER_IOTA,
        UPPER_ZETA, UPPER_LAMDA, UPPER_TAU, LOWER_FINAL_SIGMA, UPPER_ALPHA, LOWER_OMICRON, LOWER_TAU, LOWER_BETA,
        UPPER_RHO, UPPER_OMEGA, LOWER_KAPPA, LOWER_UPSILON, UPPER_PHI, LOWER_NU, DIGAMMA, UPPER_BETA, LOWER_OMEGA,
        UPPER_KAPPA, UPPER_THETA, UPPER_XI, UPPER_IOTA, UPPER_PSI, LOWER_MU, LOWER_DIGAMMA, LOWER_RHO, LOWER_THETA,
        UPPER_UPSILON, UPPER_MU, SMALL_ALPHA_PSILI, SMALL_ALPHA_DASIA, SMALL_ALPHA_PSILI_VARIA,
        SMALL_ALPHA_DASIA_VARIA, SMALL_ALPHA_PSILI_OXIA, SMALL_ALPHA_DASIA_OXIA, SMALL_ALPHA_PSILI_PERISPOMENI,
        SMALL_ALPHA_DASIA_PERISPOMENI, CAPITAL_ALPHA_PSILI, CAPITAL_ALPHA_DASIA, CAPITAL_ALPHA_PSILI_VARIA,
        CAPITAL_ALPHA_DASIA_VARIA, CAPITAL_ALPHA_PSILI_OXIA, CAPITAL_ALPHA_DASIA_OXIA,
        CAPITAL_ALPHA_PSILI_PERISPOMENI, CAPITAL_ALPHA_DASIA_PERISPOMENI, SMALL_EPSILON_PSILI, SMALL_EPSILON_DASIA,
        SMALL_EPSILON_PSILI_VARIA, SMALL_EPSILON_DASIA_VARIA, SMALL_EPSILON_PSILI_OXIA, SMALL_EPSILON_DASIA_OXIA,
        CAPITAL_EPSILON_PSILI, CAPITAL_EPSILON_DASIA, CAPITAL_EPSILON_PSILI_VARIA, CAPITAL_EPSILON_DASIA_VARIA,
        CAPITAL_EPSILON_PSILI_OXIA, CAPITAL_EPSILON_DASIA_OXIA, SMALL_ETA_PSILI, SMALL_ETA_DASIA,
        SMALL_ETA_PSILI_VARIA, SMALL_ETA_DASIA_VARIA, SMALL_ETA_PSILI_OXIA, SMALL_ETA_DASIA_OXIA,
        SMALL_ETA_PSILI_PERISPOMENI, SMALL_ETA_DASIA_PERISPOMENI, CAPITAL_ETA_PSILI, CAPITAL_ETA_DASIA,
        CAPITAL_ETA_PSILI_VARIA, CAPITAL_ETA_DASIA_VARIA, CAPITAL_ETA_PSILI_OXIA, CAPITAL_ETA_DASIA_OXIA,
        CAPITAL_ETA_PSILI_PERISPOMENI, CAPITAL_ETA_DASIA_PERISPOMENI, SMALL_IOTA_PSILI, SMALL_IOTA_DASIA,
        SMALL_IOTA_PSILI_VARIA, SMALL_IOTA_DASIA_VARIA, SMALL_IOTA_PSILI_OXIA, SMALL_IOTA_DASIA_OXIA,
        SMALL_IOTA_PSILI_PERISPOMENI, SMALL_IOTA_DASIA_PERISPOMENI, CAPITAL_IOTA_PSILI, CAPITAL_IOTA_DASIA,
        CAPITAL_IOTA_PSILI_VARIA, CAPITAL_IOTA_DASIA_VARIA, CAPITAL_IOTA_PSILI_OXIA, CAPITAL_IOTA_DASIA_OXIA,
        CAPITAL_IOTA_PSILI_PERISPOMENI, CAPITAL_IOTA_DASIA_PERISPOMENI, SMALL_OMICRON_PSILI, SMALL_OMICRON_DASIA,
        SMALL_OMICRON_PSILI_VARIA, SMALL_OMICRON_DASIA_VARIA, SMALL_OMICRON_PSILI_OXIA, SMALL_OMICRON_DASIA_OXIA,
        CAPITAL_OMICRON_PSILI, CAPITAL_OMICRON_DASIA, CAPITAL_OMICRON_PSILI_VARIA, CAPITAL_OMICRON_DASIA_VARIA,
        CAPITAL_OMICRON_PSILI_OXIA, CAPITAL_OMICRON_DASIA_OXIA, SMALL_UPSILON_PSILI, SMALL_UPSILON_DASIA,
        SMALL_UPSILON_PSILI_VARIA, SMALL_UPSILON_DASIA_VARIA, SMALL_UPSILON_PSILI_OXIA, SMALL_UPSILON_DASIA_OXIA,
        SMALL_UPSILON_PSILI_PERISPOMENI, SMALL_UPSILON_DASIA_PERISPOMENI, CAPITAL_UPSILON_DASIA,
        CAPITAL_UPSILON_DASIA_VARIA, CAPITAL_UPSILON_DASIA_OXIA, CAPITAL_UPSILON_DASIA_PERISPOMENI,
        SMALL_OMEGA_PSILI, SMALL_OMEGA_DASIA, SMALL_OMEGA_PSILI_VARIA, SMALL_OMEGA_DASIA_VARIA,
        SMALL_OMEGA_PSILI_OXIA, SMALL_OMEGA_DASIA_OXIA, SMALL_OMEGA_PSILI_PERISPOMENI, SMALL_OMEGA_DASIA_PERISPOMENI,
        CAPITAL_OMEGA_PSILI, CAPITAL_OMEGA_DASIA, CAPITAL_OMEGA_PSILI_VARIA, CAPITAL_OMEGA_DASIA_VARIA,
        CAPITAL_OMEGA_PSILI_OXIA, CAPITAL_OMEGA_DASIA_OXIA, CAPITAL_OMEGA_PSILI_PERISPOMENI,
        CAPITAL_OMEGA_DASIA_PERISPOMENI, SMALL_ALPHA_VARIA, SMALL_ALPHA_OXIA, SMALL_EPSILON_VARIA, SMALL_EPSILON_OXIA,
        SMALL_ETA_VARIA, SMALL_ETA_OXIA, SMALL_IOTA_VARIA, SMALL_IOTA_OXIA, SMALL_OMICRON_VARIA, SMALL_OMICRON_OXIA,
        SMALL_UPSILON_VARIA, SMALL_UPSILON_OXIA, SMALL_OMEGA_VARIA, SMALL_OMEGA_OXIA, SMALL_ALPHA_PSILI_YPOGEGRAMMENI,
        SMALL_ALPHA_DASIA_YPOGEGRAMMENI, SMALL_ALPHA_PSILI_VARIA_YPOGEGRAMMENI, SMALL_ALPHA_DASIA_VARIA_YPOGEGRAMMENI,
        SMALL_ALPHA_PSILI_OXIA_YPOGEGRAMMENI, SMALL_ALPHA_DASIA_OXIA_YPOGEGRAMMENI,
        SMALL_ALPHA_PSILI_PERISPOMENI_YPOGEGRAMMENI, SMALL_ALPHA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
        CAPITAL_ALPHA_PSILI_PROSGEGRAMMENI, CAPITAL_ALPHA_DASIA_PROSGEGRAMMENI,
        CAPITAL_ALPHA_PSILI_VARIA_PROSGEGRAMMENI, CAPITAL_ALPHA_DASIA_VARIA_PROSGEGRAMMENI,
        CAPITAL_ALPHA_PSILI_OXIA_PROSGEGRAMMENI, CAPITAL_ALPHA_DASIA_OXIA_PROSGEGRAMMENI,
        CAPITAL_ALPHA_PSILI_PERISPOMENI_PROSGEGRAMMENI, CAPITAL_ALPHA_DASIA_PERISPOMENI_PROSGEGRAMMENI,
        SMALL_ETA_PSILI_YPOGEGRAMMENI, SMALL_ETA_DASIA_YPOGEGRAMMENI, SMALL_ETA_PSILI_VARIA_YPOGEGRAMMENI,
        SMALL_ETA_DASIA_VARIA_YPOGEGRAMMENI, SMALL_ETA_PSILI_OXIA_YPOGEGRAMMENI, SMALL_ETA_DASIA_OXIA_YPOGEGRAMMENI,
        SMALL_ETA_PSILI_PERISPOMENI_YPOGEGRAMMENI, SMALL_ETA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
        CAPITAL_ETA_PSILI_PROSGEGRAMMENI, CAPITAL_ETA_DASIA_PROSGEGRAMMENI, CAPITAL_ETA_PSILI_VARIA_PROSGEGRAMMENI,
        CAPITAL_ETA_DASIA_VARIA_PROSGEGRAMMENI, CAPITAL_ETA_PSILI_OXIA_PROSGEGRAMMENI,
        CAPITAL_ETA_DASIA_OXIA_PROSGEGRAMMENI, CAPITAL_ETA_PSILI_PERISPOMENI_PROSGEGRAMMENI,
        CAPITAL_ETA_DASIA_PERISPOMENI_PROSGEGRAMMENI, SMALL_OMEGA_PSILI_YPOGEGRAMMENI,
        SMALL_OMEGA_DASIA_YPOGEGRAMMENI, SMALL_OMEGA_PSILI_VARIA_YPOGEGRAMMENI, SMALL_OMEGA_DASIA_VARIA_YPOGEGRAMMENI,
        SMALL_OMEGA_PSILI_OXIA_YPOGEGRAMMENI, SMALL_OMEGA_DASIA_OXIA_YPOGEGRAMMENI,
        SMALL_OMEGA_PSILI_PERISPOMENI_YPOGEGRAMMENI, SMALL_OMEGA_DASIA_PERISPOMENI_YPOGEGRAMMENI,
        CAPITAL_OMEGA_PSILI_PROSGEGRAMMENI, CAPITAL_OMEGA_DASIA_PROSGEGRAMMENI,
        CAPITAL_OMEGA_PSILI_VARIA_PROSGEGRAMMENI, CAPITAL_OMEGA_DASIA_VARIA_PROSGEGRAMMENI,
        CAPITAL_OMEGA_PSILI_OXIA_PROSGEGRAMMENI, CAPITAL_OMEGA_DASIA_OXIA_PROSGEGRAMMENI,
        CAPITAL_OMEGA_PSILI_PERISPOMENI_PROSGEGRAMMENI, CAPITAL_OMEGA_DASIA_PERISPOMENI_PROSGEGRAMMENI,
        SMALL_ALPHA_VRACHY, SMALL_ALPHA_MACRON, SMALL_ALPHA_VARIA_YPOGEGRAMMENI, SMALL_ALPHA_YPOGEGRAMMENI,
        SMALL_ALPHA_OXIA_YPOGEGRAMMENI, SMALL_ALPHA_PERISPOMENI, SMALL_ALPHA_PERISPOMENI_YPOGEGRAMMENI,
        CAPITAL_ALPHA_VRACHY, CAPITAL_ALPHA_MACRON, CAPITAL_ALPHA_VARIA, CAPITAL_ALPHA_OXIA,
        CAPITAL_ALPHA_PROSGEGRAMMENI, SMALL_ETA_VARIA_YPOGEGRAMMENI, SMALL_ETA_YPOGEGRAMMENI,
        SMALL_ETA_OXIA_YPOGEGRAMMENI, SMALL_ETA_PERISPOMENI, SMALL_ETA_PERISPOMENI_YPOGEGRAMMENI,
        CAPITAL_EPSILON_VARIA, CAPITAL_EPSILON_OXIA, CAPITAL_ETA_VARIA, CAPITAL_ETA_OXIA, CAPITAL_ETA_PROSGEGRAMMENI,
        SMALL_IOTA_VRACHY, SMALL_IOTA_MACRON, SMALL_IOTA_DIALYTIKA_VARIA, SMALL_IOTA_DIALYTIKA_OXIA,
        SMALL_IOTA_PERISPOMENI, SMALL_IOTA_DIALYTIKA_PERISPOMENI, CAPITAL_IOTA_VRACHY, CAPITAL_IOTA_MACRON,
        CAPITAL_IOTA_VARIA, CAPITAL_IOTA_OXIA, SMALL_UPSILON_VRACHY, SMALL_UPSILON_MACRON,
        SMALL_UPSILON_DIALYTIKA_VARIA, SMALL_UPSILON_DIALYTIKA_OXIA, SMALL_RHO_PSILI, SMALL_RHO_DASIA,
        SMALL_UPSILON_PERISPOMENI, SMALL_UPSILON_DIALYTIKA_PERISPOMENI, CAPITAL_UPSILON_VRACHY, CAPITAL_UPSILON_MACRON,
        CAPITAL_UPSILON_VARIA, CAPITAL_UPSILON_OXIA, CAPITAL_RHO_DASIA, SMALL_OMEGA_VARIA_YPOGEGRAMMENI,
        SMALL_OMEGA_YPOGEGRAMMENI, SMALL_OMEGA_OXIA_YPOGEGRAMMENI, SMALL_OMEGA_PERISPOMENI,
        SMALL_OMEGA_PERISPOMENI_YPOGEGRAMMENI, CAPITAL_OMICRON_VARIA, CAPITAL_OMICRON_OXIA, CAPITAL_OMEGA_VARIA,
        CAPITAL_OMEGA_OXIA, CAPITAL_OMEGA_PROSGEGRAMMENI, CAPITAL_ALPHA_TONOS, CAPITAL_EPSILON_TONOS,
        CAPITAL_ETA_TONOS, CAPITAL_IOTA_TONOS, CAPITAL_OMICRON_TONOS, CAPITAL_UPSILON_TONOS, CAPITAL_OMEGA_TONOS,
        SMALL_IOTA_DIALYTIKA_TONOS, CAPITAL_IOTA_DIALYTIKA, CAPITAL_UPSILON_DIALYTIKA, SMALL_ALPHA_TONOS,
        SMALL_EPSILON_TONOS, SMALL_ETA_TONOS, SMALL_IOTA_TONOS, SMALL_UPSILON_DIALYTIKA_TONOS, SMALL_IOTA_DIALYTIKA,
        SMALL_UPSILON_DIALYTIKA, SMALL_OMICRON_TONOS, SMALL_UPSILON_TONOS, SMALL_OMEGA_TONOS
    )

    DEBUG_CIRCLE = (GreekDiacritic.DEBUG_CIRCLE,
                    GreekGlyph(ch=GreekDiacritic.DEBUG_CIRCLE, psili=False, dasia=False, ypogegrammeni=False,
                               varia=False, oxia=False, perispomeni=False, dialytika=False, vrachy=False,
                               macron=False)),

    LEGAL = frozenset(dict(ALL_UTF_LETTERS).values())
