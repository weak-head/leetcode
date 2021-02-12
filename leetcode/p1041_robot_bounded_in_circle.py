def isRobotBounded(instructions: str) -> bool:
    """
    We can run movement simulation of 4 cycles.
    After 4 cycles if (x, y) is not (0, 0)
    we don't have the fixed circle.

    Also, we can run only 1 cycle,
    and if direction doesn't change,
    we wont return to (0, 0).

    Time: O(n)
    Space: O(1)
        n - length of instructions
    """

    def one_move_cycle(x, y, direction, path):
        # up, right, down, left
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for p in path:
            if p == "G":
                x += moves[direction][0]
                y += moves[direction][1]
            elif p == "L":
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
        return x, y, direction

    x, y, d = one_move_cycle(0, 0, 0, instructions)
    return (x == 0 and y == 0) or (d != 0)
