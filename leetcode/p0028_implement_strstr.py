def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    h_len, n_len = len(haystack), len(needle)
    if n_len > h_len:
        return -1

    h_ix = 0
    while (h_len - h_ix) >= n_len:
        n_ix = 0
        while n_ix < n_len:
            if haystack[h_ix + n_ix] != needle[n_ix]:
                break
            n_ix = n_ix + 1

        if n_ix == n_len:
            return h_ix

        h_ix = h_ix + 1

    return -1


def strStr2(haystack: str, needle: str) -> int:
    needle_len = len(needle)
    haystack_len = len(haystack)

    if needle_len > haystack_len:
        return -1

    if needle_len == 0:
        return 0

    for hs_ix in range(haystack_len - needle_len + 1):
        for nd_ix in range(needle_len):
            if haystack[hs_ix + nd_ix] != needle[nd_ix]:
                break
            if nd_ix == needle_len - 1:
                return hs_ix

    return -1
