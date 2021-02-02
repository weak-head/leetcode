def isMatch_dp(s, p):
    """
    Dynamic programming.

    Cross-checking string 'abbcad' with '.*c.*' pattern, we have
    the following map:

        | a | b | b | c | a | d | '' |
      . |
      * |
      c |
      . |
      * |
     '' |

    Starting from m[-1][-1] we can fill the map.

    m[-1][-1] = True, because empty string matches empty pattern.
    For all the other cells there are three cases of [True]:
        - [if match] consume pattern and char (diagonal move: right + down)
        - [if match][only for *] consume char and keep pattern (move right)
        - [if match][only for *] ignore pattern (move down)
    Otherwise [False]

    [if match] happens only when string char equals pattern char or '.'
    [only for *] could happen only for kleene star

    Time: (s * p)
    Space: (s * p)
        s - length of the string
        p - length of the pattern
    """
    m = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
    m[-1][-1] = True

    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and p[j] in {s[i], "."}

            if j + 1 < len(p) and p[j + 1] == "*":
                ignore_pattern = m[j + 2][i]  # move down
                consume_char = match and m[j][i + 1]  # move right
                m[j][i] = ignore_pattern or consume_char
            else:
                consume_char_and_pattern = match and m[j + 1][i + 1]  # diagonal
                m[j][i] = consume_char_and_pattern

    return m[0][0]


def isMatch_bt_memo(s, p):
    """
    Backtracking with memoization

    Time:
    Space:
    """
    backtrack, tried = [], set()

    si = pi = 0
    while si < len(s):

        # The kleene star pattern of form 'c*' or '.*'
        # we can:
        #   a) consume character
        #   b) ignore pattern
        if pi + 1 < len(p) and p[pi + 1] == "*":

            # a)
            # memorize the case when we consume character,
            # to backtrack to it later
            nexttry = (si + 1, pi)
            if p[pi] in {s[si], "."} and nexttry not in tried:
                backtrack.append(nexttry)
                tried.add(nexttry)

            # b)
            # ignore pattern
            pi += 2

        # Exact match of pattern char and string char:
        #   - 'c' == 'c'
        #   - 'c' == '.'
        elif pi < len(p) and p[pi] in {s[si], "."}:
            # exact match
            pi += 1
            si += 1

        # Backtrack to the case when we consumed
        # some character without touching the pattern
        elif backtrack:
            si, pi = backtrack.pop()

        else:
            return False

    # after we reached the end of the string
    # we can ignore all kleene stars
    while pi + 1 < len(p) and p[pi + 1] == "*":
        pi += 2

    return pi >= len(p)
