def isMatch_backtrack(s: str, p: str) -> bool:
    """
    Sort of backtracking to previous '*'
    https://arxiv.org/pdf/1407.0950.pdf

    Time (best)    :  O(min(s, p))
    Time (average) :  O(s * log(p))
    Time (worst)   :  O(s * p)
    Space: O(1)
        s - length of 's' string
        p - length of 'p' string

    Time complexity examples:
        Best: O(min(s, p))
            s:  abcde
            p:  abcde*

        Average: O(s * log(p))
            s: abccde
            p: ab*de

        Worst: O(s * p)
            s: aaaaaaaaaaaaab
            p: *aaaaab
    """
    si = pi = 0
    star_ix = str_ix = -1

    while si < len(s):

        # Consume character from string and pattern
        if pi < len(p) and p[pi] in {"?", s[si]}:
            si += 1
            pi += 1

        # Try to ignore '*' and memo '*' position
        elif pi < len(p) and p[pi] == "*":
            star_ix = pi
            str_ix = si
            pi += 1

        # No match. If there were no star before - we cant backtrack
        elif star_ix == -1:
            return False

        # Backtrack to the previous '*', and consume one char, keeping the '*'
        else:
            pi = star_ix + 1  # backtrack pattern
            str_ix += 1  # consume one char
            si = str_ix  # backtrack string

    # Ignore all trailing '*'
    return all(x == "*" for x in p[pi:])


def isMatch_dp(s: str, p: str) -> bool:
    """
    Dynamic programming
    Similar to {LC10}

    Time: O(s * p)
    Space: O(s * p)
        s - length of 's'
        p - length of 'p'
    """
    m = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
    m[-1][-1] = True

    for row in range(len(p) - 1, -1, -1):
        m[row][-1] = m[row + 1][-1] and p[row] == "*"

    for col in range(len(s) - 1, -1, -1):
        for row in range(len(p) - 1, -1, -1):

            if p[row] in {"?", s[col]}:
                m[row][col] = m[row + 1][col + 1]  # consume char
            elif p[row] == "*":
                ignore_pattern = m[row + 1][col]
                drop_letter = m[row][col + 1]
                m[row][col] = ignore_pattern or drop_letter

    return m[0][0]
