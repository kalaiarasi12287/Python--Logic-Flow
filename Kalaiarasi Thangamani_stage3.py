# Student Grade Calculator
"""
Task: Calculate student grade based on marks in 3 subjects.

Input: Student name, 3 subject marks (0-100)

Calculate:

Total marks
Percentage = (total/300) * 100
Grade Logic:

A: >= 75%
B: >= 60%
C: >= 40%
F: < 40%
Output: Name, Total, Percentage, Grade

Example:

Input: Raj, 80, 70, 90
Output:
Raj
Total: 240/300
Percentage: 80.0%
Grade: A
"""


def grade_calculate(name, mark1, mark2, mark3):

    total = mark1 + mark2 + mark3
    percentage = (total / 300) * 100

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    elif percentage < 40:
        grade = "F"

    print(name)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")


name = input("Enter the name of the student: ")
mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))

grade_calculate(name, mark1, mark2, mark3)
