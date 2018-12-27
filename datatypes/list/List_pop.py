#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

print(aCoolList,list(enumerate(aCoolList)))
# deleting values
aCoolList.pop(2)

print("")
print(aCoolList,list(enumerate(aCoolList)))

# Without index using pop method:
aCoolList.pop()

print("")
print(aCoolList,list(enumerate(aCoolList)))
'''
5. list.pop([i]) : list.pop()
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list. 
(The square brackets around the i in the method signature denote that the
parameter is optional, 
not that you should type square brackets at that position. 
You will see this notation frequently in the Python Library Reference.)
'''
