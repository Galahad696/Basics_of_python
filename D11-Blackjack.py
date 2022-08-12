############### Blackjack Project #####################
import random
#from replit import clear
from blackjack_art import logo



# deal the cards
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    #turno.append(card)
    return card


# Calculate the total of each hand
def calculate_score(cards):
    for card in cards:
        score = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return score

    return calculate_score

#Create a function called compare() and pass in the user_score and computer_score.
def compare(u_score, c_score):
    if u_score > 21 and c_score > 21:
        return "You went over. You lose."

    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has a Blackjack."
    elif u_score == 0:
        return "Win with a Blackjack."
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."
# Play the game
def play_game():
    #logo

    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you ant to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    #clear()
    play_game()


