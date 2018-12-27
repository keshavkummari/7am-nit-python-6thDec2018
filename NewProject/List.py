'''
List is Mutable sequence of values of any types. A list with zero element is called an empty list.
List elements are indexed by seq integers.
'''

#creating and accessing List datatype

list1=['python', 'linux', 1997, 20.00, 34, 34]
print (list1,type(list1),id(list1),list(enumerate(list1)))

#LisT Methods
#Append can add a number, string, list of variable, tuple. Item assignment is allowed.

list1.append("newvalue")
print(list1,type(list1),id(list1),list(enumerate(list1)))

#Delete - builtin fucntion - we can delete only slice of the varaible.

del list1[2]

print(list1,type(list1),id(list1),list(enumerate(list1)))

# count - to check count of specific element

print("Printing the count of variable value for the substring:",list1.count(34))

#Extend method - is similar to concatination

Beforeextend =['a','b','c']
Afterextend=['1','2']
Beforeextend.extend(Afterextend)

print("print the output after extend command:", Beforeextend)