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
import glob
import re
import unicodedata
from pathlib import PosixPath

DIACRITICS_TABLE = dict.fromkeys(map(ord, "\u0300\u0301\u0304\u0306\u0308\u0313\u0314\u0342\u0345"), None)

def main():
    words = {}
    follow = {}
    follow_strip = {}
    characters = {}
    for path in glob.glob("koine/*.txt"):
        text = PosixPath(path).read_text()

        for parts in re.split("[\u002C\u002E\u003B\u00B7]", text):
            match = re.findall("[\u0300\u0301\u0304\u0306\u0308\u0313\u0314\u0342\u0345\u0390-\u03ff\u1f00-\u1fff]+[\u2019]?", parts)
            cnt = len(match)
            if cnt > 1:
                before = match[0]
                before_stripped = before.translate(DIACRITICS_TABLE)
                for idx in range(1, cnt):
                    after = match[idx]
                    after_stripped = after.translate(DIACRITICS_TABLE)

                    if before not in follow.keys():
                        follow[before] = set()
                    follow[before].add(after)

                    if before_stripped not in follow_strip.keys():
                        follow_strip[before_stripped] = set()
                    follow_strip[before_stripped].add(after_stripped)

                    before = after
                    before_stripped = after_stripped

        for line in text.splitlines():
            match = re.findall("[\u0300\u0301\u0304\u0306\u0308\u0313\u0314\u0342\u0345\u0390-\u03ff\u1f00-\u1fff]+[\u2019]?", line)
            for word in match:
                stripped = word.translate(DIACRITICS_TABLE)
                if stripped not in words.keys():
                    words[stripped] = set()
                words[stripped].add(word)

            for token in list(line):
                if token not in characters.keys():
                    characters[token] = 0
                characters[token] += 1

    for word in sorted(list(words.keys())):
       print("{0}: {1}".format(word, " ".join(sorted(list(words[word])))))

    for word in sorted(list(follow.keys())):
       print("{0}: {1}".format(word, " ".join(sorted(list(follow[word])))))

    for word in sorted(list(follow_strip.keys())):
       print("{0}: {1}".format(word, " ".join(sorted(list(follow_strip[word])))))

    print("Total words: {}".format(sum(words.values())))
    print("Distinct words: {}".format(len(words.keys())))

    for token in sorted(list(characters.keys())):
        print("  {0}  {1}  {2}  {3}".format(
            token,
            hex(ord(token)),
            unicodedata.name(token, "N/a"),
            characters[token]
        ))


if __name__ == "__main__":
    main()

