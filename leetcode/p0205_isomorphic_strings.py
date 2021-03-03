from collections import defaultdict


def isIsomorphic(s: str, t: str) -> bool:
    """
    Encode each string and check the encoding match

    Time: O(n)
    Space: O(n)
    """

    def encode(s):
        m = {}
        r = []
        for char in s:
            if char not in m:
                m[char] = len(m)  # increasing index
            r.append(m[char])
        return str(r)

    return encode(s) == encode(t)


def group_isomorphic(strs):
    """
    Follow-up, group isomorphic strings

    Time: O(n * l)
    Space: O(l)
        n - number of strings
        l - length of longest string
    """

    def encode(s):
        r, d = [], {}
        for c in s:
            if c not in d:
                d[c] = len(d)
            r.append(d[c])
        return str(r)

    m = defaultdict(list)
    for s in strs:
        m[encode(s)].append(s)

    return list(m.values())
