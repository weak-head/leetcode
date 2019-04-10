from typing import Generator, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if head == [] or k <= 1:
        return head

    new_head = prev_group_end = current = ListNode(None)
    new_head.next = head
    ix = 0

    while current != None:
        if ix == k:
            n_group_head, n_group_end = reverse_group(
                prev_group_end.next, current)
            prev_group_end.next = n_group_head
            prev_group_end = n_group_end
            current = prev_group_end.next
            ix = 1
        else:
            current = current.next
            ix = ix + 1

    return new_head.next


def reverse_group(head, tail):
    current = last_element = head
    new_head = None
    next_group_head = tail.next

    while current != next_group_head:
        new_current = current.next
        current.next = new_head
        new_head = current
        current = new_current

    last_element.next = next_group_head
    return new_head, last_element


def from_array(a: List[int]) -> ListNode:
    head = current = ListNode(None)
    for el in a:
        current.next = ListNode(el)
        current = current.next
    return head.next


def to_array(head: ListNode) -> Generator[int, None, None]:
    while head is not None:
        yield head.val
        head = head.next


def reverse_convert(a: List[int], k: int) -> List[int]:
    head = from_array(a)
    head = reverseKGroup(head, k)
    return list(to_array(head))


if __name__ == '__main__':
    assert reverse_convert([], 1) == []
    assert reverse_convert([], 0) == []
    assert reverse_convert([], 110) == []

    assert reverse_convert([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert reverse_convert([1, 2, 3, 4, 5, 6, 7, 8, 9], 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert reverse_convert([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [
        2, 1, 4, 3, 6, 5, 8, 7, 9]
    assert reverse_convert([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [
        3, 2, 1, 6, 5, 4, 9, 8, 7]

    print('passed')