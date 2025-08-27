"""
2048 Game (Tkinter)
Run: python game_2048.py
"""
import tkinter as tk, random

SIZE=4

def new_game():
    return [[0]*SIZE for _ in range(SIZE)]

def add_tile(board):
    empty=[(r,c) for r in range(SIZE) for c in range(SIZE) if board[r][c]==0]
    if not empty: return
    r,c=random.choice(empty)
    board[r][c]=2 if random.random()<0.9 else 4

def compress(board):
    changed=False
    new=[[0]*SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        pos=0
        for c in range(SIZE):
            if board[r][c]!=0:
                new[r][pos]=board[r][c]; pos+=1
        if new[r]!=board[r]: changed=True
    return new,changed

def merge(board):
    changed=False
    for r in range(SIZE):
        for c in range(SIZE-1):
            if board[r][c]!=0 and board[r][c]==board[r][c+1]:
                board[r][c]*=2; board[r][c+1]=0; changed=True
    return board,changed

def reverse(board): return [row[::-1] for row in board]
def transpose(board): return [list(row) for row in zip(*board)]

def move_left(board):
    c1,_=compress(board)
    m,_=merge(c1)
    c2,_=compress(m)
    return c2

def move_right(board): return reverse(move_left(reverse(board)))
def move_up(board): return transpose(move_left(transpose(board)))
def move_down(board): return transpose(move_right(transpose(board)))

class Game2048(tk.Frame):
    def __init__(self):
        super().__init__()
        self.grid(); self.master.title("2048")
        self.board=new_game(); add_tile(self.board); add_tile(self.board)
        self.cells=[]
        for r in range(SIZE):
            row=[]
            for c in range(SIZE):
                f=tk.Frame(self,bg="lightgrey",width=100,height=100)
                f.grid(row=r,column=c,padx=5,pady=5)
                l=tk.Label(f,text="",bg="lightgrey",font=("Arial",24,"bold"))
                l.place(relx=0.5,rely=0.5,anchor="center")
                row.append(l)
            self.cells.append(row)
        self.update_ui()
        self.master.bind("<Key>",self.key)

    def update_ui(self):
        for r in range(SIZE):
            for c in range(SIZE):
                v=self.board[r][c]
                self.cells[r][c].config(text=str(v) if v else "", bg="lightyellow" if v else "lightgrey")

    def key(self,e):
        keymap={"Left":move_left,"Right":move_right,"Up":move_up,"Down":move_down}
        if e.keysym in keymap:
            nb=keymap[e.keysym](self.board)
            if nb!=self.board:
                self.board=nb; add_tile(self.board)
                self.update_ui()

if __name__=="__main__": Game2048().mainloop()
