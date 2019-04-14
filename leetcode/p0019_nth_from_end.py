class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    node, p_node, d_node, k = head, None, None, 1
    while node is not None:

        if d_node is None and k == n:
            d_node = head
        elif d_node is not None:
            p_node = d_node
            d_node = d_node.next

        node = node.next
        k = k + 1

    # generic case
    if p_node is not None:
        p_node.next = p_node.next.next
    # case when head is deleted
    elif d_node is not None:
        return d_node.next

    return head
