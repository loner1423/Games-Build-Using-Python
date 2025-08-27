# """
# Sudoku Solver (backtracking)
# Run: python sudoku_solver.py
# """
# def print_board(board):
#     for r in range(9):
#         if r%3==0: print("+-------+-------+-------+")
#         row=""
#         for c in range(9):
#             if c%3==0: row+="| "
#             row+=(str(board[r][c]) if board[r][c]!=0 else ".")+" "
#         row+="|"
#         print(row)
#     print("+-------+-------+-------+")

# def find_empty(board):
#     for r in range(9):
#         for c in range(9):
#             if board[r][c]==0: return r,c
#     return None

# def valid(board,r,c,n):
#     if any(board[r][x]==n for x in range(9)): return False
#     if any(board[x][c]==n for x in range(9)): return False
#     br,bc=3*(r//3),3*(c//3)
#     for i in range(br,br+3):
#         for j in range(bc,bc+3):
#             if board[i][j]==n: return False
#     return True

# def solve(board):
#     pos=find_empty(board)
#     if not pos: return True
#     r,c=pos
#     for n in range(1,10):
#         if valid(board,r,c,n):
#             board[r][c]=n
#             if solve(board): return True
#             board[r][c]=0
#     return False

# if __name__=="__main__":
#     puzzle=[[5,3,0,0,7,0,0,0,0],
#             [6,0,0,1,9,5,0,0,0],
#             [0,9,8,0,0,0,0,6,0],
#             [8,0,0,0,6,0,0,0,3],
#             [4,0,0,8,0,3,0,0,1],
#             [7,0,0,0,2,0,0,0,6],
#             [0,6,0,0,0,0,2,8,0],
#             [0,0,0,4,1,9,0,0,5],
#             [0,0,0,0,8,0,0,7,9]]
#     print("Sudoku puzzle:")
#     print_board(puzzle)
#     if solve(puzzle):
#         print("Solved:"); print_board(puzzle)
#     else: print("No solution.")
import tkinter as tk
from tkinter import messagebox

# ---------------- Backtracking Solver Logic ----------------
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def valid(board, r, c, n):
    if any(board[r][x] == n for x in range(9)):
        return False
    if any(board[x][c] == n for x in range(9)):
        return False
    br, bc = 3 * (r // 3), 3 * (c // 3)
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == n:
                return False
    return True

def solve(board):
    pos = find_empty(board)
    if not pos:
        return True
    r, c = pos
    for n in range(1, 10):
        if valid(board, r, c, n):
            board[r][c] = n
            if solve(board):
                return True
            board[r][c] = 0
    return False

# ---------------- Tkinter GUI ----------------
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.original = [[False for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        validate = self.root.register(self.validate_input)

        for box_row in range(3):
            for box_col in range(3):
                frame = tk.Frame(
                    self.root,
                    highlightbackground="black",
                    highlightthickness=2,
                    bd=1
                )
                frame.grid(row=box_row, column=box_col, padx=2, pady=2)

                for r in range(3):
                    for c in range(3):
                        row, col = box_row * 3 + r, box_col * 3 + c
                        entry = tk.Entry(
                            frame, width=3, font=("Arial", 18), justify="center",
                            validate="key", validatecommand=(validate, "%P")
                        )
                        entry.grid(row=r, column=c, padx=1, pady=1)
                        self.entries[row][col] = entry

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(frame, text="Solve", bg="green", fg="white", width=12, command=self.solve_puzzle).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Clear", bg="red", fg="white", width=12, command=self.clear_grid).grid(row=0, column=1, padx=5)

    def validate_input(self, value):
        return value == "" or (value.isdigit() and 1 <= int(value) <= 9)

    def read_board(self):
        board = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.entries[r][c].get().strip()
                if val:
                    row.append(int(val))
                    self.original[r][c] = True
                    self.entries[r][c].config(fg="blue")
                else:
                    row.append(0)
                    self.original[r][c] = False
                    self.entries[r][c].config(fg="black")
            board.append(row)
        return board

    def write_board(self, board):
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)
                self.entries[r][c].insert(0, str(board[r][c]))
                self.entries[r][c].config(fg="blue" if self.original[r][c] else "green")

    def solve_puzzle(self):
        board = self.read_board()
        if solve(board):
            self.write_board(board)
            messagebox.showinfo("Sudoku Solver", "Puzzle Solved!")
        else:
            messagebox.showwarning("Sudoku Solver", "No solution found.")

    def clear_grid(self):
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)
                self.entries[r][c].config(fg="black")
                self.original[r][c] = False

# ---------------- Main ----------------
if __name__ == "__main__":
    root = tk.Tk()
    SudokuGUI(root)
    root.mainloop()
