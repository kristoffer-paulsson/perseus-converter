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

    LOWER_ALPHA = '\u03B1'
    LOWER_BETA = '\u03B2'
    LOWER_GAMMA = '\u03B3'
    LOWER_DELTA = '\u03B4'
    LOWER_EPSILON = '\u03B5'
    LOWER_ZETA = '\u03B6'
    LOWER_ETA = '\u03B7'
    LOWER_THETA = '\u03B8'
    LOWER_IOTA = '\u03B9'
    LOWER_KAPPA = '\u03BA'
    LOWER_LAMBDA = '\u03BB'
    LOWER_MU = '\u03BC'
    LOWER_NU = '\u03BD'
    LOWER_XI = '\u03BE'
    LOWER_OMICRON = '\u03BF'
    LOWER_PI = '\u03C0'
    LOWER_RHO = '\u03C1'
    LOWER_SIGMA_FINAL = '\u03C2'
    LOWER_SIGMA = '\u03C3'
    LOWER_TAU = '\u03C4'
    LOWER_UPSILON = '\u03C5'
    LOWER_PHI = '\u03C6'
    LOWER_CHI = '\u03C7'
    LOWER_PSI = '\u03C8'
    LOWER_OMEGA = '\u03C9'

    CASE_LOWER = frozenset([
        LOWER_ALPHA, LOWER_BETA, LOWER_GAMMA, LOWER_DELTA, LOWER_EPSILON, LOWER_ZETA, LOWER_ETA, LOWER_THETA,
        LOWER_IOTA, LOWER_KAPPA, LOWER_LAMBDA, LOWER_MU, LOWER_NU, LOWER_XI, LOWER_OMICRON, LOWER_PI, LOWER_RHO,
        LOWER_SIGMA_FINAL, LOWER_SIGMA, LOWER_TAU, LOWER_UPSILON, LOWER_PHI, LOWER_CHI, LOWER_PSI, LOWER_OMEGA
    ])

    UPPER_ALPHA = '\u0391'
    UPPER_BETA = '\u0392'
    UPPER_GAMMA = '\u0393'
    UPPER_DELTA = '\u0394'
    UPPER_EPSILON = '\u0395'
    UPPER_ZETA = '\u0396'
    UPPER_ETA = '\u0397'
    UPPER_THETA = '\u0398'
    UPPER_IOTA = '\u0399'
    UPPER_KAPPA = '\u039A'
    UPPER_LAMBDA = '\u039B'
    UPPER_MU = '\u039C'
    UPPER_NU = '\u039D'
    UPPER_XI = '\u039E'
    UPPER_OMICRON = '\u039F'
    UPPER_PI = '\u03A0'
    UPPER_RHO = '\u03A1'
    UPPER_SIGMA = '\u03A3'
    UPPER_TAU = '\u03A4'
    UPPER_UPSILON = '\u03A5'
    UPPER_PHI = '\u03A6'
    UPPER_CHI = '\u03A7'
    UPPER_PSI = '\u03A8'
    UPPER_OMEGA = '\u03A9'

    CASE_UPPER = frozenset([
        UPPER_ALPHA, UPPER_BETA, UPPER_GAMMA, UPPER_DELTA, UPPER_EPSILON, UPPER_ZETA, UPPER_ETA, UPPER_THETA,
        UPPER_IOTA, UPPER_KAPPA, UPPER_LAMBDA, UPPER_MU, UPPER_NU, UPPER_XI, UPPER_OMICRON, UPPER_PI, UPPER_RHO,
        UPPER_SIGMA, UPPER_TAU, UPPER_UPSILON, UPPER_PHI, UPPER_CHI, UPPER_PSI, UPPER_OMEGA
    ])

    HYPHEN_MINUS = '\u002D'

    ALPHABET = frozenset(CASE_LOWER | CASE_UPPER | {HYPHEN_MINUS})

