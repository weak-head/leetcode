def minWindow1(S: str, T: str) -> str:
    """
    Time: O(s*t)
    Space: O(s)
        s - length of 's'
        t - length of 't'
    """

    # Values in 'starts' are indexes of 't[0]' in 's'.
    # After the full computation, indexes in 'starts'
    # are indexes of endings 't[-1]' in 's'.
    # . Subsequence is defined by 'S[is: starts[ix]+1]'.
    #   (ix - starts[ix]) => length of the subsequence that contains 't'.
    starts = [ix if char == T[0] else None for ix, char in enumerate(S)]

    # With each iteration 'starts' invariant holds true.
    #   -  S[ix:starts[ix]+1] -> subsequence of 's' that contains t[:ti]
    for ti in range(1, len(T)):

        previous_start = None
        continuation = [None] * len(S)

        for si in range(len(S)):
            # Match of the subsequence continuation,
            # carry over the previous start
            if S[si] == T[ti] and previous_start is not None:
                continuation[si] = previous_start

            if starts[si] is not None:
                previous_start = starts[si]

        # Move to the following char in 'T'
        starts = continuation

    m_start, m_end = 0, len(S)
    for end, start in enumerate(starts):
        if start is not None and (end - start < m_end - m_start):
            m_start, m_end = start, end

    return S[m_start : m_end + 1] if m_end < len(S) else ""


def minWindow2(S: str, T: str) -> str:
    """
    Two pointers,
    Continuosly expand and shrink to find all substrings
    of 'S' that contain 'T'.

    Time: O(s * t)
    Space: O(1)
        s - number of characters in 'S'
        t - number of characters in 'T'
    """

    # two-pointer method
    # Keep expanding the bound until we get the correct substring
    # then shrink the substring to minimize it
    si = ti = 0
    ans = ""

    while si < len(S):

        # Expand the bound until we get the
        # maximum substring that contains 't'
        if S[si] == T[ti]:
            ti += 1

            # Got the substring,
            # now we need to find the starting point
            if ti == len(T):
                end = si + 1

                # Once 'ti' reaches 0,
                # 'si' would point to the begining of the substring
                while ti > 0:
                    if T[ti - 1] == S[si]:
                        ti -= 1
                    si -= 1

                si += 1
                # Stubstring that contains 't' is S[si:end]
                if len(ans) == 0 or end - si < len(ans):
                    ans = S[si:end]

        si += 1

    return ans
