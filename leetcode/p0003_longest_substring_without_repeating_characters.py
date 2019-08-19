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


def lengthOfLongestSubstring2(s: str) -> int:
    subs = {}
    max_len, l_ix = 0, 0

    for ix, char in enumerate(s):

        # the character is not in the substring
        # we can safely add it and increase the
        # length of current substring
        if char not in subs:
            max_len = max(max_len, ix - l_ix + 1)

        # the character is in substring,
        # we have to adjust the substring,
        # removing all left items.
        # but there is an optimization we can make.
        # instead of touching the dictionary we can work
        # with indexes and check if the index of the character
        # is within the current substring range
        else:
            last_char_ix = subs[char]

            # the char is outside the substring
            # borders and we can simply ignore it
            if last_char_ix < l_ix:
                max_len = max(max_len, ix - l_ix + 1)

            # the previous char position is our current left limit
            else:
                l_ix = last_char_ix + 1

        subs[char] = ix

    return max_len
