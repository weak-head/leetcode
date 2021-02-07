from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
        n - length of the array
    """

    def node(l, r):
        if l > r:
            return None
        m = (l + r) >> 1
        return TreeNode(nums[m], node(l, m - 1), node(m + 1, r))

    return node(0, len(nums) - 1)
