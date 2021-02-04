class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
        n - length of the list

    Follow up: p0025 - Reverse in K-Group
    """
    if not head or not head.next:
        return head

    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
