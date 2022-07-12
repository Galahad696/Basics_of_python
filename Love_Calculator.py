# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name1 = name1.lower()
new_name2 = name2.lower()

t1 = new_name1.count('t')
t2 = new_name2.count('t')
r1 = new_name1.count('r')
r2 = new_name2.count('r')
u1 = new_name1.count('u')
u2 = new_name2.count('u')
e1 = new_name1.count('e')
e2 = new_name2.count('e')

total1 = t1+t2+r1+r2+u1+u2+e1+e2

l1 = new_name1.count('l')
l2 = new_name2.count('l')
o1 = new_name1.count('o')
o2 = new_name2.count('o')
v1 = new_name1.count('v')
v2 = new_name2.count('v')
e1 = new_name1.count('e')
e2 = new_name2.count('e')

total2 = l1+l2+o1+o2+v1+v2+e1+e2

score = f"{total1}{total2}"

new_score = int(score)
if new_score < 10 or new_score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif new_score >= 40 and new_score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")