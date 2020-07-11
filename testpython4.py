#testpython4
s = "Strings test"
print(id(s))

s = "abcdefghijklmnopqrstuvwxyz"
print(id(s))

#indexing
print(s[-4])

#slicing
print(s[0:6])
print()
print(s[6:])
print(s[:6])

#stride
print()
print(s[::3])
print(s[::-2])

for value in s:
	print(value)

print()

for value in s[::2]:
	print(value)

#format
# print using {} then add .format(num1,num2) after end of strings print which is "eg la lal".format()

#s1 = s.capitalize()
#will caps the front string.
#got another function too. upper, lower, title
#upper = all caps, lower = all to lower, title = convert start string to caps

#check with function, will return boolean (true / false)
#isupper() , islower(), istitle()

print()
#split , join
s1 = "html,python,java,php"
l = s1.split(",")
print(l)

s2 = (" ").join(l) #join list of l and put space in between them
print(s2)

#maketrans
#translate
s3 = "abcd"
s4 = "1234"

print()
s5 = "python sample string abcd we got string another  string"
table = str.maketrans(s3,s4)
#s6 = s5.translate(table)
#print(s6)
print(s5.translate(table))

#index
#find
#rfind
print()
print("python" in s5)
print(s5.index("sample"))
print(s5.find("string")) #will return -1 if not find inside the searching
print(s5.rfind("string")) # will return index of finding that found start from right

print()
#stip()  will strip any char we state from start string and from end string eg: space
#lstrip() will remove from left only
#rstrip() will remove from right only
strnew = "*******start here******end here********"
print(strnew.strip("*"))
print(strnew.lstrip("*"))
print(strnew.rstrip("*")) 


#center, ljust, rjust
#will add char we specified to make sure complete the words total char we want
#eg
sttr = "python,html,php"
print(sttr.center(20,"^"))
print(sttr.ljust(20,"_"))
print(sttr.rjust(20,"-"))

#replace
print()
print(sttr.replace("html","django"))
print(sttr)
