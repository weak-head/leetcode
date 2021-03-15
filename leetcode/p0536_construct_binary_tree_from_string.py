from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s: str) -> TreeNode:
    """
    Construct the tree from pre-order:
        4(2(3)(1))(6(5)(7))

    Into level-order:
        [4,2,6,3,1,5,7]

    Time: O(n)
    Space: O(n) #because of deque
        Note:
            We can reduce the space to O(h), by using the global index
            instead of queue, but it would be not as beautiful,
            as the solution with the deque.

        n - length of the string
        h - max height of the binary tree
    """

    def getval(q):
        val, sign = 0, 1
        if q[0] == "-":
            q.popleft()
            sign = -1
        while q and q[0] not in {"(", ")"}:
            val *= 10
            val += int(q.popleft())
        return val * sign

    def getnode(q):
        if not q:
            return None

        node = TreeNode(getval(q))

        if q and q[0] == "(":
            q.popleft()
            node.left = getnode(q)

        if q and q[0] == "(":
            q.popleft()
            node.right = getnode(q)

        if q and q[0] == ")":
            q.popleft()

        return node

    return getnode(deque(s))


def str2tree_ix(s: str) -> TreeNode:
    """
    Construct the tree from pre-order:
        4(2(3)(1))(6(5)(7))

    Into level-order:
        [4,2,6,3,1,5,7]

    Time: O(n)
    Space: O(h)
        n - length of the string
        h - max height of the binary tree
    """

    ix = 0

    def getval():
        nonlocal ix
        val, sign = 0, 1
        if s[ix] == "-":
            ix += 1
            sign = -1
        while ix < len(s) and s[ix] not in {"(", ")"}:
            val *= 10
            val += int(s[ix])
            ix += 1
        return val * sign

    def getnode():
        nonlocal ix
        if ix > len(s):
            return None

        node = TreeNode(getval())

        if ix < len(s) and s[ix] == "(":
            ix += 1
            node.left = getnode()

        if ix < len(s) and s[ix] == "(":
            ix += 1
            node.right = getnode()

        if ix < len(s) and s[ix] == ")":
            ix += 1

        return node

    return getnode()
