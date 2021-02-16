# flake8: noqa: F403, F405
import pytest
from leetcode.p0887_super_egg_drop import *

solutions = [
    egg_drop_dp,
    egg_drop_dp_bs,
]

test_cases = [
    ([1, 2], 2),
    ([2, 6], 3),
    ([3, 14], 4),
    ([3, 300], 13),
    ([2, 300], 24),
    ([30, 100], 7),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    import functools
    import gc

    gc.collect()
    wrappers = [
        a for a in gc.get_objects() if isinstance(a, functools._lru_cache_wrapper)
    ]

    for wrapper in wrappers:
        wrapper.cache_clear()

    assert solution(*args) == expectation
