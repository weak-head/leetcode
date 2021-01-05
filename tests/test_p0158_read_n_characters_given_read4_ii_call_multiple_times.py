from leetcode.p0158_read_n_characters_given_read4_ii_call_multiple_times import Solution


def test_read():
    b = [None] * 10
    s = Solution()

    s.read(b, 10)
    assert "".join(b) == "abcdabcdab"

    s.read(b, 10)
    assert "".join(b) == "cdabcdabcd"

    s.read(b, 3)
    s.read(b, 1)
    assert b[0] == "d"
