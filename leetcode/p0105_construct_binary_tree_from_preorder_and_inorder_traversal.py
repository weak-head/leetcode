from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    We use Pre-order as source of Node values.
    And In-order to identify Left and Right subtrees of the node.

    Time: O(n)
    Space: O(n)
        n - number of elements in the array
    """
    if len(preorder) == 0:
        return None

    # Using the hashtable help us
    # avoid the quadratic complexity
    inorder_map = {inorder[ix]: ix for ix in range(len(inorder))}

    def build(preorder, left, right):
        """
        'left' and 'right' identifies the boundary
        of the subtree this node is the root of
        in the 'in-order' array.
        """
        if left > right:
            return None

        node = TreeNode(preorder.popleft())

        # Left subtree:
        #   preorder[ 1 : node_ix ]
        # Right subtree:
        #   preorder[ node_ix + 1 : ]
        node_ix = inorder_map[node.val]

        node.left = build(preorder, left, node_ix - 1)
        node.right = build(preorder, node_ix + 1, right)

        return node

    return build(deque(preorder), 0, len(preorder) - 1)


def buildTree_quadratic(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    We can get Node from the Pre-order traversal,
    and we can get left and right sub-trees
    from the In-order traversal.

    This implementation is very un-efficient because
    it uses list slicing that has a complexity of O(n),
    and we have to run the list slicing O(n) * 4 times.
    Effectively this gives us quadratic complexity.

    Time: O(n * n)
    Space: O(n * n)
        n - length of the list
    """
    if len(preorder) == 0:
        return None

    # Pre-order is:
    # Node -> Left -> Right
    node = TreeNode(preorder[0])

    # In-order is:
    # Left -> Node -> Right
    node_ix = inorder.index(node.val)

    node.left = buildTree_quadratic(preorder[1 : node_ix + 1], inorder[:node_ix])
    node.right = buildTree_quadratic(preorder[node_ix + 1 :], inorder[node_ix + 1 :])

    return node
