#Write a program using match case that simulates a simple calculator.
#Ask the user for two numbers and an operation (+, -, *, /).
#Perform the operation using match case .


num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

operation = (input("Enter opration you want to perform (+, -, *, /): "))

match operation:

	case '+':
		print("Addition of nums are: ", num1+num2)
	case '-':
		print("Substraction of nums are: ", num1-num2)
	case '*':
		print("Multiplication of nums are: ", num1*num2)
	case '/':
		print("Division of nums are: ", num1/num2)
	case _:
		print("invalid operation!!!")