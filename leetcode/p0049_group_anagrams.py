from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(lambda: defaultdict(lambda: []))
    for s in strs:
        groups[len(s)][hash(s)].append(s)

    res = []
    for group in groups.values():
        for subgroup in group.values():
            res.append(subgroup)
    return res


def hash(string):
    h, a = 0, ord("a")
    for c in string:
        h += 26 ** (ord(c) - a)
    return h
