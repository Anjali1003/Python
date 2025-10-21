# #Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break ).
# for i in range(1, 11):
# 	print(i)
# 	if (i==7):
# 	    break

# #Print numbers from 1 to 10, skipping the number 5 (use continue )

# for i in range(1, 11):
# 	if (i==5):
# 		continue #skips 5 and continues to next iteration
# 	print(i)


#Write a loop that goes through numbers 1 to 5, but does nothing for number
#3 (use pass ).

# for i in range(1, 6):
# 	if (i==3):
# 		pass
# 	print(i)

for i in range(1, 6):
	match i:
		case 1:
			print(1)
		case 2:
			print(2)
		case 3:
			pass
		case 4: 
			print(4)
		case 5:
			print(5)
		case _:
			print("Invalid")
