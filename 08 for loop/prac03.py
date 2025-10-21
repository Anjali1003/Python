#Print the multiplication table of a number (entered by user).

num= int(input("Enter a num you want table of: "))

for i in range(1, 11):
	print(num, " X ",  i ," = ", num*i)