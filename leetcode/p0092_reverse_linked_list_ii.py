class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween_optimized(head: ListNode, left: int, right: int) -> ListNode:
    """
    Optimized for space.

    Time: O(n)
    Space: O(1)
        n - length of the list
    """
    if left == right:
        return head

    def rev_n(node, n):
        prev, cur = None, node
        while n > 0:
            if n == 1:
                node.next = cur.next
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            n -= 1
        return prev

    def rev_lr(node, l, r):
        prev, cur = None, node
        while l != 1:
            prev = cur
            cur = cur.next
            l -= 1
            r -= 1
        prev.next = rev_n(cur, r)
        return node

    node = ListNode(None, head)
    return rev_lr(node, left + 1, right + 1).next


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
