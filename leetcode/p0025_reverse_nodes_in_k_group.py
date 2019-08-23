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

    while current is not None:
        if ix == k:
            n_group_head, n_group_end = reverse_group(prev_group_end.next, current)
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


# -------------------------------------------------------------
# -------------------------------------------------------------


def reverseKGroup2(head: ListNode, k: int) -> ListNode:
    """
    Reverse K-group in the linked list.
    This implementation is easier to follow, though
    the complexity is same as above.
    """
    if head is None:
        return None

    prev = dummy = ListNode(None)
    dummy.next = head

    while True:
        # Get next group that should be reversed
        group_head, group_tail = next_group(prev.next, k)
        if group_tail is None:
            return dummy.next

        # Reverse the group
        new_head, new_tail = reverse(group_head, group_tail)

        # Re-attach the new group head and move on
        prev.next = new_head
        prev = new_tail


def next_group(head, n):
    """
    Given the head of the list returns
    the first and the last element
    of the next group with length 'n'.
    """
    if head is None:
        return head, None

    curr = head
    index = 1
    while index != n and curr:
        curr = curr.next
        index += 1

    if index != n:
        return head, None
    else:
        return head, curr


def reverse(head, last):
    """
    Given the first and any intermediate element in the list
    reverses the list between them (inclusively).
    """
    prev, curr = None, head
    last_next = last.next

    while prev != last:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    head.next = last_next
    return prev, head
