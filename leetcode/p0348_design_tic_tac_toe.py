class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonals = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.

        O(1)
        """
        s = -1 if player == 1 else 1

        self.rows[row] += s
        if abs(self.rows[row]) == self.n:
            return player

        self.cols[col] += s
        if abs(self.cols[col]) == self.n:
            return player

        if row == col:
            self.diagonals[0] += s
            if abs(self.diagonals[0]) == self.n:
                return player

        if (row + col) == self.n - 1:
            self.diagonals[1] += s
            if abs(self.diagonals[1]) == self.n:
                return player

        return 0
