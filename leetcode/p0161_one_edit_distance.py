def isOneEditDistance(s: str, t: str) -> bool:
    """
    O(n)
    n - length of the string
    """
    # for simplicity, we want 's' to be shorter than 't'
    if len(s) > len(t):
        s, t = t, s

    # length difference can't be more than 1
    if len(t) - len(s) > 1:
        return False

    for i in range(len(s)):
        if s[i] != t[i]:
            # The tail of the strings should match
            if len(s) == len(t):
                return s[i + 1 :] == t[i + 1 :]
            else:
                return s[i:] == t[i + 1 :]

    # if there are no differences, the strings
    # one edit away only if t has one extra character
    return len(s) + 1 == len(t)
