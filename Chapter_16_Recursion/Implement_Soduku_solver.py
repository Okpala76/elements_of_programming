# Problem 16.3: Implement a Sudoku solver. Your program should read an instance
# of Sudoku from the command line. The command line argument is a sequence of
# 3-digit strings, each encoding a row, a column, and a digit at that location. pg. 153

# Lets break it down.
# Sodoku is a board game with rules
# Rule 1: No value repeation on a row
# Rule 2: No value repeation on a column
# Rule 3: No value repeation on any of the 3*3 areas of the board
# Rule 4: has a 9*9 grid area

# the board is defined by a set o values designed in a 3 digit string pattern
# "005" means row =0 , column = 0 , value = 5


# The Brute force
# I wont be dwelling on the bruteforce why
# because it does not even take the game into account( the rules i mean)\

# def brute_force_sudoku(board):
#     generate every possible filling of empty cells
#     for each completed board:
#         if board is valid:
#             return board
#     return None


# Complexity
# O(9^E) where E is empty cells and 9 is all possible replacements it could have
# O(E) the recursion stack and it variables


# Optimized approach

# Build the Sodoku board
# find the first empty
# if none is empty return True
# When you find the first empty, go through and find the first number that can safey fill it
# while meeting all conditions
# if you find call sodoku again
# if sodoku meets the requirement by starting from that number to the end then glorious, if not
# then we try another number
# now is found we return false

# First lest build the board

import sys


def build_board_from_args(args: list[str]) -> list[list[int]]:
    """
    Converts command line 3-digit strings into a 9x9 Sudoku board.

    Example:
    "005" means row 0, column 0, digit 5.
    """

    board = [[0 for _ in range(9)] for _ in range(9)]

    for token in args:
        if len(token) != 3 or not token.isdigit():
            raise ValueError(f"Invalid token: {token}")

        row = int(token[0])
        col = int(token[1])
        digit = int(token[2])

        if not (0 <= row <= 8):
            raise ValueError(f"Invalid row in token: {token}")

        if not (0 <= col <= 8):
            raise ValueError(f"Invalid column in token: {token}")

        if not (1 <= digit <= 9):
            raise ValueError(f"Invalid digit in token: {token}")

        if not is_valid_number((row, col), board, digit):
            raise ValueError(f"Invalid starting board: {token}")

        if board[row][col] != 0:
            raise ValueError(f"Cell already filled: {token}")

        board[row][col] = digit

    return board


def print_board(board: list[list[int]]) -> None:
    for row in range(9):
        if row > 0 and row % 3 == 0:
            print("-" * 21)

        for col in range(9):
            if col > 0 and col % 3 == 0:
                print("|", end=" ")

            print(board[row][col], end=" ")

        print()


def find_empty_cell(board: list[list[int]]):
    "Helps us to find the the latest row and column in board that is empty"
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid_number(cell_location: tuple[int, int], board: list[list[int]], digit: int):
    row, col = cell_location

    # check if the row has repeation

    for c in range(9):
        if digit == board[row][c]:
            return False

    # check if the column has repeation
    for r in range(9):
        if digit == board[r][col]:
            return False

    # check if there is repeation in that quadrant(not quad but u get)
    row_sec = row // 3 * 3
    col_sec = col // 3 * 3

    for row in range(row_sec, row_sec + 3):
        for col in range(col_sec, col_sec + 3):
            if board[row][col] == digit:
                return False

    return True


def solve_sudoku(board: list[list[int]]):

    empty_cell = find_empty_cell(board)

    if empty_cell is None:
        return True

    row, col = empty_cell

    for i in range(1, 10):
        if is_valid_number((row, col), board, i):
            board[row][col] = i

            if solve_sudoku(board):
                return True
            # Backtrack
            # remove the already added number
            board[row][col] = 0
    # If no digit works in this cell, this path is impossible.

    return False


# Complexity
# Worst-case time:
# O(9^E)
# Why?
# Because each empty cell can still theoretically try up to 9 digits.

# Space:
# O(E)
# because recursion can go as deep as the number of empty cells.

# Personal lesson

# This problem teaches that backtracking is controlled guessing: try a valid move, go deeper, and undo it if it leads to failure. The power is not in guessing blindly, but in rejecting illegal choices early.

# The worst-case complexity is still O(9^E), but backtracking is much faster in practice because it prunes invalid choices early instead of generating complete invalid boards.
if __name__ == "__main__":
    board = build_board_from_args(sys.argv[1:])

    print("Input board:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved board:")
        print_board(board)
    else:
        print("\nNo solution exists.")
