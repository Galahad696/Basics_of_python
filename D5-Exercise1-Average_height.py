#Ask the students height's and  turn them into integers
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])



#Calculate the total elements of the list and the sum
soma = 0
total = 0
for height in student_heights:
    soma += height
    total += 1
#Calculate the average
media = soma/total

print(round(media))