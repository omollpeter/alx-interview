#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if the queen can be placed on board at (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n):
    """Solve the N-Queens problem and print all solutions."""
    def backtrack(row):
        if row == n:
            print_solution(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n
    backtrack(0)


def print_solution(board):
    """Print the board in the required format."""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)


if __name__ == "__main__":
    main()
