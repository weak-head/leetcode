from leetcode.p0157_read_n_characters_given_read4 import read


def test_solve():
    buf = [""] * 10
    assert read(buf, 4) == 4
    assert "".join(buf) == "abcd"

    buf = [""] * 10
    assert read(buf, 6) == 6
    assert "".join(buf) == "abcdab"
