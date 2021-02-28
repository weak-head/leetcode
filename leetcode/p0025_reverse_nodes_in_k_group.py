class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup_optimized(head, k):
    """
    Time: O(n)
    Space: O(1)
    """
    dummy = prev_group_end = ListNode(0)
    dummy.next = this_group_start = next_group_start = head

    while True:

        # find the start of the next group
        count = 0
        while next_group_start and count < k:
            next_group_start = next_group_start.next
            count += 1

        if count == k:
            # reverse this k-group
            pre, cur = next_group_start, this_group_start
            for _ in range(k):
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

            # connect prev group to this group
            prev_group_end.next = pre

            # jump to next iteration
            prev_group_end = this_group_start
            this_group_start = next_group_start

        else:
            return dummy.next


def reverseKGroup(head, k):
    """
    Time: O(n)
    Space: O(n)
    """
    count, node = 0, head
    while node and count < k:
        node = node.next
        count += 1

    if count < k:
        return head

    new_head, prev = reverse(head, count)
    head.next = reverseKGroup(new_head, k)
    return prev


def reverse(head, count):
    """
    Time: O(c)
    Space: O(1)
        c - count
    """
    prev, cur = None, head
    while count > 0:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        count -= 1
    return (cur, prev)
