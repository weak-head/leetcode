import pytest
from leetcode.p0022_generate_parentheses import generateParenthesis, generateParenthesis2, generateParenthesis3


@pytest.mark.parametrize(('num', 'result'), (
    (0, []),
    (1, ['()']),
    (2, ['()()', '(())']),
    (3, ['((()))', '(()())', '()(())', '(())()', '()()()'])
))
def test_genPar(num, result):
    a = generateParenthesis(num)
    b = generateParenthesis2(num)
    c = generateParenthesis3(num)

    assert len(result) == len(a)
    assert len(result) == len(b)
    assert len(result) == len(c)

    sr = set(result)
    sa = set(a)
    sb = set(b)
    sc = set(c)

    assert sr.difference(sa) == set()
    assert sr.difference(sb) == set()
    assert sr.difference(sc) == set()


def test_genPar_range():
    for num in range(9):
        # a is valid solution
        a = generateParenthesis(num)
        b = generateParenthesis2(num)
        c = generateParenthesis3(num)

        assert len(a) == len(b)
        assert len(a) == len(c)

        sa = set(a)
        sb = set(b)
        sc = set(c)

        assert sa.difference(sb) == set()
        assert sa.difference(sc) == set()