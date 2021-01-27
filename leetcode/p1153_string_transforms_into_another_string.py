def canConvert(str1: str, str2: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - number of characters in the string
    """
    if str1 == str2:
        return True

    conversions = {}
    for c1, c2 in zip(str1, str2):
        # We can have only 1 to 1 mapping,
        # otherwise we can't convert
        if conversions.setdefault(c1, c2) != c2:
            return False

    # We need to have 1 unused character in 'str2',
    # otherwise we can't covert
    return len(set(str2)) < 26
