print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

#How much each one should pay taking in account the choosed tip? (bill + tip percentage) / people
#final_payment = round(((bill + ((bill*tip_percentage)/100)) / people), 2)

#This one really round the number with decimal places, even if the second number is zero.
final_payment = "{:.2f}".format((bill + ((bill*tip_percentage)/100)) / people)

final_message = f"Each person should pay: ${(final_payment)}"

print(final_message)