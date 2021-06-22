from typing import List


def generate(numRows: int) -> List[List[int]]:
    """
    Time: O(n * n)
    Space: O(n)
        n - number of rows to generate
    """
    prev = []
    this = [1]
    res = [[1]]
    while numRows > 1:
        temp = this
        this = [1] + prev + [1]
        prev = temp

        for i in range(1, len(prev)):
            this[i] = prev[i - 1] + prev[i]

        numRows -= 1
        res.append(this)

    return res
