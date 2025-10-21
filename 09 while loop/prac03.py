# Program to reverse a given number using a while loop

num = int(input("Enter a number: "))  # Example: 123
reverse_num = 0

while num > 0:
    digit = num % 10          # Get the last digit
    reverse_num = reverse_num * 10 + digit  # Build the reversed number
    num = num // 10           # Remove the last digit

print("Reversed number:", reverse_num)

for i in range(1, 11):
	print(i)
	if (i==7):
		break

