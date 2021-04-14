class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head: ListNode, x: int) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
        n - length of the list
    """
    greater = gc = ListNode()
    smaller = sc = ListNode()

    while head:
        if head.val < x:
            sc.next = head
            sc = sc.next
        else:
            gc.next = head
            gc = gc.next
        head = head.next

    sc.next = greater.next
    gc.next = None
    return smaller.next
