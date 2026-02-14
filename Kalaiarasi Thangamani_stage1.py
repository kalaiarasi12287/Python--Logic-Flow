# Basic Calculator
"""
Create a calculator that takes two numbers and an operator (+, -, *, /) and shows the result.

Constraints:

Handle division by zero
Use if-elif-else statements
Example:

Input: 10, 5, +
Output: Result = 15

"""
def calc(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!!")
            return
        else:
            result = num1 / num2
    else:
        print("Enter valid operator")
        return

    print(f"Result = {result}")


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
op = input("Enter an operator (+, -, *, /): ")
calc(number1, number2, op)
