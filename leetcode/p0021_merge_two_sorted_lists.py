class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(None)
    current = head
    while l1 or l2:
        if not l1:
            current.next = l2
            break

        if not l2:
            current.next = l1
            break

        if l1.val < l2.val:
            current.next = l1
            current = current.next
            l1 = l1.next
        else:
            current.next = l2
            current = current.next
            l2 = l2.next
    return head.next


# recursive
def merge(node1, node2):
    if not node1:
        return node2
    if not node2:
        return node1
    if node1.val < node2.val:
        node1.next = merge(node1.next, node2)
        return node1
    else:
        node2.next = merge(node1, node2.next)
        return node2


def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    "Has the smallest overhead and as a result faster"
    cur = dummy = ListNode(None)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            cur = l1
            l1 = l1.next
        else:
            cur.next = l2
            cur = l2
            l2 = l2.next

    if l2:
        cur.next = l2

    if l1:
        cur.next = l1

    return dummy.next
