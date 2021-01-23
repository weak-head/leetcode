from typing import List


def addBoldTag1(s: str, dict: List[str]) -> str:
    """
    Time: O(m * n)
        m - number of words in dict
        n - total length of the string
    Space: O()
    """
    bold = [False] * len(s)

    for word in dict:
        start = s.find(word)
        while start != -1:
            for i in range(start, len(word) + start):
                bold[i] = True
            start = s.find(word, start + 1)

    output = []

    i = 0
    while i < len(s):
        if bold[i]:
            output.append("<b>")
            while i < len(s) and bold[i]:
                output.append(s[i])
                i += 1
            output.append("</b>")
        else:
            output.append(s[i])
            i += 1

    return "".join(output)


def addBoldTag2(s: str, dict: List[str]) -> str:
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
