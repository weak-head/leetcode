from collections import Counter


def minWindow(s, t):
    """
    Sliding window
    With optimization to track the state

    Time: O(s + t)
    Space: O(t)
        s - length of 's'
        t - length of 't'
    """
    if not s or not t:
        return ""

    state = Counter(t)
    state_left = len(state)
    ml = mr = None  # right side open
    li = ri = 0

    while li < len(s):

        covers = state_left == 0

        # we can't find the window
        if ri == len(s) and state_left != 0:
            break

        # adjust min
        if covers:
            if ml is None or (ri - li) < (mr - ml):
                ml, mr = li, ri

        # covers or reached end -> move left
        if covers or ri == len(s):
            ch = s[li]
            if ch in state:
                state[ch] += 1
                if state[ch] == 1:
                    state_left += 1
            li += 1
        # not covers, expand -> move right
        else:
            ch = s[ri]
            if ch in state:
                state[ch] -= 1
                if state[ch] == 0:
                    state_left -= 1

            ri += 1

    return s[ml:mr] if ml is not None else ""
