from typing import List

# Strainforward scanning
def longestCommonPrefix2(strs: List[str]) -> str:
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

# Checking n-th letter of a k-th string
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ''
    for ix, current_char in enumerate(strs[0]):
        for s in strs:
            if len(s) <= ix:
                return s
            if s[ix] != current_char:
                return strs[0][0:ix]
    return strs[0]
