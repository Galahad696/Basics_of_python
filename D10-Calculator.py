# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    from calculator_art import logo
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    finish = False
    while not finish:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        question = input(
            f"Type 'y' to continue calculating with {answer}, or typo 'n' to start a new calculation.: ").lower()
        if question == "y":
            num1 = answer
        elif question == "n":
            finish = True
            calculator()


calculator()