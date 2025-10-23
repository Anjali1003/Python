l=[10,20,30,2,2,2,3,4,8]

x= int(input("Enter element to count its occurence: "))

if x in l:
    print("{} is present at index {}".format(x,l.index(x)))
else:
    print("{} is not present in the list".format(x))

print(l.count(2))
print(l.index(30))
print(len(l))