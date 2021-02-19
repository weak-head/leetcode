def stone_game(p):
    """
    Dynamic programming

    Generalization of stone game.
    Works for odd and even number of piles.
    Track the max possible score for the first and back hand.

    The generalization is hard, because whenever
    the first hand makes a selection, it becomes
    the back hand for the remaining sub-problem.
    With each selection first and back hands are switched.

    Time: O(n^2)
    Space: O(n^2)
        n - length of the array
    """
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    # main diagonal, first hand selects
    for i in range(n):
        dp[i][i] = (p[i], 0)

    # diagonal traversal
    for diag in range(1, n):
        for row in range(n - diag):
            col = diag + row

            # the current pile sequence is defined by
            #   > p[row .. col]
            # row - is left-most pile
            # col - is right-most pile

            # - The first hand could select left- or right-most pile -
            # Whenever first hand select left or right-most pile,
            # it becomes the back hand of the remaining pile sequence.

            left_most = p[row] + dp[row + 1][col][1]  # left + back_hand(row+1 .. col)
            right_most = p[col] + dp[row][col - 1][1]  # right + back_hand(row .. col-1)

            # - Select the optimal move -
            # First-hand of subproblem becomes the back-hand of this problem
            if left_most > right_most:
                dp[row][col] = (left_most, dp[row + 1][col][0])
            else:
                dp[row][col] = (right_most, dp[row][col - 1][0])

    first, back = dp[0][-1]
    return first > back


def stone_game_optimized(p):
    """
    Dynamic Programming, optimized for space.

    Same logic, but instead of the main diagonal traversal
    we follow left-right bottom-up direction and
    re-use state to save the space.

    Time: O(n^2)
    Space: O(n)
        n - length of the array
    """
    n = len(p)
    this = [0] * n
    prev = [0] * n
    prev[-1] = (p[-1], 0)

    for row in range(n - 2, -1, -1):
        this[row] = (p[row], 0)
        for col in range(row + 1, n):

            left_most = p[row] + prev[col][1]
            right_most = p[col] + this[col - 1][1]

            if left_most > right_most:
                this[col] = (left_most, prev[col][0])
            else:
                this[col] = (right_most, this[col - 1][0])

        this, prev = prev, this

    first, back = prev[-1]
    return first > back
