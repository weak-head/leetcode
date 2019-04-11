
'''Without using linear Manacher's algorithm'''

def longestPalindrome(s: str) -> str:
    if s is None or len(s) == 0:
        return ''

    s_len = len(s)
    longest_l_ix, longest_r_ix = 0, 0
    for ix in range(0, s_len):

        # odd palindrome case, ix is a center of palindrome
        l_ix, r_ix = ix - 1, ix + 1
        while l_ix >= 0 and r_ix < s_len and s[l_ix] == s[r_ix]:
            if (r_ix - l_ix) > (longest_r_ix - longest_l_ix):
                longest_l_ix, longest_r_ix = l_ix, r_ix
            l_ix, r_ix = l_ix - 1, r_ix + 1

        # even palindrome case, ix is left half of a center
        l_ix, r_ix = ix, ix + 1
        while l_ix >= 0 and r_ix < s_len and s[l_ix] == s[r_ix]:
            if (r_ix - l_ix) > (longest_r_ix - longest_l_ix):
                longest_l_ix, longest_r_ix = l_ix, r_ix
            l_ix, r_ix = l_ix - 1, r_ix + 1

    return s[longest_l_ix:longest_r_ix + 1]

if __name__ == '__main__':
    assert longestPalindrome('') == ''
    assert longestPalindrome('abcd') == 'a'
    assert longestPalindrome('aba') == 'aba'
    assert longestPalindrome('abacaba') == 'abacaba'
    assert longestPalindrome('abacabad') == 'abacaba'
    assert longestPalindrome('dabacaba') == 'abacaba'
    assert longestPalindrome('abaccaba') == 'abaccaba'
    assert longestPalindrome('dabaccaba') == 'abaccaba'
    assert longestPalindrome('abaccabad') == 'abaccaba'

    print('done')