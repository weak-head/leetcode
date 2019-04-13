
def isMatch(s: str, p: str) -> bool:
    if s == '' and p == '':
        return True
    if p == '':
        return False

    if s != '' and (s[0] == p[0] or p[0] == '.'):
        if len(p) > 1 and p[1] == '*':
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
        if len(p) > 1 and p[1] == '*':
            return isMatch(s, p[2:])

    return False