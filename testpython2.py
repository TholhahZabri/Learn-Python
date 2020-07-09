#python operators
# + , - , * , / , // , % , **

num1 = 10
num2 = 20

print(num1 ** num2)
print(num1 // 3)
print(num1 % 3)

#Comparison operators
# < , > , <= , >= , == , !=

print(num1 == num2)
print(num1 <= num2)
print(num1 < 10)
print(num1 <= 10)

#Identity operators

n1 = 100
n2 = 200

print()
print(n1 is n2)
print(n1 is not n2)

no1 = [10,20,30]
no2 = [10,20,30]

print()
print(no1 == no2)   #will return true because the value is same
print(no1 is no2, id(no1), id(no2))   # will return false because the location of memory is not the same even same value

#Assignment operator
# = , += , -= , *= , /=
nom1 = 100
print()
print(nom1)

nom1 = nom1 + 5   # Same as nom1 += 5
print(nom1)

nom1 -= 5  # same as nom1 = nom1 - 5
print(nom1)

#Bitwise operator
# & , | , ^ , >> , <<
nu1 = 2
print(bin(nu1))

nu2 = 1
print(bin(nu2))

print(nu1 & nu2)  # perform AND bitwise operation. binary 10 and 1 . will be 0
print(nu1 | nu2)  # perform OR bitwise operation. binary 10 and 1 . will be 3
print(nu1 >> 1)  # move binary 1 to the left, so 10 will be 01

#Logical operators
# and , or , not
print(10 == 10 and 20 == 20) # True, both must be true the it is true
print(10 == 20 and 30 == 30) #False because not both is true. 1 is false. so false
print(not(10 == 10))  # False. because it is true, then the answer is being NOT the ans

l = [10, 20, 30, 40, 50]
print(30 in l)  # will print true as the 30 is inside the list, so it is true

s = "Python String"
print("Python" in s) # will return true. because Python words is in the sentence. Case sensitive
print("Python" not in s) # False, because Python words is exist inside the string

