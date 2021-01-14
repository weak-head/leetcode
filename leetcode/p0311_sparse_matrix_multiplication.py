"""
Design a data structure for sparse matrix multiplication.
"""


def multiply(dimensions, mxa: [(int, int, int)], mxb: [(int, int, int)]) -> [[int]]:
    """
    This is the core of the question.

    Each matrix is represented as a collection of tuples (r, c, v)
        r - row
        c - column
        v - value
    The tuple is in the collection only in case if value doesn't equal to zero.

    Time: O(n * m)
    n - number of non-zero elements in the matrix A
    m - number of non-zero elements in the matrix B

    Space: O(r * c)
    r - number of rows in the matrix A
    c - number of columns in the matrix B
    """
    res = [[0 for _ in range(dimensions[1])] for _ in range(dimensions[0])]
    for ar, ac, av in mxa:
        for br, bc, bv in mxb:
            if ac == br:
                res[ar][bc] += av * bv
    return res


def compact(mx: [[int]]) -> [(int, int, int)]:
    """
    Compact sparse matrix
    """
    res = []
    for r in range(len(mx)):
        for c in range(len(mx[r])):
            if mx[r][c]:
                res.append((r, c, mx[r][c]))
    return res


def multiplySparse(mxa: [[int]], mxb: [[int]]) -> [[int]]:
    return multiply((len(mxa), len(mxb[0])), compact(mxa), compact(mxb))
