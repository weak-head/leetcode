from typing import List

# Strainforward scanning
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ''
    common_prefix = list(strs[0])
    for s in strs:
        for s_ix in range(len(common_prefix) - 1, -1, -1):
            if s_ix >= len(s) or common_prefix[s_ix] != s[s_ix]:
                d_ix = len(common_prefix) - 1
                while d_ix >= s_ix:
                    del common_prefix[d_ix]
                    d_ix = d_ix - 1
        if common_prefix == []:
            return ""
    return "".join(common_prefix)

if __name__ == '__main__':
    assert longestCommonPrefix([]) == ''
    assert longestCommonPrefix(['abc', 'abcd', 'abcdef', 'abb']) == 'ab'
    assert longestCommonPrefix(['abc', 'fde', 'fek']) == ''
    assert longestCommonPrefix(["flower","flow","flight"]) == 'fl'
    assert longestCommonPrefix(['aca', 'bca']) == ''

    print('passed')