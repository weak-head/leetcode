from typing import List
from collections import defaultdict


def groupStrings(strings: List[str]) -> List[List[str]]:
    """
    Time: O(c)
        c - Total number of all characters in all strings
    """

    def frequency(s):
        return tuple([(ord(c) - ord(s[0])) % 26 for c in s])

    similar = defaultdict(list)
    for s in strings:
        similar[frequency(s)].append(s)

    return similar.values()
