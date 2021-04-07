def halvesAreAlike(s: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    vowels = set("aeiouAEIOU")
    mid = len(s) // 2

    ca = sum(1 for c in s[:mid] if c in vowels)
    cb = sum(1 for c in s[mid:] if c in vowels)

    return ca == cb
