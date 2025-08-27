"""
Number Guessing Game
Run: python number_guess.py
"""
import random

def main():
    target = random.randint(1, 100)
    tries = 0
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid integer."); continue
        tries += 1
        if guess < target: print("Too low!")
        elif guess > target: print("Too high!")
        else:
            print(f"Correct! Attempts: {tries}")
            break

if __name__ == "__main__":
    main()
