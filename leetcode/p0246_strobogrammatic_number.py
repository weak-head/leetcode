from collections import deque


def isStrobogrammatic_2(num: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - number of bits in the number
    """
    flips = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6",
    }
    r = deque()
    for n in num:
        if n not in flips:
            return False
        r.appendleft(flips[n])
    return num == "".join(r)


def isStrobogrammatic_1(num: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - number of bits in the number
    """
    s = num
    strob = {"0", "1", "8"}
    l, r = 0, len(s) - 1
    while l <= r:
        if (
            (s[l] in strob and s[r] in strob and s[l] == s[r])
            or (s[l] == "6" and s[r] == "9")
            or (s[l] == "9" and s[r] == "6")
        ):
            l += 1
            r -= 1
        else:
            return False

    return True
