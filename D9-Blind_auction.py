#from replit import clear
from blind_auction_art import logo

print(logo)
# HINT: You can call clear() to clear the output in the console.

users = {}
ask = True
while ask == True:
    user_name = input("What is your name: ")
    user_bid = int(input("What's your bid? $"))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    users[user_name] = user_bid
    #if other_bidder == "yes":
        #clear()
    if other_bidder == "no":
        ask = False
        #clear()
    else:
        #clear()
        print("Type only 'yes' or 'no' to the third question.")

max_bid = max(i for i in users.values())
max_bidder = max(users, key=users.get)
print(f"The winner is {max_bidder} with a bid of ${max_bid}.")