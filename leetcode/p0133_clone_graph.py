class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: "Node") -> "Node":
    """
    Use hash table to track already visited nodes.

    Time: O(n)
    Space: O(n)
        n - number of nodes in the graph
    """

    def clone(node, visited):
        if node is None:
            return None

        if node in visited:
            return visited[node]

        n = Node(node.val)
        visited[node] = n

        for neighbor in node.neighbors:
            n.neighbors.append(clone(neighbor, visited))

        return n

    return clone(node, {})
