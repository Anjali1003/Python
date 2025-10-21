l=[10,20,30,40,50,60]

p=0

while p<len(l):
	print(l[p])
	p=p+1

print("------------------------------")


#To print elements of list index wise:
l=[10,20,30,40,50,60]

i=0
while i < len(l):
	print("The element present at the +ve index : {} and at -ve index : {} is : {}".format(i,i-len(l),l[i]))
	i=i+1