class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


def cleanRoom(robot: "Robot"):
    """
    O(n - m)
    n - number of cells in the room
    m - number of obstacles
    """
    # visited cells
    visited = set()
    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(cell=(0, 0), d=0):
        visited.add(cell)
        robot.clean()

        for i in range(4):
            # using the base direction 'd' to
            # evaluate the new cell we need to move to
            new_direction = (d + i) % 4

            # The next cell we will be at
            # when we make a 'move'
            new_cell = (
                cell[0] + directions[new_direction][0],
                cell[1] + directions[new_direction][1],
            )

            if new_cell not in visited and robot.move():
                backtrack(new_cell, new_direction)
                go_back()

            # All our directions turn are right-handed
            robot.turnRight()

    backtrack()
