# flake8: noqa: F403, F405
import pytest
from leetcode.p0341_flatten_nested_list_iterator import *

solutions = [
    NestedIterator,
]

test_cases = [
    ([], []),
    ([1, 2], [1, 2]),
    ([1, 2, [[3, 4], 5], 6, [7]], [1, 2, 3, 4, 5, 6, 7]),
    ([1, [[[[[2]]]]], [[3, 4], 5], 6, [7]], [1, 2, 3, 4, 5, 6, 7]),
]


@pytest.mark.timeout(1)
def test_ni_int():
    ni = NestedInteger(4)
    assert ni.isInteger()
    assert ni.getInteger() == 4


@pytest.mark.timeout(1)
def test_ni_list():
    ni = NestedInteger([1, [2, 3]])
    assert not ni.isInteger()
    for ix, nv in enumerate(ni.getList()):
        assert type(nv) == NestedInteger
        if ix == 0:
            assert nv.isInteger()
            assert nv.getInteger() == 1
        elif ix == 1:
            assert not nv.isInteger()
            for nnv, iv in zip(nv.getList(), [2, 3]):
                assert nnv.isInteger()
                assert nnv.getInteger() == iv


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    s = solution(NestedInteger(args).getList())
    for v in expectation:
        assert s.hasNext()
        assert s.next() == v
    assert not s.hasNext()
