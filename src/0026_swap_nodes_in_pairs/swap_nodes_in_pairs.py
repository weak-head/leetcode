from typing import List, Generator


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head: ListNode) -> ListNode:
    new_head = current = ListNode(None)
    parent_prev = parent = None
    current.next, ix = head, 0

    while current.next != None:
        parent_prev = parent
        parent = current
        current = current.next
        ix = ix + 1

        # even node
        if ix % 2 == 0:
            parent.next = current.next
            current.next = parent
            parent_prev.next = current
            current = parent

    return new_head.next


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


def swap_convert(a: List[int]) -> List[int]:
    head = from_array(a)
    head = swapPairs(head)
    return list(to_array(head))


if __name__ == '__main__':
    assert swap_convert([]) == []
    assert swap_convert([1, 2, 3, 4]) == [2, 1, 4, 3]
    assert swap_convert([1, 2, 3, 4, 5, 6, 7]) == [2, 1, 4, 3, 6, 5, 7]

    print('passed')
