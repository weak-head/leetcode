import pytest
from leetcode.p0020_valid_parentheses import isValid


@pytest.mark.parametrize(('string', 'valid'), (
    ('', True),
    ('()', True),
    ('(abc + [k] - {as()} + )', True),
    ('(abc + [k] - as()} + )', False),
    ('(abc + [k - {as()} + )', False),
    ('abc + [k] - {as()} + )', False),
    (')abc + [k] - {as()} + (', False),
))
def test_isValid(string, valid):
    assert isValid(string) == valid