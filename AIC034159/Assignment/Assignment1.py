# Write a program to calculate basic calculation of two numbers

# Input 2 number and operator from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

# Execute the calculation to 2 numberes with respect to operator
if (operator == "+") :
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif (operator == "-") :
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
elif (operator == "*") :
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
elif (operator == "/") :
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
else :
    print("Invalid operator")