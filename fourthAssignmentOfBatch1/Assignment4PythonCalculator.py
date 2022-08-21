# This is my regular assignment.
# Written by Rafat Karim.
Num1 = float(input("Enter a number:"))
Operator = input("Enter a operator")
Num2 = float(input("Enter another number:"))
if Operator == "+":
    print("Your result is",Num1 + Num2)
elif Operator == "-":
    print("Your result is",Num1 - Num2)
elif Operator == "*":
    print("Your result is",Num1 * Num2)
elif Operator == "/":
    print("Your result is",Num1 / Num2)
elif Operator == "**":
    print("Your result is",Num1 ** Num2)
elif Operator == "//":
    print("Your result is",Num1 // Num2)
elif Operator == "%":
    print("Your result is",Num1 % Num2)
else:
    print("Please enter a operator")