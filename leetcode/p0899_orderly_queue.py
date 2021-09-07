def orderlyQueue(s: str, k: int) -> str:
    """
    When k == 1 only rotation is possible.
    When k > 1 any permutation is possible.

    Time: O(n * n)
    Space: O(n)
    """
    if k == 1:
        return min(s[i:] + s[:i] for i in range(len(s)))
    else:
        return "".join(sorted(s))
