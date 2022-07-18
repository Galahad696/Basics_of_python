for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            number = "FizzBuzz"
        else:
            number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    print(number)