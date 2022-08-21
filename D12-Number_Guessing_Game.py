# A number guessing game
import random
from number_guessing_art import logo

hard = 5
easy = 10

# Allow the player to submit a guess for a number between 1 and 100.
n = random.randrange(0, 101)


"""Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. If they got the answer correct, show the actual answer to the player."""
def check(num):
    if num < n:
        print("""Too low.""")
    elif num == n:
        print(f"You won. The answer is {n}.")
    else:
        print("""Too high""")


# Track the number of turns remaining.
def hard_level(remain):
    """Track the remaining turns to hard level"""
    global hard
    hard -= 1
    if hard == 0:
        print("You've run out of guesses, you lose.")
    else:
        print(f"Guess again.\nYou have {hard} attempts remaining to guess the number.")


def easy_level(remain):
    """Track the remaining turns to easy level"""
    global easy
    easy -= 1
    if easy == 0:
        print("You've run out of guesses, you lose.")

    else:
        print(f"Guess again.\nYou have {easy} attempts remaining to guess the number.")



print(logo)
print(f"""Welcome to the Number Guessing Game!
I'm thinking of a number between 0 and 100""")
# print(f"Pssst, the correct answer is {n}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    print(f"You have {hard} attempts remaining to guess the number.")

else:
    print(f"You have {easy} attempts remaining to guess the number.")

ask = True
while ask:
    guess = int(input("Make a guess: "))
    check(guess)

    if guess == n:
        ask = False

    else:
        if difficulty == "hard":
            hard_level(hard)
            if hard == 0:
                ask = False
        else:
            easy_level(easy)
            if easy == 0:
                ask = False