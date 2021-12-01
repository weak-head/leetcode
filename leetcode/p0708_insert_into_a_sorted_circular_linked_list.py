class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insort(head, insertVal):
    """
    Time: O(n)
    Space: O(1)
        n - length of the circular list
    """
    if head is None:
        node = Node(insertVal)
        node.next = node
        return node

    prev, curr = head, head.next
    insert = False

    while True:

        if prev.val <= insertVal <= curr.val:
            insert = True
        elif prev.val > curr.val:
            if insertVal >= prev.val or insertVal <= curr.val:
                insert = True

        if insert:
            prev.next = Node(insertVal, curr)
            return head

        prev, curr = curr, curr.next

        if prev == head:
            break

    prev.next = Node(insertVal, curr)

    return head
