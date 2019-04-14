
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
