class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: "Node") -> str:
        """
        Encodes a tree to a single string.

        DFS with a sentinel
        Time: O(n)
        Space: O(n)
        """
        r = []

        def dfs(node: Node):
            if not node:
                return

            # Convert an integer to Unicode character.
            # We can cover up to int(2^64).
            # Also we need to shift the int value by 48,
            # so it's never converted to '#'.
            r.append(chr(node.val + 48))

            for c in node.children:
                dfs(c)

            # end of all children for this node
            r.append("#")

        dfs(root)
        return "".join(r)

    def deserialize(self, data: str) -> "Node":
        """
        Decodes your encoded data to tree.

        Time: O(n)
        Space: O(n)
        """
        ix = 0

        def recover():
            nonlocal ix

            if ix >= len(data):
                return

            if data[ix] == "#":
                return

            node = Node(ord(data[ix]) - 48, [])
            ix += 1

            while data[ix] != "#":
                node.children.append(recover())

            ix += 1
            return node

        return recover()
