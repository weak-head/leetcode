class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    """
    Time: O(n)
    Space: O(n)
        n - length of the list
    """

    successor = None

    def rev_n(head, n):
        nonlocal successor
        if n == 1:
            successor = head.next
            return head

        new_head = rev_n(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return new_head

    def rev_lr(head, l, r):
        if l == 1:
            return rev_n(head, r)
        head.next = rev_lr(head.next, l - 1, r - 1)
        return head

    return rev_lr(head, left, right)
