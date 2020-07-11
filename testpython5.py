#testpython5
#list - mutable (can update, delete and add)
l = [1,2,3,4,"java","python","html",['a','b','c']]
print(l,type(l))
print()

print(l[7][-1])

#append() append value(s) at last but as 1 form even many val is add
l.append(600)
print(l)

#extend([val,val,val]) add value(s) at last, but as separate form
print()
l.extend([400,500,600])
print(l)

print()
l.extend(["testing boi"])
print(l)

#insert() insert in any index you want, then shift other value to right
l.insert(1,"test")
print(l)

#l2 = l.copy() #better use copy instead declare direct l2 = l, bcz they'll share memory so if l is change l2 will change too. if use copy, then they wont share memory

#update element of list
#l[2] = 300 . this will update the content of index 2 to be 300

#delete element got so many
#pop(), pop(2) will pop last element or element based on index given
#remove(), will remove the element given instead put index. eg: remove("test"), remove test
#remove() will just remove first occurence of element we want to remove
#clear(l) will clear all element in the list
#del l , will delete the list from memory. totally delete


#l2 = [1,2,3,'a','b','e','c']
l2 = ['a','b','e','c']
print(l2)
l2.reverse()
print(l2, l2.count('a'))

#dict
d = {"id":1,"name":"aaa","email":"a@a.com"}
print(d)
print(type(d['id']))
print(d["email"])

d["contact_num"] = 1234
print(d)
print()

print(d.get("email1","takwujud"))
print(d.setdefault("email1","bbb@b.com"))
print(d)

print()
for x in d:
	print(x, d[x])

di = {}
for i in range(1,11): #if pun in range(10), value will start from 0 -9
	di[i] = i * i		  # but this, value will start from 1-10

print(di)

print()
#if want print keys only then can use this
print(d.keys())

#if want print values only then can use this
print(d.values())

#if want print items inside the dict
print(d.items())


#convert list to dict
l3 = ["name", "nom", "emails"]
l4 = ["saya", 134567, "abc@abc.com"]

print()
dict1 = dict(zip(l3,l4))
print(dict1)

#create keys only
dict2 = dict.fromkeys(l3,"takda") #set l3 as keys and takda as default value depa
print()
print(dict2)

#gabung dict utk jd 1 dict

d5 = {1:1, 2:16, 3:9, 7:17}
d6 = {1:5, 4:20}		#l6 punya key 1 punya value akan update key 1 dr l5

d5.update(d6)   # gabung both keys
print(d5)

#delete item from dict
# pop, popitem, clear, del

r = d5.pop(2)  #remove key 2 and its value 
print(d5, r)   


r = d5.popitem()   #will pick random key and pop it. it will pop both key and item
print(r)  # will print the key and item

# d5.clear() will clear all keys and item inside the dict
# d5.del() will delete the dictionary itself

# sets:
# immutable data, all elements should be unique, all element should be immutable( int, float, tuple, str) and sets are unordered

sets = {102,20,20,30,40,50,10,60}
sets2 = {101,20,20,30,40,50,10,602}

print()
print(sets)   #will only print unique and not redundat data. unordered

#add data to sets
sets.add(600)
print(sets)

#combined sets using union. 
#eg: sets3 = sets.union(sets2)
#will combine sets and sets2. but duplicate will not have. unique

#intersection()  will print element that intersect in sets and sets2
print(sets.intersection(sets2))

#difference()  will print element that are not duplicate in when 2 sets intersect
print(sets.difference(sets2))

#symmetric_difference() will only output element that not intersect in both element. combine both but same will be removed
print(sets.symmetric_difference(sets2))

#update() update the sets with another sets value
#sets.update(sets2)
#print(sets)

#sets.intersection_update(sets2)  update the sets only with intersection val
#sets.difference_update(sets2) update the sets only with diff between them
#sets.symmetric_difference_update(sets) update sets only with sym_diff

#sets2.issubset(s1) will return True if all val in sets2 is in sets
#sets.superset(sets2) will return True if sets value is superset all val sets2

# convert list to set
# s = l1.set()   so if got duplicate will be unique also. dupp remove
#
# sets to list
# l = s.list(), so when use list, we can use sort

# pop     will remove random element in sets. wont accept any argument. random. will return the pop element in the new variable if give.

# remove  will remove element in sets. need argument. element as argument to remove the element in sets. if element not exist. will output error

# discard  will delete the element . eg sets.discard(600), will remove 600 from the list. if element not exist. will not output error

# clear will clear all the elements

# del  will delete the the sets itself

print(sum(sets))  #will sum all elements in the list,sets
print(max(sets))  #will print max number inside the sets/list
print(min(sets))  #will output min inside the list/sets

print(round(2.522276))  #will rouund off the val .
print(round(5.43126,4))	#will round off the val in 4 decimal place


#math in python
# need to import math
# math.fsum  floating summation
# math.sum
# math.floor
# math.ceil
# math.sqrt
# math.factorial
# math.modf    separate decimal part and integer part. can also be use like this
# d , i = math.modf(44.5556)  so i = 44 , d = 0.5556
#
# math.pow(19,2)
# math.log(10,2)   log base 2 of 10
# math.log2(10)
# math.log10(2)
#
# math.sin(0)
# math.sin(math.radians(20))
# math.cos(math.radians(20))
# math.tan(math.radians(20))
#
#
# if want to use random
# import random
#
# print(random.random())  will use random function inside random lib
#
# pick random number based on variable

import random

l = [1,2,3,4,5,6]
print(random.choice(l))
print(random.uniform(10,11))  # will give floating random number
print(random.randint(10,20))

# randint vs randrange . 
# rantint(1,3) will give 1 to 3 as random number
# randrange(1,3) will only give 1 to 2 as random number