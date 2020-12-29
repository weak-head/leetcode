from typing import List


class FileSystem:
    class Dir:
        def __init__(self):
            self.dirs = {}  # string - dir
            self.files = {}  # string - string

    def __init__(self):
        self._root = FileSystem.Dir()

    def ls(self, path: str) -> List[str]:
        """
        O(n + m + k*log(k))
        n -> length of input string
        m -> depth of last directory
        k -> number of child items in the last directory
        """
        node = self._root
        files = []

        if path != "/":
            parts = path.split("/")
            for i in range(1, len(parts) - 1):
                node = node.dirs[parts[i]]

            if parts[len(parts) - 1] in node.files:
                files.append(parts[len(parts) - 1])
                return files
            else:
                node = node.dirs[parts[len(parts) - 1]]

        files.extend([*node.dirs.keys(), *node.files.keys()])
        files.sort()

        return files

    def mkdir(self, path: str) -> None:
        """
        O(n + m)
        n -> lengths of the input string
        m -> depth of the last directory
        """
        if path == "/":
            return

        node = self._root
        parts = path.split("/")
        for i in range(1, len(parts)):
            if parts[i] not in node.dirs:
                node.dirs[parts[i]] = FileSystem.Dir()
            node = node.dirs[parts[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        O(n + m + c)
        n -> length of the input string
        m -> depth of the last directory
        c -> complexity of appending a new content (in this case O(1))
        """
        node = self._root
        parts = filePath.split("/")
        for i in range(1, len(parts) - 1):
            node = node.dirs[parts[i]]
        node.files[parts[len(parts) - 1]] = (
            node.files.get(parts[len(parts) - 1], "") + content
        )

    def readContentFromFile(self, filePath: str) -> str:
        """
        O(n + m)
        n -> length of the input string
        m -> depth of the last directory
        """
        node = self._root
        parts = filePath.split("/")
        for i in range(1, len(parts) - 1):
            node = node.dirs[parts[i]]
        return node.files[parts[len(parts) - 1]]
