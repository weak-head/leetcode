def isMatch(s: str, p: str) -> bool:
    """
    Backtracking without memoization,
    with string copy. Very slow.
    """
    if s == "" and p == "":
        return True
    if p == "":
        return False

    if s != "" and (s[0] == p[0] or p[0] == "."):
        if len(p) > 1 and p[1] == "*":
            # ignore glob
            match = isMatch(s, p[2:])

            # ignore char and glob
            match = match or isMatch(s[1:], p[2:])

            # ignore char and preserve glob
            return match or isMatch(s[1:], p)
        else:
            return isMatch(s[1:], p[1:])
    # s == '' | s[0] != p[0] | p[0] != '.'
    else:
        if len(p) > 1 and p[1] == "*":
            return isMatch(s, p[2:])

    return False


def isMatch2(s, p):
    """Backtracking with memoization"""
    sn, pn = len(s), len(p)
    si = pi = 0
    stack, tried = list(), set()

    # try to reach the end of the string
    while si < sn:
        if pi + 1 < pn and p[pi + 1] == "*":
            # here we have two cases:
            #   - consume string character
            #   - ignore pattern
            nexttry = (si + 1, pi)
            if p[pi] in {s[si], "."} and nexttry not in tried:
                # consume the character from 's'
                # and memorize that we need to try this later
                stack.append(nexttry)
                tried.add(nexttry)

            # ignore pattern
            pi += 2
        elif pi < pn and p[pi] in {s[si], "."}:
            # exact match
            pi += 1
            si += 1
        elif stack:
            # backtrack
            si, pi = stack.pop()
        else:
            return False

    # after we reached the end of the string
    # we can ignore all kleene stars
    while pi + 1 < pn and p[pi + 1] == "*":
        pi += 2

    return pi >= pn
