# In the chapter we introduce Graphs the algo of partial understanding with relation to computer .. the discipline behind it
# with graph modeling at the heart of it we talk dfs, bfs and DAG, directed ad undirected , acylic and cyclic and
# we see how physical relation are mapped.
# is a world high on progress who are those that will take the guard of the foundation.

# Problem 19.1: Given a 2D array of black and white entries representing a maze with
# designated entrance and exit points, find a path from the entrance to the exit, if one
# exists.

# This problem we have solved before in this book and yet t surfaces again., we solved this when
# where understanding recursion


def search_maze(
    maze: list[list[int]], entrance: tuple[int, int], exit: tuple[int, int]
):
    row_len = len(maze)
    col_len = len(maze[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up  # down  # right  # left
    visited = set()
    path = []

    def is_valid(row: int, col: int):
        # check if out of bound
        within_row = 0 < row < row_len
        within_col = 0 < col < col_len

        if not within_col or not within_row:
            return False

        # visited
        if (row, col) in visited:
            return False

        # not white
        if maze[row][col] == 1:
            return False

        return True

    def dfs(row: int, col: int):

        if not is_valid(row, col):
            return False

        visited.add((row, col))
        path.append((row, col))

        if (row, col) == exit:
            return True

        for row_d, col_d in directions:

            new_row = row_d + row
            new_col = col_d + col

            if dfs(new_row, new_col):
                return True

        path.pop()
        return False

    if dfs(entrance[0], entrance[1]):
        return path
    return []
