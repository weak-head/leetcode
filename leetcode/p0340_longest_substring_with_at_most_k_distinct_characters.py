from collections import defaultdict, OrderedDict


def lengthOfLongestSubstringKDistinct1(s: str, k: int) -> int:
    """
    Sliding window + Hashmap

    Time: O(n)
    Space: O(k)
        n - length of the string
        k - substring length
    """
    if k == 0:
        return 0

    c = defaultdict(int)
    l, r, max_len = 0, 0, 0

    while r < len(s):

        # Move left side
        while len(c) > k and l < r:
            c[s[l]] -= 1
            if c[s[l]] == 0:
                del c[s[l]]
            l += 1

        # Move right side
        c[s[r]] += 1
        r += 1

        if len(c) <= k:
            max_len = max(max_len, r - l)

    return max_len


def lengthOfLongestSubstringKDistinct2(s: str, k: int) -> int:
    """
    Sliding Windows + Ordered Dictionary

    Time: O(n)
    Space: O(k)
        n - length of the string
        k - substring length
    """
    if not k:
        return k

    start, longest = 0, 0
    last_seen = OrderedDict()

    for end, c in enumerate(s):

        # Update insertion order
        if c in last_seen:
            del last_seen[c]
        last_seen[c] = end

        if len(last_seen) > k:
            _, index = last_seen.popitem(last=False)
            start = index + 1

        longest = max(longest, (end - start) + 1)

    return longest
