import numpy as np

# Example: empty cells are 0

def load_board(grid):
    """
    Convert a 9×9 nested list into a NumPy array of dtype int.
    """
    board = np.array(grid, dtype=int)
    assert board.shape == (9, 9), "Board must be 9x9"
    return board

def is_valid(board, r, c, d):
    # Row check
    if d in board[r, :]:
        return False

    # Column check
    if d in board[:, c]:
        return False

    # 3×3 subgrid check
    br, bc = 3 * (r // 3), 3 * (c // 3)
    if d in board[br:br+3, bc:bc+3]:
        return False

    return True

def find_empty(board):
    """
    Return (r, c) of the first empty cell (0), or None if full.
    """
    for r in range(9):
        for c in range(9):
            if board[r, c] == 0:
                return r, c
    return None


def solve(board):
    """
    Solve the board in-place. Return True if solved, False if no solution.
    """
    empty = find_empty(board)
    if empty is None:
        return True  # Puzzle solved

    r, c = empty
    for d in range(1, 10):
        if is_valid(board, r, c, d):
            board[r, c] = d
            if solve(board):
                return True
            board[r, c] = 0  # backtrack

    return False  # trigger backtracking

if __name__ == '__main__':
    from puzzles import sample_puzzle

    board = load_board(sample_puzzle)
    print("Original:\n", board)

    if solve(board):
        print("Solved:\n", board)
    else:
        print("No solution exists.")

