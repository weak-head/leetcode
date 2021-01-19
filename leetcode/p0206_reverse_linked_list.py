class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    def rev(node):
        if not node:
            return None, None

        first, last = rev(node.next)
        node.next = None

        if last:
            last.next = node
            return first, node
        else:
            return node, node

    first, _ = rev(head)
    return first
