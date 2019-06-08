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


# ------------------------


def groupAnagrams2(strs):
    groups = defaultdict(lambda: [])
    for s in strs:
        groups[to_key(s)].append(s)

    res = []
    for group in groups.values():
        res.append(group)
    return res


def to_key(s):
    key = [0] * 26
    for c in s:
        ix = ord(c) - ord("a")
        key[ix] += 1
    return tuple(key)


# -----------------------------


def groupAnagrams3(strs):
    """
    The fastest solution
    """
    diclist = {}

    for s in strs:
        temp = "".join(sorted(s))

        if temp in diclist:
            diclist[temp].append(s)
        else:
            diclist[temp] = [s]

    return [diclist[i] for i in diclist]
