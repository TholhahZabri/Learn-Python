#testpython6

# map
# filter
# lambda

def sqr(num1):
	return num1**2

l = [13,20,37,40,50,60]
l2 = [2,3,4,5,6,7]
result = list(map(sqr,l))

#for value in result:
#	print(value)
print(result)
print(list(map(lambda no1:no1**2, l)))
print()

def add(x,y):
	return x + y

r2 = list(map(add, l, l2))
print(r2)


def check_num(x):
	if x % 2 == 0:
		return True
	else:
		return False

print()
r3 = list(filter(check_num,l))
print(r3)
print(list(filter(lambda no1: no1 % 2 == 0, l)))

print()

d = {1:50, 2:40, 3:30 , 4:20 , 5:10}

print(sorted(d.items(), key= lambda x:x[1]))



######################

# Generators

#normal flow of functions
def printVal(x):
	for value in x:
		print(value)

printVal(l)

##

# generators function

def fibo():
	f = 0
	s = 1
	while(True):
		next_val = f + s
		yield next_val      #put yield it will become generator functions
		f,s = s,next_val

g = fibo()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print()
print()
#########
# Iterator and itertools

no2 = [10,20,30,40,50]
no3 = iter(no2)

#print(next(no3))

for i in no3:
	print(i)

print()
print()

# itertools

import itertools   # itertools.chain, itertools.cycle, itertools.tee, itertools.islice, itertools.permutations, itertools.combinations

li1 = [10,20,30,40,50]
li2 = [101,201,301,401,501]
li3 = [102,202,302,402,502]

i = itertools.chain(li2,li2,li3)

for x in i:
	print(x)