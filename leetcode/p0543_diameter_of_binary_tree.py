def diameterOfBinaryTree(root):
    """
    Time: O(n)
    Space: O(n)
        n - number of nodes in the tree
    """

    max_distance = 0

    def dfs(node):
        nonlocal max_distance
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        max_distance = max(max_distance, left + right)

        return max(left, right) + 1

    dfs(root)
    return max_distance
