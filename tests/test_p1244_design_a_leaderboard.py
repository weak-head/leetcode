from leetcode.p1244_design_a_leaderboard import Leaderboard


def test_solve():
    l = Leaderboard()
    l.addScore(1, 1)
    l.addScore(2, 1)
    l.addScore(3, 1)
    l.addScore(4, 1)
    l.addScore(5, 1)
    l.addScore(6, 10)
    assert l.top(3) == 12
    assert l.top(4) == 13
    assert l.top(1) == 10
