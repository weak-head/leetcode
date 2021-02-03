class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Time: O(max(n, m))
    Space: O(max(n, m))
        n - length of the first list
        m - length of the second list
    """

    c = 0
    head = cur = ListNode(None)
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        v = (v1 + v2 + c) % 10
        c = (v1 + v2 + c) // 10
        cur.next = ListNode(v)
        cur = cur.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    if c:
        cur.next = ListNode(c)

    return head.next
