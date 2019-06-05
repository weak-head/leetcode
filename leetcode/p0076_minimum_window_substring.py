from collections import Counter


def minWindow(s, t):
    """
    Solution using sliding window.
    Relatively slow because of 'covers'.
    """
    tnum = Counter(t)
    slen = len(s)
    lix = rix = 0
    ml = mr = None
    while lix < slen:
        cov = covers(tnum)
        # we have found the window
        if cov or rix == slen:
            if cov:
                # adjust min range
                if ml is None or (rix - lix) < (mr - ml):
                    ml, mr = lix, rix

            ch = s[lix]
            if ch in tnum:
                tnum[ch] += 1

            lix += 1
        # we can more rix forward
        else:
            ch = s[rix]
            if ch in tnum:
                tnum[ch] -= 1
            rix += 1

    return "" if ml is None else s[ml:mr]


def covers(tnum: Counter):
    for v in tnum.values():
        if v > 0:
            return False
    return True
