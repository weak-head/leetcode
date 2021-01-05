from typing import List


def candyCrush(board: List[List[int]]) -> List[List[int]]:
    """
    O( (row * col)^2 )
    """

    # O(row * col)
    while True:
        crush = set()

        # Mark candies to crush O(row * col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Vertical candy
                if (
                    row > 1
                    and board[row][col]
                    and board[row][col] == board[row - 1][col] == board[row - 2][col]
                ):
                    crush |= {(row, col), (row - 1, col), (row - 2, col)}

                # Horizontal candy
                if (
                    col > 1
                    and board[row][col]
                    and board[row][col] == board[row][col - 1] == board[row][col - 2]
                ):
                    crush |= {(row, col), (row, col - 1), (row, col - 2)}

        # The board is stable
        if not crush:
            break

        # Crush candies O(row * col)
        for row, col in crush:
            board[row][col] = 0

        # Drop candies
        for col in range(len(board[0])):

            first_zero_row = len(board) - 1
            for row in reversed(range(len(board))):
                if board[row][col]:
                    board[first_zero_row][col] = board[row][col]
                    first_zero_row -= 1

            for zero_row in range(first_zero_row + 1):
                board[zero_row][col] = 0

    return board
