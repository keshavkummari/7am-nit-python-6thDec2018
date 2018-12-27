"""
#!/usr/bin/python

a_list = [1, 2, 3]

print(a_list,type(a_list),id(a_list),len(a_list))

a_list.append(4)

a_list.append("Welcome to PyWorld")

print(a_list,type(a_list),id(a_list),len(a_list))

a_list.append([5, 6, 7])

a_list.append(('Py','dev','prd'))

print(a_list,type(a_list),id(a_list),len(a_list))

a_list.append("Guido")

print(a_list,type(a_list),id(a_list),len(a_list))


#!/usr/bin/python

list1 = ['python', 'linux', 1997, 2000]

print (list1)

del list1[2]

print ("After deleting value at index 2 : ")

print (list1)

del list1

print(list1)

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56, 34, 34, 78, 98]

# Trying to find the no.of occurenecs in a variable:

# Method : count(x)
print(aCoolList.count(22))

print(aCoolList.count('spiderman'))

print(oneMoreList.count(34))

# Return the number of times x appears in the list.

"""


#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

# extending the list

# Before:
print (aCoolList)
#print(type(aCoolList),len(aCoolList),id(aCoolList))

print (oneMoreList)
#print(type(oneMoreList),len(oneMoreList),id(oneMoreList))

aCoolList.extend(oneMoreList)
# After:

print (aCoolList)
#print(type(aCoolList),len(aCoolList),id(aCoolList))

"""
Extend the list by appending all the items in the given list;
equivalent to a[len(a):] = L.
"""

