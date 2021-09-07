def orderlyQueue(s: str, k: int) -> str:
    """
    Time: O(n * n)
    Space: O(n)
    """
    if k == 1:
        return min(s[i:] + s[:i] for i in range(len(s)))
    else:
        return "".join(sorted(s))
