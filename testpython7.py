#testpython7

fp = open("input.txt", "r")

#### print(fp.read())
#### print(fp.read(25))
print()
print()

# readlines    -   wil put all the content in file into list. so 1 line is 1 things inside a list, 2nd line is the 2 things in the list

# readline     -   will read line by line. if execute another so it will output the next line and next and next

#print(fp.readlines()[:2])

for x in fp:
	print(x)

print()
print()
# write mode. will flush the content and write new things in the file
# w  mode - will only write to file. cannot read
# w+ mode - can write to file and also read the file

fw = open("input2.txt", "w+")
print(fw.tell())
fw.write("new file has been created!")
print(fw.tell())
# tell()  -  will tell the position of the pointer in the file before/after the operation

content = fw.read()
print(fw.tell())

# seek()  -  to change the pointer position inside the file
# seek() will need offset and position
# seek(offset, position)
# position --> 0 start of the file, 1 - current postion, 2 - end of the file