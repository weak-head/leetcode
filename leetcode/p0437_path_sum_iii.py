from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum_prefix_sum(root: TreeNode, k: int) -> int:
    """
    Prefix sums

    Time: O(n)
    Space: O(h)
        n - number of nodes
        h - max height of the tree
    """
    count = 0
    prefix_sums = defaultdict(int)

    def preorder(node: TreeNode, prefix_sum) -> None:
        nonlocal count, prefix_sums

        if node is None:
            return

        prefix_sum += node.val

        if prefix_sum == k:
            count += 1

        count += prefix_sums[prefix_sum - k]

        prefix_sums[prefix_sum] += 1

        preorder(node.left, prefix_sum)
        preorder(node.right, prefix_sum)

        prefix_sums[prefix_sum] -= 1

    preorder(root, 0)
    return count


def pathSum_bf(root: TreeNode, sum: int) -> int:
    """
    Naive brute-force

    Time: O(n^2)
    Space: O(h)
        n - number of nodes in the tree
        h - height of the tree
    """

    def psum(node, s):
        if not node:
            return 0

        return count(node, s) + psum(node.left, s) + psum(node.right, s)

    def count(node, s):
        if node is None:
            return 0

        return (
            (s == node.val)
            + count(node.left, s - node.val)
            + count(node.right, s - node.val)
        )

    return psum(root, sum)
