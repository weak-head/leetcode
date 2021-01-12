def canConvert(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True

    conversions = {}
    # strings are of the same length
    for c1, c2 in zip(str1, str2):
        # we can have only 1 to 1 mapping,
        # otherwise we can't convert
        if conversions.setdefault(c1, c2) != c2:
            return False

    # We can use only 26 lowercase English characters
    return len(set(str2)) < 26
