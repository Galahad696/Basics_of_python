def prime_checker(number):
    prime = []

    for i in range(1, n + 1):
        if number % i == 0:
            prime.append(number)

    if len(prime) == 2:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
