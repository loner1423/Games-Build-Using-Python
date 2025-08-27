"""
Memory Puzzle (Tkinter)
Flip cards and match pairs
Run: python memory_puzzle.py
"""
import tkinter as tk, random

root = tk.Tk(); root.title("Memory Puzzle")
symbols = list("😀🐱🐶🍎🍌🍇🍒🍓🥑🥕🍕🍔")
cards = symbols*2; random.shuffle(cards)
buttons, revealed, first = [], {}, None

def click(i):
    global first
    if i in revealed: return
    btn = buttons[i]
    btn.config(text=cards[i])
    revealed[i] = cards[i]
    if first is None:
        first = i
    else:
        root.after(800, check, i)

def check(i):
    global first
    if cards[first] != cards[i]:
        buttons[first].config(text="?")
        buttons[i].config(text="?")
        del revealed[first], revealed[i]
    first = None
    if len(revealed)==len(cards):
        tk.Label(root, text="You win!", font=("Arial",20)).pack()

for i in range(len(cards)):
    b = tk.Button(root,text="?",width=4,height=2,font=("Arial",20),command=lambda i=i: click(i))
    b.grid(row=i//6,column=i%6,padx=5,pady=5)
    buttons.append(b)

root.mainloop()
