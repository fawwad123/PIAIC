# Input 2 number and operator from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

if (operator == "+") :
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif (operator == "-") :
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
elif (operator == "*") :
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
elif (operator == "-") :
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))

    
