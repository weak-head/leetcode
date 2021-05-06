class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST_inorder(head):
    """
    List size + inorder traversal

    Time: O(n)
    Space: O(h)
        n - number of elements
        h - height of the tree (call stack)
    """

    def list_size(head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def inorder(l, r):
        nonlocal head
        if l > r:
            return None

        m = (l + r) >> 1
        left = inorder(l, m - 1)
        node = TreeNode(head.val)
        node.left = left

        head = head.next

        node.right = inorder(m + 1, r)
        return node

    return inorder(0, list_size(head) - 1)


def sortedListToBST_preorder(head: ListNode) -> TreeNode:
    """
    Convert to array + preorder traversal

    Time: O(n)
    Space: O(n)
        n - number of elements
    """
    a = []
    while head:
        a.append(head.val)
        head = head.next

    def preorder(l, r):
        nonlocal a
        if l > r:
            return None

        m = (l + r) >> 1
        node = TreeNode(a[m])
        node.left = preorder(l, m - 1)
        node.right = preorder(m + 1, r)
        return node

    return preorder(0, len(a) - 1)
