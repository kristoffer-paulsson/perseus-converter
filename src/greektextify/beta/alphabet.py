#
# Copyright (c) 2023 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Betacode latin->koine mapping."""
from greektextify.text.alphabet import GreekAlphabet


class BetaAlphabet(GreekAlphabet):

    UPPER_CASE = ord('\u002A')

    LATIN_A = ord('\u0041')
    LATIN_B = ord('\u0042')
    LATIN_C = ord('\u0043')
    LATIN_D = ord('\u0044')
    LATIN_E = ord('\u0045')
    LATIN_F = ord('\u0046')
    LATIN_G = ord('\u0047')
    LATIN_H = ord('\u0048')
    LATIN_I = ord('\u0049')
    # LATIN_J = ord('\u004A')  # Not part of standard.
    LATIN_K = ord('\u004B')
    LATIN_L = ord('\u004C')
    LATIN_M = ord('\u004D')
    LATIN_N = ord('\u004E')
    LATIN_O = ord('\u004F')
    LATIN_P = ord('\u0050')
    LATIN_Q = ord('\u0051')
    LATIN_R = ord('\u0052')
    LATIN_S = ord('\u0053')
    LATIN_T = ord('\u0054')
    LATIN_U = ord('\u0055')
    LATIN_V = ord('\u0056') # Skipping Digamma to begin with
    LATIN_W = ord('\u0057')
    LATIN_X = ord('\u0058')
    LATIN_Y = ord('\u0059')
    LATIN_Z = ord('\u005A')

    NUMBER_1 = ord('\u0031')
    NUMBER_2 = ord('\u0032')
    NUMBER_3 = ord('\u0033')

    HYPHEN_MINUS = ord('\u002D')

    LATIN_CHARS = frozenset([
        UPPER_CASE, LATIN_A, LATIN_B, LATIN_C, LATIN_D, LATIN_E, LATIN_F, LATIN_G, LATIN_H, LATIN_I, LATIN_K,
        LATIN_L, LATIN_M, LATIN_N, LATIN_O, LATIN_P, LATIN_Q, LATIN_R, LATIN_S, LATIN_T, LATIN_U, LATIN_W,
        LATIN_X, LATIN_Y, LATIN_Z, NUMBER_1, NUMBER_2, NUMBER_3, LATIN_V
    ])

    LATIN_NUMBERS = frozenset([
        NUMBER_1, NUMBER_2, NUMBER_3
    ])

    ALPHABET = frozenset(LATIN_CHARS | {HYPHEN_MINUS})

    BETA_LETTERS = {
        (LATIN_A, ): (GreekAlphabet.UPPER_ALPHA, GreekAlphabet.LOWER_ALPHA),
        (LATIN_B, ): (GreekAlphabet.UPPER_BETA, GreekAlphabet.LOWER_BETA),
        (LATIN_C, ): (GreekAlphabet.UPPER_XI, GreekAlphabet.LOWER_XI),
        (LATIN_D, ): (GreekAlphabet.UPPER_DELTA, GreekAlphabet.LOWER_DELTA),
        (LATIN_E, ): (GreekAlphabet.UPPER_EPSILON, GreekAlphabet.LOWER_EPSILON),
        (LATIN_F, ): (GreekAlphabet.UPPER_PHI, GreekAlphabet.LOWER_PHI),
        (LATIN_G, ): (GreekAlphabet.UPPER_GAMMA, GreekAlphabet.LOWER_GAMMA),
        (LATIN_H, ): (GreekAlphabet.UPPER_ETA, GreekAlphabet.LOWER_ETA),
        (LATIN_I, ): (GreekAlphabet.UPPER_IOTA, GreekAlphabet.LOWER_IOTA),
        (LATIN_K, ): (GreekAlphabet.UPPER_KAPPA, GreekAlphabet.LOWER_KAPPA),
        (LATIN_L, ): (GreekAlphabet.UPPER_LAMDA, GreekAlphabet.LOWER_LAMDA),
        (LATIN_M, ): (GreekAlphabet.UPPER_MU, GreekAlphabet.LOWER_MU),
        (LATIN_N, ): (GreekAlphabet.UPPER_NU, GreekAlphabet.LOWER_NU),
        (LATIN_O, ): (GreekAlphabet.UPPER_OMICRON, GreekAlphabet.LOWER_OMICRON),
        (LATIN_P, ): (GreekAlphabet.UPPER_PI, GreekAlphabet.LOWER_PI),
        (LATIN_Q, ): (GreekAlphabet.UPPER_THETA, GreekAlphabet.LOWER_THETA),
        (LATIN_R, ): (GreekAlphabet.UPPER_RHO, GreekAlphabet.LOWER_RHO),
        (LATIN_S, ): (GreekAlphabet.UPPER_SIGMA, GreekAlphabet.LOWER_SIGMA),
        (LATIN_S, NUMBER_1): (None, GreekAlphabet.LOWER_SIGMA),
        (LATIN_S, NUMBER_2): (None, GreekAlphabet.LOWER_FINAL_SIGMA),
        (LATIN_S, NUMBER_3): (GreekAlphabet.UPPER_LUNATE, GreekAlphabet.LOWER_LUNATE),
        (LATIN_T, ): (GreekAlphabet.UPPER_TAU, GreekAlphabet.LOWER_TAU),
        (LATIN_U, ): (GreekAlphabet.UPPER_UPSILON, GreekAlphabet.LOWER_UPSILON),
        (LATIN_W, ): (GreekAlphabet.UPPER_OMEGA, GreekAlphabet.LOWER_OMEGA),
        (LATIN_X, ): (GreekAlphabet.UPPER_CHI, GreekAlphabet.LOWER_CHI),
        (LATIN_Y, ): (GreekAlphabet.UPPER_PSI, GreekAlphabet.LOWER_PSI),
        (LATIN_Z, ): (GreekAlphabet.UPPER_ZETA, GreekAlphabet.LOWER_ZETA),
        (LATIN_V, ): (GreekAlphabet.DIGAMMA, GreekAlphabet.LOWER_DIGAMMA)
    }



