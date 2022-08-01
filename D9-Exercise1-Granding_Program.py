student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


#Create an empty dictionary called student_gradees.
student_grades = {}

# Add the grades to student_grades.
for keys in student_scores:
    score = student_scores[keys]
    if score >= 91:
        student_grades[keys] = "Outstanding"
    elif score >= 81:
        student_grades[keys] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"


print(student_grades)