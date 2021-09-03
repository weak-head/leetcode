from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTrees(n: int) -> List[TreeNode]:
    """
    Time: O(catalan_number)
    Space: O(n * catalan_number)
    """

    def gen(start, end):
        if start > end:
            return [None]

        all_trees = []
        for root in range(start, end + 1):
            left_tree = gen(start, root - 1)
            right_tree = gen(root + 1, end)

            for l in left_tree:
                for r in right_tree:
                    current_tree = TreeNode(root)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)

        return all_trees

    return gen(1, n) if n else []
