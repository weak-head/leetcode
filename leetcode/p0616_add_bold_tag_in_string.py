from typing import List


def addBoldTag(s: str, dict: List[str]) -> str:
    """
    Number of substrings for a strings is 'n * (n+1) / 2'
    O(n*(n+1)/2) = O(n^2)
    n - total length of the string
    """
    mask = [False] * len(s)
    for r in reversed(range(len(s))):
        for l in range(r + 1):
            if mask[l]:
                break

            w = s[l : r + 1]
            if w in dict:
                for ix in range(l, r + 1):
                    mask[ix] = True

    res = []
    prev_bold = False
    for ix in range(len(s)):
        if mask[ix] and not prev_bold:
            res.append("<b>")

        if not mask[ix] and prev_bold:
            res.append("</b>")

        prev_bold = mask[ix]
        res.append(s[ix])

    if prev_bold:
        res.append("</b>")

    return "".join(res)
