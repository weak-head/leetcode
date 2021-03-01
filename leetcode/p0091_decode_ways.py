from functools import lru_cache


def num_decoding_dp(s: str) -> int:
    """
    Dynamic Programming, optimized for space

    Time: O(n)
    Space: O(1)
        n - length of the string
    """
    prev1 = prev2 = 1
    for i in range(len(s) - 1, -1, -1):
        this = 0
        if s[i] != "0":
            this = prev1
            if (i + 1) < len(s) and int(s[i : i + 2]) <= 26:
                this += prev2
        prev2 = prev1
        prev1 = this

    return prev1


def num_decoding_dp_bu(s: str) -> int:
    """
    Dynamic Programming, Bottom Up

    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    m = [1] * (len(s) + 2)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            m[i] = 0
        else:
            ways = m[i + 1]
            if (i + 1) < len(s) and int(s[i : i + 2]) <= 26:
                ways += m[i + 2]
            m[i] = ways
    return m[0]


def num_decodings_dp_td(s: str) -> int:
    """
    Dynamic Programming, Top Down

    Time: O(n)
    Space: O(n)
        n - length of the string
    """

    @lru_cache(None)
    def decode(i):
        if i >= len(s):
            return 1

        if s[i] == "0":
            return 0

        if i == len(s) - 1:
            return 1

        ways = decode(i + 1)
        if int(s[i : i + 2]) <= 26:
            ways += decode(i + 2)

        return ways

    return decode(0)
