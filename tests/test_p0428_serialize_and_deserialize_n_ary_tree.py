from leetcode.p0428_serialize_and_deserialize_n_ary_tree import Node, Codec


def test_codec():

    tree = Node(
        1,
        [
            Node(2),
            Node(3, [Node(4, [Node(5)])]),
            Node(6),
            Node(7, [Node(8, [Node(9), Node(10), Node(11, [Node(13)]), Node(12)])]),
        ],
    )

    serialized = "12#345###6#789#:#;=##<####"

    c = Codec()
    assert c.serialize(tree) == serialized
    t2 = c.deserialize(serialized)
    assert compare(tree, t2)


def compare(n1: Node, n2: Node):
    if n1.val != n2.val:
        return False

    for c1, c2 in zip(n1.children, n2.children):
        if not compare(c1, c2):
            return False

    return True
