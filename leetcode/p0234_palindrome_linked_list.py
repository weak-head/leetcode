from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - number of elements in the list
    """
    q = deque()

    def pal(node):
        nonlocal q

        if not node:
            return True

        p = True
        q.append(node.val)
        if node.next:
            p = pal(node.next)

        v = q.popleft()
        return p and v == node.val

    return pal(head)


def isPalindrome2(head: ListNode) -> bool:
    """
    Find the half of the list,
    reverse the second half in place,
    compare first half with the second half.

    Time: O(n)
    Space: O(1)
    """

    def end_of_first_half(head):
        """
        Find the half of the list.

        Time: O(n)
        Space: O(1)
            n - number of elements in the list
        """
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_list(head):
        """
        Reverse list in place.

        Time: O(n)
        Space: O(1)
            n - number of elements in the list
        """
        previous, current = None, head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    if head is None:
        return True

    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)

    result = True
    first = head
    second = second_half_start

    while result and second:
        if first.val != second.val:
            result = False
        first = first.next
        second = second.next

    # Restore the list
    first_half_end.next = reverse_list(second_half_start)
    return result
