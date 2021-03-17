from functools import lru_cache


def minSteps_dp(n: int) -> int:
    """
    Dynamic Programming, top down

    Time: O(n^2)
    Space: O(n^2)
    """

    @lru_cache(None)
    def mins(buf_len, size):
        if size == n:
            return 0

        if size > n:
            return float("inf")

        if buf_len > n:
            return float("inf")

        if buf_len + size > n:
            return float("inf")

        if_paste = float("inf")
        if buf_len > 0:
            if_paste = 1 + mins(buf_len, size + buf_len)

        if_copy = float("inf")
        if buf_len < size:
            if_copy = 1 + mins(size, size)

        return min(if_paste, if_copy)

    return mins(0, 1)


def minSteps_prime(n):
    """
    Prime factorization

    Time: O(sqrt(n))
    Space: O(1)
    """
    ans = 0
    d = 2
    while n > 1:
        while n % d == 0:
            ans += d
            n /= d
        d += 1
    return ans
