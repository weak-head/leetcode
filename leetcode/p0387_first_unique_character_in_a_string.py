class Node:
    def __init__(self, val, ix, next, prev):
        self.val = val
        self.ix = ix
        self.prev = prev
        self.next = next


def firstUniqChar(s: str) -> int:
    chars = {}
    head = Node(None, None, None, None)
    head.next = head.prev = head

    for ix, c in enumerate(s):
        if c not in chars:
            node = Node(c, ix, head, head.prev)
            head.prev.next = node
            head.prev = node
            chars[c] = node
        else:
            node = chars[c]
            if node is not None:
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                chars[c] = None

    result = head.next
    return result.ix if result.val else -1
