class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup2(head, k):
    """
    Time: O(n)
    Space: O(1)
    """
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:

        count = 0
        while r and count < k:  # use r to locate the range
            r = r.next
            count += 1

        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups

        else:
            return dummy.next


# -----


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
