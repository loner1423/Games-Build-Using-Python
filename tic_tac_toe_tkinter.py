"""
Tic-Tac-Toe with Tkinter GUI
Run: python tic_tac_toe_tkinter.py
"""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [" "] * 9
turn = ["X"]

buttons = []

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board: return "Draw"
    return None

def click(i):
    if board[i] != " ":
        return
    board[i] = turn[0]
    buttons[i]["text"] = turn[0]
    w = check_winner()
    if w:
        if w == "Draw":
            messagebox.showinfo("Game Over","It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {w} wins!")
        reset()
    else:
        turn[0] = "O" if turn[0] == "X" else "X"
        status["text"] = f"Turn: {turn[0]}"

def reset():
    for i in range(9):
        board[i] = " "
        buttons[i]["text"] = " "
    turn[0] = "X"
    status["text"] = "Turn: X"

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()
for i in range(9):
    btn = tk.Button(frame, text=" ", width=5, height=2, font=("Arial", 24),
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

controls = tk.Frame(root)
controls.pack(pady=5)
status = tk.Label(controls, text="Turn: X", font=("Arial", 14))
status.pack(side="left", padx=5)
reset_btn = tk.Button(controls, text="Reset", command=reset)
reset_btn.pack(side="left", padx=5)

root.mainloop()
