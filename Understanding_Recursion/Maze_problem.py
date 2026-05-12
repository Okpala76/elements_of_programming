### We are trying to take a list of list and a representation fo a maze and end start at a point and iterate through it to get from a start-point to an end-point
## the main idea is to search depth and if there is a dead end we pop off the opiawuni


def maze_runner(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]):

    path: list[tuple[int, int]] = []
    visited: set[tuple[int, int]] = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  ## up  ## down  ## left  ## right

    row_count = len(maze)
    column_count = len(maze[0]) if row_count > 0 else 0

    def is_valid(row: int, column: int):
        ## to check that the cell is with reach
        row_is_in_maze = 0 <= row < row_count
        column_is_in_maze = 0 <= column < column_count

        ## confirming it
        if not row_is_in_maze or not column_is_in_maze:
            return False
        ## check if cell is a wall
        if maze[row][column] == 1:
            return False
        ## check if cell has been visited
        if (row, column) in visited:
            return False

        ## if has survive ... Yakubu manage!!
        return True

    def back_tracking(row: int, column: int) -> bool:
        if not is_valid(row, column):
            return False

        path.append((row, column))
        visited.add((row, column))

        if (row, column) == end:
            return True

        for row_dir, colunm_dir in directions:
            next_row = row + row_dir
            next_column = column + colunm_dir

            if back_tracking(next_row, next_column):
                return True

        path.pop()
        visited.remove((row, column))

        return False

    start_row, start_column = start

    if back_tracking(start_row, start_column):
        return path
    return []


print(maze_runner([[1, 0, 0], [1, 0, 0], [1, 0, 0]], (0, 2), (2, 2)))


## We make the visited a set so we dont have two tuples added to it as sets a are ....
