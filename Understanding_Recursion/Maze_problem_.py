# The goal is to start from a given point and search through the maze until we reach the destination point.

# The main idea is to use a depth-first search
# (DFS) approach: we keep moving deeper into one possible path until we either find the destination
# or hit a dead end. When we reach a dead end, we backtrack by popping the last position off the path and trying another available direction.
# This process continues until a valid path to the end is found or all possible paths have been explored.


def maze_runner(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    # path holder
    path: list[tuple[int, int]] = []
    # the places we have visited
    visited: set[tuple[int, int]] = set()

    # This stipulates the directioning
    # we make use of lists within a list
    # Hence meaning that (0,1) will be outer list at index of 0 and inner or sub list at index of 1
    # so 0 is the x axis and 1 is the y axis as should be
    # e.g
    # [
    # [0,0,1],
    # [0,1,0],
    # [0,0,1]
    # ]
    # (0,1) = 0
    # (0,2) = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  ## up  ## down  ## left  ## right

    ## we accept the row as earlier stated the index of the outer list
    row_count = len(maze)
    ## and the coulmn as the row's lists if there is a row since teh column is dependent on the coulmn
    column_count = len(maze[0]) if row_count > 0 else 0

    ## Here we write a function that will check , relative to the present location of navigation(when we begin to move across the maze) is even
    # a valid point(node or location, axis), if it is out of bound or the location of a wall(1) this fucntion will return false
    # or if it is a row that has been visited before, we dont go there again
    def is_valid(row: int, column: int):
        ## to check that the cell is within reach
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

        ## if it survives ... Yakubu manage!!
        return True

    def back_tracking(row: int, column: int) -> bool:
        ## we start by applying the isvalid fuction to know if this row works or not
        if not is_valid(row, column):
            return False
        # if it does work and has no compromise we add it to the path and the update our visited list
        path.append((row, column))
        visited.add((row, column))

        # if this is our specified "end" axis or co-ordinates
        if (row, column) == end:
            return True

        # Now here the crispy part
        # we now try every direction relative to our present location to see if any is valid(not visted, not out of bound, not a wall)
        # so we iterate the four locations around the point of validity
        for row_dir, colunm_dir in directions:
            next_row = row + row_dir  # construct the next row co-ordinate
            next_column = column + colunm_dir  # construct the next column co-ordinate

            ## Now we call backtracking again to make the checks and handle new cordinate correctly
            if back_tracking(next_row, next_column):
                return True
        ## if a false is returned
        # then we pop that location from our path
        # and then go ahead to return false of that direction
        # and go on to consider other directions and consider this one as a dead end
        path.pop()
        visited.remove((row, column))

        return False

    ## here we extract from the  start row and start column from the start tuple added in line 8
    start_row, start_column = start
    ## Then we call the first instance of back tracking with our extracted values
    if back_tracking(start_row, start_column):
        # and finally we return the path built at the latter end
        return path
    return []


print(maze_runner([[1, 0, 0], [1, 0, 0], [1, 0, 0]], (0, 1), (2, 2)))


## We make the visited a set so we dont have two tuples added to it as sets a are ....

a = 1
b = 2  # ?  <-- Comment Macro ~ Result ->

print(a)
