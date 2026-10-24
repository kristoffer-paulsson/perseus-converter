#
# Copyright (c) 2022 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""The Greek alphabet as described in:

Smyth, Herbert Weir. 1920. A Greek Grammar for Colleges. American Book Company.
https://www.unicode.org/charts/PDF/U0300.pdf
https://www.unicode.org/charts/PDF/U0370.pdf
https://www.unicode.org/charts/PDF/U1F00.pdf

Following also has to be considered.
https://unicode.org/charts/PDF/U02B0.pdf
"""


class GreekAlphabet:
    """Greek alphabet according to Smyth grammar 1.1.1."""

    LOWER_ALPHA = ord('\u03B1')
    LOWER_BETA = ord('\u03B2')
    LOWER_GAMMA = ord('\u03B3')
    LOWER_DELTA = ord('\u03B4')
    LOWER_EPSILON = ord('\u03B5')
    LOWER_ZETA = ord('\u03B6')
    LOWER_ETA = ord('\u03B7')
    LOWER_THETA = ord('\u03B8')
    LOWER_IOTA = ord('\u03B9')
    LOWER_KAPPA = ord('\u03BA')
    LOWER_LAMDA = ord('\u03BB')
    LOWER_MU = ord('\u03BC')
    LOWER_NU = ord('\u03BD')
    LOWER_XI = ord('\u03BE')
    LOWER_OMICRON = ord('\u03BF')
    LOWER_PI = ord('\u03C0')
    LOWER_RHO = ord('\u03C1')
    LOWER_FINAL_SIGMA = ord('\u03C2')
    LOWER_SIGMA = ord('\u03C3')
    LOWER_TAU = ord('\u03C4')
    LOWER_UPSILON = ord('\u03C5')
    LOWER_PHI = ord('\u03C6')
    LOWER_CHI = ord('\u03C7')
    LOWER_PSI = ord('\u03C8')
    LOWER_OMEGA = ord('\u03C9')

    LOWER_DIGAMMA = ord('\u03DD')
    LOWER_LUNATE = ord('\u03F2')


    CASE_LOWER = frozenset([
        LOWER_ALPHA, LOWER_BETA, LOWER_GAMMA, LOWER_DELTA, LOWER_EPSILON, LOWER_ZETA, LOWER_ETA, LOWER_THETA,
        LOWER_IOTA, LOWER_KAPPA, LOWER_LAMDA, LOWER_MU, LOWER_NU, LOWER_XI, LOWER_OMICRON, LOWER_PI, LOWER_RHO,
        LOWER_FINAL_SIGMA, LOWER_SIGMA, LOWER_TAU, LOWER_UPSILON, LOWER_PHI, LOWER_CHI, LOWER_PSI, LOWER_OMEGA,

        LOWER_DIGAMMA, LOWER_LUNATE
    ])

    UPPER_ALPHA = ord('\u0391')
    UPPER_BETA = ord('\u0392')
    UPPER_GAMMA = ord('\u0393')
    UPPER_DELTA = ord('\u0394')
    UPPER_EPSILON = ord('\u0395')
    UPPER_ZETA = ord('\u0396')
    UPPER_ETA = ord('\u0397')
    UPPER_THETA = ord('\u0398')
    UPPER_IOTA = ord('\u0399')
    UPPER_KAPPA = ord('\u039A')
    UPPER_LAMDA = ord('\u039B')
    UPPER_MU = ord('\u039C')
    UPPER_NU = ord('\u039D')
    UPPER_XI = ord('\u039E')
    UPPER_OMICRON = ord('\u039F')
    UPPER_PI = ord('\u03A0')
    UPPER_RHO = ord('\u03A1')
    UPPER_SIGMA = ord('\u03A3')
    UPPER_TAU = ord('\u03A4')
    UPPER_UPSILON = ord('\u03A5')
    UPPER_PHI = ord('\u03A6')
    UPPER_CHI = ord('\u03A7')
    UPPER_PSI = ord('\u03A8')
    UPPER_OMEGA = ord('\u03A9')

    DIGAMMA = ord('\u03DC')
    UPPER_LUNATE = ord('\u03F9')

    CASE_UPPER = frozenset([
        UPPER_ALPHA, UPPER_BETA, UPPER_GAMMA, UPPER_DELTA, UPPER_EPSILON, UPPER_ZETA, UPPER_ETA, UPPER_THETA,
        UPPER_IOTA, UPPER_KAPPA, UPPER_LAMDA, UPPER_MU, UPPER_NU, UPPER_XI, UPPER_OMICRON, UPPER_PI, UPPER_RHO,
        UPPER_SIGMA, UPPER_TAU, UPPER_UPSILON, UPPER_PHI, UPPER_CHI, UPPER_PSI, UPPER_OMEGA,

        DIGAMMA, UPPER_LUNATE
    ])

    HYPHEN_MINUS = ord('\u002D')

    ALPHABET = frozenset(CASE_LOWER | CASE_UPPER | {HYPHEN_MINUS})

    FROM_LOWER = {
        LOWER_ALPHA: UPPER_ALPHA,
        LOWER_BETA: UPPER_BETA,
        LOWER_GAMMA: UPPER_GAMMA,
        LOWER_DELTA: UPPER_DELTA,
        LOWER_EPSILON: UPPER_EPSILON,
        LOWER_ZETA: UPPER_ZETA,
        LOWER_ETA: UPPER_ETA,
        LOWER_THETA: UPPER_THETA,
        LOWER_IOTA: UPPER_IOTA,
        LOWER_KAPPA: UPPER_KAPPA,
        LOWER_LAMDA: UPPER_LAMDA,
        LOWER_MU: UPPER_MU,
        LOWER_NU: UPPER_NU,
        LOWER_XI: UPPER_XI,
        LOWER_OMICRON: UPPER_OMICRON,
        LOWER_PI: UPPER_PI,
        LOWER_RHO: UPPER_RHO,
        LOWER_SIGMA: UPPER_SIGMA,
        LOWER_FINAL_SIGMA: UPPER_SIGMA,
        LOWER_TAU: UPPER_TAU,
        LOWER_UPSILON: UPPER_UPSILON,
        LOWER_PHI: UPPER_PHI,
        LOWER_CHI: UPPER_CHI,
        LOWER_PSI: UPPER_PSI,
        LOWER_OMEGA: UPPER_OMEGA,
        LOWER_DIGAMMA: DIGAMMA,
        LOWER_LUNATE: UPPER_LUNATE
    }

    FROM_UPPER = {
        UPPER_ALPHA: LOWER_ALPHA,
        UPPER_BETA: LOWER_BETA,
        UPPER_GAMMA: LOWER_GAMMA,
        UPPER_DELTA: LOWER_DELTA,
        UPPER_EPSILON: LOWER_EPSILON,
        UPPER_ZETA: LOWER_ZETA,
        UPPER_ETA: LOWER_ETA,
        UPPER_THETA: LOWER_THETA,
        UPPER_IOTA: LOWER_IOTA,
        UPPER_KAPPA: LOWER_KAPPA,
        UPPER_LAMDA: LOWER_LAMDA,
        UPPER_MU: LOWER_MU,
        UPPER_NU: LOWER_NU,
        UPPER_XI: LOWER_XI,
        UPPER_OMICRON: LOWER_OMICRON,
        UPPER_PI: LOWER_PI,
        UPPER_RHO: LOWER_RHO,
        UPPER_SIGMA: LOWER_SIGMA,
        UPPER_TAU: LOWER_TAU,
        UPPER_UPSILON: LOWER_EPSILON,
        UPPER_PHI: LOWER_PHI,
        UPPER_CHI: LOWER_CHI,
        UPPER_PSI: LOWER_PSI,
        UPPER_OMEGA: LOWER_OMEGA,
        DIGAMMA: LOWER_DIGAMMA,
        UPPER_LUNATE: LOWER_LUNATE
    }

    @classmethod
    def to_upper(cls, char: int) -> int:
        return cls.FROM_LOWER[char]

    @classmethod
    def to_lower(cls, char: int) -> int:
        return cls.FROM_UPPER[char]

