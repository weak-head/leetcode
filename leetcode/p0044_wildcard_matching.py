def isMatch(s: str, p: str) -> bool:
    sn, pn = len(s), len(p)
    si = pi = 0
    stack, tried = list(), set()

    while si < sn:
        if pi < pn and p[pi] == "*":
            # memorize that we need to try
            # consuming next char
            nexttry = (si + 1, pi)
            if nexttry not in tried:
                tried.add(nexttry)
                stack.append(nexttry)
            # ignore
            pi += 1
        elif pi < pn and p[pi] in {"?", s[si]}:
            pi += 1
            si += 1
        elif stack:
            si, pi = stack.pop()
        else:
            return False

    while pi < pn and p[pi] == "*":
        pi += 1

    return pi >= pn
