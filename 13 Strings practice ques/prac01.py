# text="My name is John and I am 25 years old."
# vowels=['a','e','i','o','u']
# sum=0
# for char in text.lower():
# 	if (char in vowels):
# 		sum+=1
# 		print(f"{char} is a vowel")

# print(f"total vowels {sum} present")
#-----------------------------------------------------------------
#Palindrome program
# text="aamaa"

# # if (text[::-1]==text[::1]):
# if (text == text[::-1]):
#     print(f"the string {text} is a palindrome")
# else:
#     print(f"the string {text} is not a palindrome")
#-----------------------------------------------------------------
#Print the reversed string word by word
#text="Learning python is very easy"
text=input("Enter some string: ")
l1=text.split()
print(l1)
l2=l1[::-1]
print(l2)
l3=' '.join(l2)
print(l3)

