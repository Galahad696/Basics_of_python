import random

rock = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
   _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

#Ask the users what they choose
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
   print("You typed an invalid number. You lose.\n")
else:
    print("You chose:\n", game_images[choice])
# if choice == 0:
#     print(f'{rock}\nYou chose rock.')
# elif choice == 1:
#     print(f'{paper}\nYou chose paper.')
# elif choice == 2:
#     print(f'{scissors}\nYou chose scissors.')
#if choice >= 3 or choice < 0:
   #print("You typed an invalid number. You lose.")

computer_choice = random.randint(0,2)
print("Computer chose:\n", game_images[computer_choice])
# if computer_choice == 0:
#     print(f'{rock}\nComputer chose rock.\n')
# elif computer_choice == 1:
#     print(f'{paper}\nComputer chose paper.\n')
# else:
#     print(f'{scissors}\nComputer chose scissors.\n')

if choice == computer_choice:
    print("We have a draw.")
else:
    if choice == 0 and computer_choice == 2:
        print("You won!")
    elif choice == 2 and computer_choice == 0:
        print("Computer won!")
    elif computer_choice > choice:
        print("Computer won!")
    elif choice >= 3 or choice < 0:
        print("Computer won! Type a valid number.")
    elif choice > computer_choice:
        print("You won!")

