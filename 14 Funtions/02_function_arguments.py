# def add(a, b, plus=0):
#     x = a + b + plus
#     return x


# c = add(3, 5, 2)
# print(c)

# c1 = add(b=5, a=3)
# print(c1)


# def full_name(first, last):
# 	print(f"full name is {first} {last}")
	
# f=input("Enter First name: ")
# L=input("Eneter Last name: ")

# full_name(f, L)

# Write a function calculate_area(length, width=10) that returns the area of
# a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def area(length, breath=10):
	s= length * breath
	return s
	
L=int(input("Enter length: "))
#B=int(input("Eneter breath: "))

print(area(L ))
