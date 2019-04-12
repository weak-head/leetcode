
def lengthOfLongestSubstring(s: str) -> int:
    visited_chars, max_length, start_ix = {}, 0, 0
    for end_ix, char in enumerate(s):
        if char in visited_chars:
            max_length = max(max_length, end_ix - start_ix)
            # already visited char, need to reset
            if visited_chars[char] >= start_ix:
                start_ix = visited_chars[char] + 1
        else:
            max_length = max(max_length, end_ix - start_ix + 1)
        visited_chars[char] = end_ix
    return max(max_length, len(s) - start_ix)