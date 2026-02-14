#Add Result Check
"""
Extend Stage 1: After showing result, check if it's positive, negative, or zero and print accordingly.

Example:

Input: 10, 5, -
Output: 
Result = 5
Positive
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

    if result < 0:
        print("Negative")
    elif result > 0:
        print("Positive")
    else:
        print("Zero")


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
op = input("Enter an operator (+, -, *, /): ")
calc(number1, number2, op)
