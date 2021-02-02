import pytest
from leetcode.p0234_palindrome_linked_list import ListNode, isPalindrome, isPalindrome2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((ListNode(1)), (True)),
        ((ListNode(1, ListNode(2))), (False)),
        ((ListNode(1, ListNode(2, ListNode(2, ListNode(1))))), (True)),
        ((ListNode(1, ListNode(2, ListNode(1)))), (True)),
        ((None), (True)),
    ),
)
def test_solve(a, expectation):
    assert isPalindrome(a) == expectation
    assert isPalindrome2(a) == expectation
