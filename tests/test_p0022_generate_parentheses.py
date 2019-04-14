import pytest
from leetcode.p0022_generate_parentheses import generateParenthesis, generateParenthesis2, generateParenthesis3


@pytest.mark.parametrize(('n', 'result'), (

))
def test_genPar(n, result):
    pass

    # for num in range(9):
    #     # a is valid solution
    #     a = generateParenthesis(num)
    #     b = generateParenthesis2(num)
    #     c = generateParenthesis3(num)

    #     if len(a) != len(b):
    #         print('[b] failed for num {} len: {} vs {}'.format(num, len(a), len(b)))
    #     if len(a) != len(c):
    #         print('[c] failed for num {} len: {} vs {}'.format(num, len(a), len(c)))

    #     sa = set(a)
    #     sb = set(b)
    #     sc = set(c)

    #     if sa.difference(sb) != set():
    #         print('[a-b] diff: {}'.format(sa - sb))
    #         print('[a]: {}'.format(sa))
    #         print('[b]: {}'.format(sb))
    #         assert False
    #     if sa.difference(sc) != set():
    #         print('[a-c] diff: {}'.format(sa - sc))
    #         print('[a]: {}'.format(sa))
    #         print('[c]: {}'.format(sc))
    #         assert False

    # print('passed')
