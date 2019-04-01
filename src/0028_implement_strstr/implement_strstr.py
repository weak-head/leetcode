
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

if __name__ == '__main__':
    assert strStr('abbba', 'bba') == 2
    assert strStr('asb', '') == 0
    assert strStr('kdf', 'abc') == -1
    assert strStr('abba', 'abbaa') == -1

    print('passed')