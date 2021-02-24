from functools import lru_cache


def maxA(n: int) -> int:
    """
    Dynamic Programming

    We know that our key sequence should end with either:
        - pressing 'A'
        - pressing 'Ctrl-V'
    And we should have 'Ctrl-A' + 'Ctrl-C' somewhere in the middle.

    Time: O(n^2)
    Space: (n)
    """

    s = [0] * (n + 1)
    for keys_left in range(1, n + 1):
        # simply press 'A'
        press_a = s[keys_left - 1] + 1

        # press 'Ctrl-V' with 'Ctrl-A' + 'Ctrl-C'
        # somewhere in the middle
        press_v = float("-inf")
        for ctrl_a_c in range(2, keys_left):
            # If we hit [Ctrl-A + Ctrl-C] at 'ctrl_a_c' position
            # we copy buffer at 'ctrl_a_c - 2' position.
            buff_len = s[ctrl_a_c - 2]

            # Now we can paste this buffer 'N' times
            # and it will result in 'N+1' sizes of the original buffer
            paste_size = buff_len * (keys_left - ctrl_a_c + 1)

            press_v = max(press_v, paste_size)

        s[keys_left] = max(press_a, press_v)

    return s[-1]


def maxA_naive_slow(n: int) -> int:
    """
    Dynamic Programming

    This solution follows the direct logic.
    It's slow, but will give the correct result.

    Time: O(n^3)
    Space: O(n^3)

    leetcode: TLE
    """

    @lru_cache(None)
    def mlen(a_len, buf_len, keys_left):
        if keys_left == 0:
            return a_len

        if keys_left < 0:
            return float("-inf")

        add_a = mlen(a_len + 1, buf_len, keys_left - 1)
        copy_buf = mlen(a_len, a_len, keys_left - 2)
        insert_buf = mlen(a_len + buf_len, buf_len, keys_left - 1)

        return max(add_a, copy_buf, insert_buf)

    return mlen(0, 0, n)
