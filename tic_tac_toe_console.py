"""
Tic-Tac-Toe (2 players, console)
Run: python tic_tac_toe_console.py
"""
BOARD = [" "] * 9

def print_board():
    b = BOARD
    print(f"\n {b[0]} | {b[1]} | {b[2]}")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]}\n")

def winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if BOARD[a] != " " and BOARD[a] == BOARD[b] == BOARD[c]:
            return BOARD[a]
    if " " not in BOARD: return "Draw"
    return None

def main():
    turn = "X"
    print("Tic-Tac-Toe — positions 1..9")
    print_board()
    while True:
        try:
            pos = int(input(f"Player {turn}, choose position (1-9): ")) - 1
            if pos not in range(9) or BOARD[pos] != " ":
                print("Invalid move. Try again."); continue
        except ValueError:
            print("Enter a number 1-9."); continue
        BOARD[pos] = turn
        print_board()
        w = winner()
        if w:
            if w == "Draw": print("It's a draw!")
            else: print(f"Player {w} wins!")
            break
        turn = "O" if turn == "X" else "X"

if __name__ == "__main__":
    main()
