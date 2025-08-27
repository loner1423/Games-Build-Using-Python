"""
Rock, Paper, Scissors vs Computer
Run: python rock_paper_scissors.py
"""
import random

CHOICES = ["rock", "paper", "scissors"]

def outcome(player, comp):
    if player == comp: return "Draw"
    wins = {("rock","scissors"),("scissors","paper"),("paper","rock")}
    return "Win" if (player, comp) in wins else "Lose"

def main():
    print("Rock Paper Scissors. Type quit to stop.")
    while True:
        player = input("Your choice (rock/paper/scissors): ").lower().strip()
        if player == "quit": break
        if player not in CHOICES:
            print("Invalid choice."); continue
        comp = random.choice(CHOICES)
        print(f"Computer: {comp}. Result: {outcome(player, comp)}\n")

if __name__ == "__main__":
    main()
