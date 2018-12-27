
'''

STRINGS

1. capitalize method
2. center () method:
3. Count ()
4. startswith ()
5. endswith()
6. find method
7.index

'''


# capitalize
name = "guido van rossum"
print("capitalize method:", name.capitalize())

print ("calling datatypes:", len(name), id(name))
#center - str,width,fill characters- name length is 16, so when we give 20 and fill as @, it prints @ prefix and suffix

print ("center method", name.center(25,'@'))

#count - str, count (counting o in names 0 - 17 is start and end index)
print ("count method: ", name.count('o'))
print ("count method: ", name.count('o',0,17))
check = 'o'
print ("count method: ", name.count(check))

# starts with checks if given sub-strings matches the values specified- o/p true or false.
print("startswith:", name.startswith('G',0,17))
print("startswith:", name.startswith('gui',0,17))

#endswith

print("endswith:", name.endswith('rossum',0,17))
print("endswith:", name.endswith('van',0,17))

#find method - search substring from start - end index and prints the position/index number of the variable string

print("find:", name.find('van',0,17))

#index: if condition true, prints the index of substring, if false gives error in code.(In find command if variable doesnt exist it gives -1)

print("index:", name.index('van',0,17))

print ("output:", len(name),id(name),type(name))

#isalnum method - checks alpha/numeric value and no special characters- condition is true/ false
nameA= "version10"

print ("Isalnum method:",nameA.isalnum())

#isnum and isdigit mehtod, islower, isupper, swap case
nameB= "version 10"
print ("Isnum method:",nameB.isnumeric())
print ("Isdigit method:",nameB.isdigit())
print ("Isdecimal method:",nameB.isdecimal())
print("IsLower:", name.islower())
print("IsUPPER:", name.isupper())

NameC= "my first code in python"
print("SwapCase:", NameC.swapcase())

#isspace - checks space
print("isspace:", NameC.isspace(), id(NameC))

#istitle - each starting letter word has title case, condition is true.
# if the starting is a number, then it ignores and checks the next character

print("IsTitle:", name.istitle())

#justify method (fill characters left or right side based on the length)
print(len(NameC))
print("justification :", NameC.rjust(25,'%'))
print("justification :", NameC.ljust(25,'@'))

#strip - if the first condition is false as per the fill, the strip is not executed
nameD="##$Text to type $$#"
print("strip :", nameD.strip())
print("strip :", nameD.lstrip('#$'))
print("strip :", nameD.rstrip('$#'))

#min max


#rfind

pyworld = "aws azure devops and python"

print("find",pyworld.find('azure')) # search substring from left to right
print("rfind",pyworld.rfind('azure')) # search substring from right to left

#rindex() method, index

print("index",pyworld.index('azure'))
print("rindex",pyworld.rindex('azure'))

print ("split", pyworld.split())
print ("split2elements", pyworld.split(' ', 2)) # splits as 0,1,2 elements
print ("split3elements", pyworld.split(' ', 3)) #splits as 0,1,2,3 elements

#splitlines method
print ("SplitLines: ", pyworld.splitlines()) # prints as list datatype


pyworld1 = "aws\nazure\ndevops\nand python"
print ("SplitLines() method: ", pyworld1.splitlines(2)) #








