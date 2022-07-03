'''Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
time_remaining = 90 - int(age)

weeks = time_remaining * round(52.1428571)

days = time_remaining * 365

months = time_remaining * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")