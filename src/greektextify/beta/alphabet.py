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

    UPPER_CASE = '\u002A'

    LATIN_A = '\u0041'
    LATIN_B = '\u0042'
    LATIN_C = '\u0043'
    LATIN_D = '\u0044'
    LATIN_E = '\u0045'
    LATIN_F = '\u0046'
    LATIN_G = '\u0047'
    LATIN_H = '\u0048'
    LATIN_I = '\u0049'
    # LATIN_J = '\u004A'  # Not part of standard.
    LATIN_K = '\u004B'
    LATIN_L = '\u004C'
    LATIN_M = '\u004D'
    LATIN_N = '\u004E'
    LATIN_O = '\u004F'
    LATIN_P = '\u0050'
    LATIN_Q = '\u0051'
    LATIN_R = '\u0052'
    LATIN_S = '\u0053'
    LATIN_T = '\u0054'
    LATIN_U = '\u0055'
    # LATIN_V = '\u0056'  # Skipping Digamma to begin with
    LATIN_W = '\u0057'
    LATIN_X = '\u0058'
    LATIN_Y = '\u0059'
    LATIN_Z = '\u005A'

    NUMBER_1 = '\u0031'
    NUMBER_2 = '\u0032'
    NUMBER_3 = '\u0033'

    LATIN_CHARS = frozenset([
        UPPER_CASE, LATIN_A, LATIN_B, LATIN_C, LATIN_D, LATIN_E, LATIN_F, LATIN_G, LATIN_H, LATIN_I, LATIN_K,
        LATIN_L, LATIN_M, LATIN_N, LATIN_O, LATIN_P, LATIN_Q, LATIN_R, LATIN_S, LATIN_T, LATIN_U, LATIN_W,
        LATIN_X, LATIN_Y, LATIN_Z, NUMBER_1, NUMBER_2, NUMBER_3
    ])

    LATIN_NUMBERS = frozenset([
        NUMBER_1, NUMBER_2, NUMBER_3
    ])

    HYPHEN_MINUS = '\u002D'

    ALPHABET = frozenset(LATIN_CHARS | {HYPHEN_MINUS})

    BETA_LETTERS = {
        LATIN_A: (GreekAlphabet.UPPER_ALPHA, GreekAlphabet.LOWER_ALPHA),
        LATIN_B: (GreekAlphabet.UPPER_BETA, GreekAlphabet.LOWER_BETA),
        LATIN_C: (GreekAlphabet.UPPER_XI, GreekAlphabet.LOWER_XI),
        LATIN_D: (GreekAlphabet.UPPER_DELTA, GreekAlphabet.LOWER_DELTA),
        LATIN_E: (GreekAlphabet.UPPER_EPSILON, GreekAlphabet.LOWER_EPSILON),
        LATIN_F: (GreekAlphabet.UPPER_PHI, GreekAlphabet.LOWER_PHI),
        LATIN_G: (GreekAlphabet.UPPER_GAMMA, GreekAlphabet.LOWER_GAMMA),
        LATIN_H: (GreekAlphabet.UPPER_ETA, GreekAlphabet.LOWER_ETA),
        LATIN_I: (GreekAlphabet.UPPER_IOTA, GreekAlphabet.LOWER_IOTA),
        LATIN_K: (GreekAlphabet.UPPER_KAPPA, GreekAlphabet.LOWER_KAPPA),
        LATIN_L: (GreekAlphabet.UPPER_LAMBDA, GreekAlphabet.LOWER_LAMBDA),
        LATIN_M: (GreekAlphabet.UPPER_MU, GreekAlphabet.LOWER_MU),
        LATIN_N: (GreekAlphabet.UPPER_NU, GreekAlphabet.LOWER_NU),
        LATIN_O: (GreekAlphabet.UPPER_OMICRON, GreekAlphabet.LOWER_OMICRON),
        LATIN_P: (GreekAlphabet.UPPER_PI, GreekAlphabet.LOWER_PI),
        LATIN_Q: (GreekAlphabet.UPPER_THETA, GreekAlphabet.LOWER_THETA),
        LATIN_R: (GreekAlphabet.UPPER_RHO, GreekAlphabet.LOWER_RHO),
        LATIN_S: (GreekAlphabet.UPPER_SIGMA, GreekAlphabet.LOWER_SIGMA),
        LATIN_S + NUMBER_1: (None, GreekAlphabet.LOWER_SIGMA),
        LATIN_S + NUMBER_2: (None, GreekAlphabet.LOWER_SIGMA_FINAL),
        LATIN_T: (GreekAlphabet.UPPER_TAU, GreekAlphabet.LOWER_TAU),
        LATIN_U: (GreekAlphabet.UPPER_UPSILON, GreekAlphabet.LOWER_UPSILON),
        LATIN_W: (GreekAlphabet.UPPER_OMEGA, GreekAlphabet.LOWER_OMEGA),
        LATIN_X: (GreekAlphabet.UPPER_CHI, GreekAlphabet.LOWER_CHI),
        LATIN_Y: (GreekAlphabet.UPPER_PSI, GreekAlphabet.LOWER_PSI),
        LATIN_Z: (GreekAlphabet.UPPER_ZETA, GreekAlphabet.LOWER_ZETA)
    }



