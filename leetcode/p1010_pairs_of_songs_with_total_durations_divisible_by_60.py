from typing import List
import collections


def numPairsDivisibleBy60(time: List[int]) -> int:
    k, mods = 0, {}
    for num in time:
        mod = num % 60
        key = (60 - mod) % 60
        if key in mods:
            k = k + mods[key]
        mods[mod] = mods.get(mod, 0) + 1
    return k


def numPairsDivisibleBy60_2(time):
    c = collections.Counter()
    res = 0
    for t in time:
        res += c[-t % 60]
        c[t % 60] += 1
    return res