def getSmallestString(n: int, k: int) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - desired length of the string
    """
    s = ["a"] * n
    k -= n
    ix = len(s) - 1

    while k > 0:
        v = min(25, k)  # from 'b' to 'z'
        s[ix] = chr(ord("a") + v)
        k -= v
        ix -= 1

    return "".join(s)
