# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def report():
    """Report the resources available"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print (f"Money: ${profit}")

def resources_enough(choice):
    """Check if there is resources enough to attend the customer request"""
    if MENU[choice]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
        if MENU[choice]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
            if question != "espresso":
                if MENU[choice]['ingredients']['milk'] > resources['milk']:
                    print("Sorry there is not enough milk.")
    else:
        return True

def process_coins(quarter, dime, nickle, pennie):
    """Process the coins and give the change or refund the money if it's insufficient."""
    total = (0.25 * quarter) + (0.1 * dime) + (0.05 * nickle) + (0.01 * pennie)
    if total >= MENU[question]['cost']:
        change = round(total - MENU[question]['cost'], 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
machine_on = True
while machine_on:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if question == 'report':
        report()

    elif question == 'espresso':
        if resources_enough(question):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            if process_coins(quarters, dimes, nickles, pennies):
                print(f"Here is your {question} ☕. Enjoy!")
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            profit += 1.5

    elif question == 'cappuccino':
        if resources_enough(question):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            if process_coins(quarters, dimes, nickles, pennies):
                print(f"Here is your {question} ☕. Enjoy!")
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            profit += 3.0
    elif question == 'latte':
        if resources_enough(question):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            if process_coins(quarters, dimes, nickles, pennies):
                print(f"Here is your {question} ☕. Enjoy!")
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
            profit += 2.5

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif question == "off":
        print("Goodbye")
        machine_on = False
    else:
        print("Write properly.")

