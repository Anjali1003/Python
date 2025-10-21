#Ask the user to enter a day number (1–7) and print the corresponding day of
#the week using match case .


	
num = int(input("Enter a day number (1–7) : "))

match num:

	case 1:
		print("Its a Sunday...!")
	case 2:
		print("Its a Monday")
	case 3:
		print("Its a Tuesday")
	case 4:
		print("Its a Wednesday")
	case 5:
		print("Its a Thrusday")
	case 6:
		print("Its a Friday")
	case 7:
		print("Its a Sturday")
	case _:
		print("Ist not a day")