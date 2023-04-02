# Taking input from user
marks_obtained = float(input("Enter the marks obtained: "))
total_marks = float(input("Enter the total marks: "))

# Calculating the percentage
percentage = (marks_obtained/total_marks) * 100

# Checking the grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

# Displaying the result
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")