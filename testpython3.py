#Conditional Statement
"""
if [conditions]:
	statements
elif [conditions]:
	statements
else:
	statements

"""

num1 = 100
num2 = 200
num3 = 300

if num1 > num2:
	print("Num1 is greater than num2")
elif num2 > num1 :
	print("Num2 is greater than num1")
else:
	print("Neither is greater")

print()

# looping
# for [var name] in [iterable data types]
#	statements
#
#	str list tuple dict set

l = [10,20,30,40]

for value in l:
	print(value, end = " ", flush = False)
print(flush = True)

sum = 0

for val in l:
	sum+= val
	print(sum)
print()

for nu in range(50,100,10):
	print(nu)

for test in l:
	print(test)
	if test == 10:
		print("Found!")
		break
else:
	print("Not Found")

print("outside")
print()

for index,test in enumerate(l):
	print(index,test)

# while already know

# divisible by 5 and 7
for nom in range(1500,2700):
	if(nom % 7 == 0 and nom % 5 == 0):
		print(nom)

numbers = [1,2,3,4,5,6,7,8,9]

#even and odd 
even = 0
odd = 0
for x in numbers:
	if(x % 2 == 0):
		print("even num", x)
		even+=1
	else:
		print("Odd num", x)
		odd+=1

print("even number: {} \nOdd number: {}".format(even, odd))