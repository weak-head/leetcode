class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    """
    Double pointer, fast/slow

    Time: O(n)
    Space: O(1)
    """
    if head is None:
        return None

    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
