from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(n)
    """
    if head is None:
        return None

    def list_len(head):
        cur = head
        l = 0
        last = None
        while cur is not None:
            last = cur
            cur = cur.next
            l += 1
        return (l, last)

    def kth(head, k):
        n = 0
        cur = head
        prev = None
        while n != k:
            prev = cur
            cur = cur.next
            n += 1
        return prev

    l, last = list_len(head)

    k = k % l
    if k == 0:
        return head

    prev = kth(head, l - k)
    last.next = head
    head = prev.next
    prev.next = None

    return head
