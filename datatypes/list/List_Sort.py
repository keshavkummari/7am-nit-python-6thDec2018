#!/usr/bin/python

#aCoolList = ["superman", "spiderman", '1947','1987',"Spiderman"]
"""
aCoolList = ["c","5","A","!","k"]

oneMoreList = [98, 34, 56,10, 34, 78, 2]
"""
aCoolList = ("c","5","A","!","k")

oneMoreList = (98, 34, 56,10, 34, 78, 2)

a = list(aCoolList)

print(a)

print("")

a.sort()

print(a)

#!/usr/bin/python

#aCoolList = ["superman", "spiderman", '1947','1987',"Spiderman"]

aCoolList = ["c","5","A","!","k"]

oneMoreList = [98, 34, 56,10, 34, 78, 2]

print(aCoolList)
aCoolList.sort()
print(aCoolList)

print (oneMoreList)
oneMoreList.sort()
print (oneMoreList)


'''
8. list.sort(cmp=None, key=None, reverse=False):
Sort the items of the list in place
(the arguments can be used for sort customization, 
see sorted() for their explanation).
'''
