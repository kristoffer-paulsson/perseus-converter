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
"""Data used in the application for several reasons."""
import json
from hashlib import md5
from pathlib import PosixPath


class MetaIterator:
    """Iterator for the PDL using the canonical-greekLit.tracking.json"""
    def __init__(self, data_path: PosixPath):
        self.path = data_path

    def __iter__(self):
        for resource in self._res_iter().values():
            yield resource

    def _res_iter(self):
        cnt_grc = 0
        cnt_eng = 0
        res = dict()
        for x, y, z, p in self._load_iter():
            hash = md5(x[:-8].encode()).digest()
            if "grc" in x:
                if hash in res.keys():
                    res[hash]["grc"].append(x)
                    res[hash]["valid"] = y
                    res[hash]["meta"] = z
                    res[hash]["ref"] = p
                else:
                    res[hash] = {
                        "grc": [x],
                        "value": y,
                        "meta": z,
                        "ref": p,
                        "eng": list()
                    }
                cnt_grc += 1
            elif "eng" in x:
                if hash in res.keys():
                    res[hash]["eng"].append(x)
                else:
                    res[hash] = {
                        "grc": list(),
                        "value": None,
                        "meta": None,
                        "ref": None,
                        "eng": [x]
                    }
                cnt_eng += 1
        return res

    def _load_iter(self):
        with open(self.path.joinpath("canonical-greekLit/canonical-greekLit.tracking.json")) as obj:
            for key, value in json.load(obj).items():
                yield value["target"], value["valid_xml"] if "valid_xml" in value else None, value["has_cts_metadata"] if "has_cts_metadata" in value else None, value["has_cts_refsDecl"] if "has_cts_refsDecl" in value else None
