# Problem 17.2: How many ways can you go from the top-left to the bottom-right
# in an n × m 2D array? How would you count the number of ways in the presence
# of obstacles, specified by an n × m Boolean 2D array B, where a true represents an
# obstacle.
#
#


from turtle import right


def count_2D_ways(two_d_arr: list[list[int]]):

    row = len(two_d_arr)
    col = len(two_d_arr[0])

    def helper(i, j):
        if i >= row or j >= col:
            return 0
        if two_d_arr[i][j] == True:
            return 0
        if (
            i == row - 1 and j == col - 1
        ):  ## avoid checking the value at the index i.e two_d_arr[i][j] == two_d_arr[row-1][col-1] why?..go figure
            return 1

        right = helper(i, j + 1)
        down = helper(i + 1, j)

        return right + down

    return helper(0, 0)


# Complexity
# Time = O(2^(n + m)) == O(2^(2n)) == O(2^n)()removing constants ----- cells are visted more that once, we expreience branching where every cell call two cells, exponential
# Space =  O(2^n) for all recursion stacks
# Pattern: top-down dynamic programming.

## Let use add memoization
# Now memoisation will help use easily track an return a cell paths so we dont have to recalulate


def count_2D_ways_memo(two_d_arr: list[list[int]]):
    row = len(two_d_arr)
    col = len(two_d_arr[0])
    memo = {}  ## dict is like saying list it is the class itself and a typer

    def helper(i, j):
        # memoisation block
        if (i, j) in memo:
            return memo[(i, j)]  # dicts are returned with square brackets

        # outside grid
        if i >= row or j >= col:
            return 0

        # blocked
        if two_d_arr[i][j] is True:
            return 0
        # reach target
        if i == row - 1 and j == col - 1:
            return 1

        right = helper(i, j + 1)
        left = helper(i + 1, j)

        total = right + left

        memo[(i, j)] = total  ## dont use sum it is an inbuit pythin function

        return total

    return helper(0, 0)


# Complexity
# Time = O(n*m) == O(n^2) ---- memoisation ensure only one visit per cell
# Space = O(n) visited all stack
# pattern : top-down dynamic programming with memoization.

# Brute force:
# recalculates the same cell many times → exponential

# Memoization:
# calculates each cell once → n * m


def count_2D_ways_dp(two_d_arr: list[list[int]]):
    row = len(two_d_arr)
    col = len(two_d_arr[0])

    dp = [[0] * col for _ in range(row)]

    if two_d_arr[0][0] is True:
        return 0

    dp[0][0] = 1

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue

            if two_d_arr[i][j] is True:
                dp[i][j] = 0
                continue

            left_count = dp[i][j - 1] if j > 0 else 0
            above_count = dp[i - 1][j] if i > 0 else 0

            dp[i][j] = left_count + above_count

    return dp[row - 1][col - 1]


# Complexity
# Let rows = n and cols = m
# Time:  O(n * m)
#   We visit every cell once.
#
# Space: O(n * m)
#   The dp table stores one answer for every cell.
#
# If the grid is square, meaning n == m:
# Time:  O(n^2)
# Space: O(n^2)

# Pattern: 2D Dynamic Programming / grid DP


if __name__ == "__main__":
    tester_arr = [[False, False, False], [False, False, False], [False, False, False]]
    print(count_2D_ways_dp(tester_arr))
