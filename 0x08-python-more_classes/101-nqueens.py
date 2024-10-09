#!/usr/bin/python3
"""Solves the N queens puzzle

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    ./101-nqueens.py N

N must be an int >= equal to 4.

Attributes:
    board : A list of lists representing the chessboard
    solutions : A list of lists containing solutions
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for ur in range(n)]
    [row.append(' ') for ur in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(brd, rw, colo):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        brd: The current working chessboard.
        rw: The row where a queen was last played.
        colo : The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(colo + 1, len(brd)):
        brd[rw][c] = "x"
    # X out all backwards spots
    for c in range(colo - 1, -1, -1):
        brd[rw][c] = "x"
    # X out all spots below
    for r in range(rw + 1, len(brd)):
        brd[r][colo] = "x"
    # X out all spots above
    for r in range(rw - 1, -1, -1):
        brd[r][colo] = "x"
    # X out all spots diagonally down to the right
    c = colo + 1
    for r in range(rw + 1, len(brd)):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = colo - 1
    for r in range(rw - 1, -1, -1):
        if c < 0:
            break
        brd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = colo + 1
    for r in range(rw - 1, -1, -1):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = colo - 1
    for r in range(rw + 1, len(brd)):
        if c < 0:
            break
        brd[r][c] = "x"
        c -= 1


def recursive_solve(brd, rw, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        brd : The current working chessboard
        row : The current working row
        queens : The current number of placed queens
        solutions : A list of lists of solutions
    Returns:
        solutions
    """
    if queens == len(brd):
        solutions.append(get_solution(brd))
        return (solutions)

    for v in range(len(brd)):
        if brd[rw][v] == " ":
            tmp_brd = brd_deepcopy(brd)
            tmp_brd[rw][v] = "Q"
            xout(tmp_brd, rw, v)
            solutions = recursive_solve(tmp_brd, rw + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    solutions = recursive_solve(brd, 0, 0, [])
    for soltn in solutions:
        print(soltn)
