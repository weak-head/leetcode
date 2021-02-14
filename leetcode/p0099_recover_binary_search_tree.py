class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree_inorder(root: TreeNode) -> None:
    """
    If we swap any two nodes in a binary search tree,
    we can think of this as swapping two elements
    in the sorted array.

    We can get the sorted array from the inorder traversal.

    The inorder traversal:
        > 1 2 3 4 5 6 7 8  [normal]
        > 1 2 7 4 5 6 3 8  [swapped nodes]

        7 > 4 => [7] is first
        6 > 3 => [3] is second

    Time: O(n)
    Space: O(h)
        n - number of nodes in the tree
        h - height of the tree
    """

    prev = first = second = None

    def traverse(node):
        """ Inorder traversal """
        nonlocal prev, first, second

        if node is None:
            return

        traverse(node.left)

        if prev and prev.val > node.val and not first:
            first = prev

        if prev and prev.val > node.val and first:
            second = node

        prev = node

        traverse(node.right)

    traverse(root)
    t = first.val
    first.val = second.val
    second.val = t
    # first.val, second.val = second.val, first.val


def recoverTree_morris(root):
    """
    Similar logic as above,
    but using Morris inorder traversal
    to save space on the call stack.

    Time: O(n)
    Space: O(1)
        n - number of nodes in the tree
    """
    x = y = predecessor = pred = None

    while root:
        # If there is a left child
        # then compute the predecessor.
        # If there is no link predecessor.right = root --> set it.
        # If there is a link predecessor.right = root --> break it.
        if root.left:
            # Predecessor node is one step left
            # and then right till you can.
            predecessor = root.left
            while predecessor.right and predecessor.right != root:
                predecessor = predecessor.right

            # set link predecessor.right = root
            # and go to explore left subtree
            if predecessor.right is None:
                predecessor.right = root
                root = root.left
            # break link predecessor.right = root
            # link is broken : time to change subtree and go right
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root

                predecessor.right = None
                root = root.right
        # If there is no left child
        # then just go right.
        else:
            # check for the swapped nodes
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
            pred = root

            root = root.right

    x.val, y.val = y.val, x.val
