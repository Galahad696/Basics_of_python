
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


#Calculates the highest value
max_value = 0
for number in student_scores:
    if number > max_value:
        max_value = number


print(f"The highest score in the class is: {max_value}.")

