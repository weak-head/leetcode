import pytest
from leetcode.p0022_generate_parentheses import (
    generateParenthesis,
    generateParenthesis2,
    generateParenthesis3,
    generateParenthesis4,
)


@pytest.mark.parametrize(
    ("num", "result"),
    (
        (0, []),
        (1, ["()"]),
        (2, ["()()", "(())"]),
        (3, ["((()))", "(()())", "()(())", "(())()", "()()()"]),
    ),
)
def test_genPar(num, result):
    a = generateParenthesis(num)
    b = generateParenthesis2(num)
    c = generateParenthesis3(num)
    d = generateParenthesis4(num)

    assert len(result) == len(a)
    assert len(result) == len(b)
    assert len(result) == len(c)
    assert len(result) == len(d)

    sr = set(result)
    sa = set(a)
    sb = set(b)
    sc = set(c)
    sd = set(d)

    assert sr.difference(sa) == set()
    assert sr.difference(sb) == set()
    assert sr.difference(sc) == set()
    assert sr.difference(sd) == set()


def test_genPar_range():
    for num in range(9):
        # a is valid solution
        a = generateParenthesis(num)
        b = generateParenthesis2(num)
        c = generateParenthesis3(num)
        d = generateParenthesis4(num)

        assert len(a) == len(b)
        assert len(a) == len(c)
        assert len(a) == len(d)

        sa = set(a)
        sb = set(b)
        sc = set(c)
        sd = set(d)

        assert sa.difference(sb) == set()
        assert sa.difference(sc) == set()
        assert sa.difference(sd) == set()
