import random
from D14_higher_lower_art import logo
from D14_higher_lower_art import vs
from D14_higher_lower_data import data

# Logo
print(logo)


# Random choice in data list.
def choice():
    """Generates a random list element to compare with."""
    return random.choice(data)


# Function to compare the followers.
def compare(answer, aleatory_choice1, aleatory_choice2):
    """Takes the user answer and return if they are right(True) or wrong(False)."""
    if answer == 'a':
        if aleatory_choice1['follower_count'] > aleatory_choice2['follower_count']:
            return True
        else:
            return False
    elif answer == 'b':
        if aleatory_choice2['follower_count'] > aleatory_choice1['follower_count']:
            return True
        else:
            return False


# Function to play the game.
def play():
    score = 0
    play_the_game = True

    choice1 = choice()
    choice2 = choice()

    # Substitute the second option of comparison if the player guess right.
    while play_the_game:
        if score > 0:
            choice1 = choice2
            choice2 = choice()

        # Makes sure that the options of comparison are different
        while choice1 == choice2:
            choice2 = choice()

        print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}. ")
        print(vs)
        print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}. ")

        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        compare(choose, choice1, choice2)

        print(logo)

        if choice1['follower_count'] > choice2['follower_count'] and compare(choose, choice1, choice2) == True:
            score += 1
            print(f"You're right! Current score: {score}")
        elif choice2['follower_count'] > choice1['follower_count'] and compare(choose, choice1, choice2) == True:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"You lose. Final score: {score}")
            play_the_game = False


play()





