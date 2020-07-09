print("Hello World!")

first = 10
second = 20

a = 30
b = 30
addition = first + second

print(addition)
print(id(addition))
print(type(first),type(second))
print(id(first),id(second))

print(id(a),id(b))

num2 = 12.44
print(type(num2))

s = "Hello 'Python'"
print(s, type(s))

# List - can modify in the same memory location
l = [10,20,30,40,"string"]
print(l, type(l), id(l))

l.append(60)
print(l, id(l))

for i in l:
  print(i, type(i), end = " ", flush = True)

print(flush = False)
print("this is a test")

print()
# Tuple
t = (10,20,30)
print(t)
print()

#dict
d = {"name":"thor","email":"test@tst.com"}
print(d['email'])

#set
s = {10,20,30,40}

#bool
# True / False  <---- capital letter

# Complex
#eg: 4 + 3j


