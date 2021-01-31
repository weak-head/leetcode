class Dir:
    def __init__(self, value=-1):
        self.children = {}
        self.value = value


class FileSystem:
    """
    Trie based.
    """

    def __init__(self):
        self.fs = Dir()

    def createPath(self, path: str, value: int) -> bool:
        """
        Time: O(n)
        Space: O(n)
            n - length of the path
                (because of path.split)
        """
        parts = path.split("/")
        node = self.fs

        for ix in range(1, len(parts) - 1):
            if parts[ix] in node.children:
                node = node.children[parts[ix]]
            else:
                return False

        if parts[-1] in node.children:
            return False

        node.children[parts[-1]] = Dir(value)
        return True

    def get(self, path: str) -> int:
        """
        Time: O(n)
        Space: O(1)
            n - length of the path
            (because of path.split)
        """
        parts = path.split("/")
        node = self.fs
        for ix in range(1, len(parts)):
            if parts[ix] in node.children:
                node = node.children[parts[ix]]
            else:
                return -1
        return node.value
