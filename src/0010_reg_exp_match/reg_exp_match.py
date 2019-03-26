
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

if __name__ == '__main__':
    assert isMatch('aaa', 'aaa') == True
    assert isMatch('aaa', 'a*') == True

    assert isMatch('aaa', 'aaaa') == False
    assert isMatch('aaaa', 'aaa') == False

    assert isMatch('', '.*') == True
    assert isMatch('', 'a*') == True

    assert isMatch('abc', 'c*d*abb*cc*') == True
    assert isMatch('abc', 'c*d*a.b*cc*') == True
    assert isMatch('abcde', 'c*d*a.c.*') == True
    assert isMatch('abcde', 'c*d*a.b.*') == False
    assert isMatch('abc', '.*') == True

    assert isMatch('', '') == True
    assert isMatch('abc', '') == False
    assert isMatch('', 'abc') == False
    assert isMatch('', 'a*b*c*') == True

    assert isMatch('abcde', '.....') == True
    assert isMatch('abcdef', '.....') == False
    assert isMatch('abcd', '.....') == False

    assert isMatch('bbbbba', '.*a*a') == True

    assert isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False

    print('passed')