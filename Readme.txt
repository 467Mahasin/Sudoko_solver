🧠 Automatic Sudoku Solver 🧩
A Python project using NumPy to solve 9x9 Sudoku puzzles automatically

📌 Overview
This is a simple yet powerful Automatic Sudoku Solver built using Python and NumPy.
It takes a 9x9 Sudoku puzzle as input (with empty cells marked as 0) and solves it using a backtracking algorithm.

Perfect for learning recursion, backtracking, and matrix manipulation using NumPy!

🚀 Features
Solves any valid 9x9 Sudoku puzzle

Uses NumPy arrays for efficient board representation

Implements the classic backtracking algorithm

Command-line interface (CLI) based

Easy to read and modify

🧮 How It Works
The algorithm follows these steps:

Find an empty cell (marked as 0)

Try digits 1 through 9 in that cell

Check if the digit is valid in the current row, column, and 3x3 box

If valid, place the digit and recursively try to solve the rest of the board

If no valid digit is found, backtrack and try a different number

📦 Requirements
Python 3.13.0
NumPy


# Sample Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve(board)
print_board(board)
📂 File Structure
sudoku_solver/
│
├── solver.py   # Contains solving logic
└── puzzles.py  # Project explanation
└── README.md   # Project explanation


✅ Sample Output

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9


📈 Future Improvements
Add a GUI using Tkinter or PyQt

Add input from an image (via OCR)

Solve puzzles of different sizes (e.g. 4x4 or 16x16)

Visualize solving steps

🙋‍♂️ Author
MAHASIN
If you liked this project, feel free to ⭐ the repo and connect with me!

