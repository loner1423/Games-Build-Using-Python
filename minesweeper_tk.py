"""
Minesweeper (Tkinter)
Run: python minesweeper_tk.py
"""
import tkinter as tk, random

ROWS,COLS,MINES=8,8,10

class Cell(tk.Button):
    def __init__(self,master,r,c):
        super().__init__(master,width=3,height=1,font=("Arial",12),command=self.reveal)
        self.r,self.c=r,c; self.is_mine=False; self.adj=0; self.revealed=False
    def reveal(self):
        if self.revealed: return
        self.revealed=True
        if self.is_mine:
            self.config(text="*",bg="red")
            tk.messagebox.showinfo("Game Over","You hit a mine!")
            return
        self.config(text=str(self.adj) if self.adj>0 else "",relief="sunken",bg="lightgrey")
        if self.adj==0:
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr or dc:
                        nr,nc=self.r+dr,self.c+dc
                        if 0<=nr<ROWS and 0<=nc<COLS:
                            cells[nr][nc].reveal()

root=tk.Tk(); root.title("Minesweeper")
cells=[[Cell(root,r,c) for c in range(COLS)] for r in range(ROWS)]
for r in range(ROWS):
    for c in range(COLS):
        cells[r][c].grid(row=r,column=c)

# place mines
pos=random.sample([(r,c) for r in range(ROWS) for c in range(COLS)],MINES)
for r,c in pos: cells[r][c].is_mine=True
for r in range(ROWS):
    for c in range(COLS):
        if cells[r][c].is_mine: continue
        cells[r][c].adj=sum(1 for dr in (-1,0,1) for dc in (-1,0,1)
                            if dr or dc and 0<=r+dr<ROWS and 0<=c+dc<COLS and cells[r+dr][c+dc].is_mine)

root.mainloop()
