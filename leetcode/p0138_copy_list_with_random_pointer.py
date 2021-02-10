class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList_pointers(head: "Node") -> "Node":
    """
    Keep each cloned node next to the original node.
    Then split the list in two.

    Here are the steps:
        1. traverse the list and clone the nodes
            > original:
                a -> b -> c
            > becomes:
                a -> a' -> b -> b' -> c -> c'

        2. traverse the list and update random pointers of the cloned nodes
            > traverse and adjust random pointers of '
                a -> a' -> b -> b' -> c -> c'

        3. detach cloned nodes into separate list
            > the single list
                a -> a' -> b -> b' -> c -> c'
            > splits in the two
                a  -> b  -> c
                a' -> b' -> c'

    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    # 1.
    cur = head
    while cur:
        node = Node(cur.val, None, None)

        node.next = cur.next
        cur.next = node
        cur = node.next

    # 2.
    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    # 3.
    orig = head
    copy_head = copy = head.next
    while orig:
        orig.next = copy.next
        copy.next = copy.next.next if copy.next else None

        copy = copy.next
        orig = orig.next

    return copy_head


def copyRandomList_hash(head: "Node") -> "Node":
    """
    Use hash table to track already visited nodes,
    and avoid processing them again.

    Time: O(n)
    Space: O(n)
    """

    def copy(node, visited):
        if node is None:
            return None

        if node in visited:
            return visited[node]

        n = Node(node.val)
        visited[node] = n

        n.next = copy(node.next, visited)
        n.random = copy(node.random, visited)

        return n

    return copy(head, {})
