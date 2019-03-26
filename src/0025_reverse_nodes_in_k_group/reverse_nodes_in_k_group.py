from typing import Generator, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


if __name__ == '__main__':
    head = from_array([1,2,3,4,5])
    itm3 = head.next
    head, end = reverse_group(head, itm3)
    print(list(to_array(head)), end.val)
