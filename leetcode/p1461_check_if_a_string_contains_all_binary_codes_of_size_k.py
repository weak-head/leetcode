def hasAllCodes(s: str, k: int) -> bool:
    """
    Sliding window, with sliding hash

    Time: O(n)
    Space: O(2^k)
    """
    need = 1 << k  # 2^k
    seen = [False] * need  # 2^k
    all_one = need - 1
    code = count = 0

    for i in range(len(s)):
        code = ((code << 1) & all_one) | int(s[i])

        if i >= k - 1 and not seen[code]:
            seen[code] = True
            count += 1
            if count == need:
                return True

    return False
