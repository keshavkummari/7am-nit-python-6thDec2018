Python Data Types - List
#!/usr/bin/python

'''
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
'pop', 'remove', 'reverse', 'sort']
'''
# ------------------------------------------------------- #

# ------------------------------------------------------- #

# Operations:
1 + # Concatenation Operators
2 * # Repetition Operator
3 [] # Slice Operator
4 [:] # Range Slice Operator
5 [::] # 0-Based Indexing
6 []=
7 in  # Membership Operators
8 not in  # Membership Operators
9 is   # Identity Operators
10 is not   # Identity Operators
11 < # Comparison Operators
12 > # Comparison Operators
13 <= # Comparison Operators
14 >= # Comparison Operators
15 == # Comparison Operators
16 != # Comparison Operators
17 a_list.append  # Methods
18 a_list.extend  # Methods
19 a_list.insert  # Methods
20 a_list.remove  # Methods
21 a_list.pop  # Methods
22 a_list.reverse  # Methods
23 a_list.sort  # Methods
24 a_seq.index  # Methods
25 a_seq.count  # Methods
26 a_str.join  # Methods
27 random.shuffle   # Module & Method
28 len # Function
29 sum # Function
30 max # Function
31 min # Function
32 zip # Function
33 sorted # Function
34 map # Function
35 filter # Function
36 reduce # Function
37 any # Function
38 all # Function
39 list # Function
40 range # Function
41 enumerate # Function
42 type # Function
43 isinstance # Function
44 dir # Function
45 hasattr # Function
46 str # Function
47 repr # Function

# ------------------------------------------------------- #
'''
A list is a mutable sequence of values of any type.

A list with zero elements is called an empty list.

List elements are indexed by sequential integers, starting with zero.
'''
# ------------------------------------------------------- #
List Constants                                  =       […]
Convert Iterable or Iterator into List          =       list()
Set Value at Specific Position in List          =       a_list[]=
Arithmetic Progressions List                    =       range()
Add Item to End of List                         =       a_list.append()
Add Multiple Items to End of List               =       a_list.extend()
Insert Item into List                           =       a_list.insert()
Remove Item from List by Value                  =       a_list.remove()
Remove Item from List by Position               =       a_list.pop()
Reverse Items in List                           =       a_list.reverse()
Sort Items in List in Place                     =       a_list.sort()
# ------------------------------------------------------- #
List Constants                                  =       […]

# Syntax:
[val<sub>0</sub>, val<sub>1</sub>, …]

# Examples:

print []
Output : []

print [1, 2, 3, 8, 9]
Output : [1, 2, 3, 8, 9]

print [(1, 2), 'hello', 3, ['a', 'b', 'c']]
Output : [(1, 2), 'hello', 3, ['a', 'b', 'c']]

'''
Lists are constructed with square brackets, separating items with commas.
'''
# ------------------------------------------------------- #
# Syntax:
list()
list(an_iter)

# Examples:

print list()
[]
print list('abc')
['a' ,'b', 'c']

print list([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]

print list((1, 2, 3, 4, 5))
[1, 2, 3, 4, 5]

print list(set([1, 2, 3, 4]))
[1, 2, 3, 4]

print list({1: 2, 3: 4})
[1, 3]

print list(enumerate(['a', 'b', 'c', 'd']))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

'''
Converts any iterable or iterator into a list. If the argument is already a list, it returns a copy, i.e., a new list with the same elements.
'''

# ------------------------------------------------------- #
# Syntax:
a_list[index] = value

# Example:

numbers = [4, 8, 19, 0]
numbers[1] = 27

print numbers
[4, 27, 19, 0]

'''
Mutates the list to now contain the given value at the given index.
The index must be within the current range of indices of the list.
'''

# Syntax:
#a_list[index] = value

# Example:

numbers = [4, 8, 19, 0]

print('To Check Index value of each element in a Variable: ',list(enumerate(numbers)))

print("")

print("Accessing a List Variable: ",numbers)

print("")

numbers[1] = 27

print("Append or Modify a exising element value: ",numbers)

print('To Check Index value of each element in a Variable: ',list(enumerate(numbers)))


# ------------------------------------------------------- #

Syntax:
range(stop)
range(start, stop)
range(start, stop, step)
Examples:
Code Output
print range(5)
[0, 1, 2, 3, 4]
print range(1, 10)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(-10, 100, 20)
[-10, 10, 30, 50, 70, 90]
print range(100, -10, -20)
[100, 80, 60, 40, 20, 0]
for i in range(5):
    print i
0
1
2
3
4
This is a versatile function to create lists containing arithmetic progressions. The step cannot be zero, and it defaults to 1. The start defaults to 0. The full form returns a list of integers [start, start + step, start + 2 * step, …]. If step is positive, the last element is the largest start + i * step less than stop; if step is negative, the last element is the smallest start + i * step greater than stop.

It is often used in for loops, as illustrated in the last example above. It provides a mechanism for looping a specific number of iterations.
# ------------------------------------------------------- #
Syntax:
a_list.append(x)
Examples:
Code Output
a_list = [1, 2, 3]
a_list.append(4)
a_list.append([5, 6, 7])
print a_list
[1, 2, 3, 4, [5, 6, 7]]
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1.append([4, 5, 6])
list2.extend([4, 5, 6])
print list1
print list2
[1, 2, 3, [4, 5, 6]]
[1, 2, 3, 4, 5, 6]
Add item x to the end of the list a_list.

A common mistake is to confuse a_list.append(x) and a_list.extend(x). As shown in the last example above, the former adds one element to the list, while the latter adds a group of elements.
# ------------------------------------------------------- #
Syntax:
a_list.extend(an_iter)
Examples:
Code Output
a_list = [1, 2, 3]
a_list.extend([])
print a_list
[1, 2, 3]
a_list = [1, 2, 3]
a_list.extend([4, 5, 6])
a_list.extend((7, 8))
a_list.extend('abc')
a_list.extend({'d': 'e', 'f': 'g'})
[1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'f']
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1.append([4, 5, 6])
list2.extend([4, 5, 6])
print list1
print list2
[1, 2, 3, [4, 5, 6]]
[1, 2, 3, 4, 5, 6]
Add each item from the iterable an_iter onto the end of the list a_list. When the iterable is a list, this is also called concatenation.

A common mistake is to confuse a_list.append(x) and a_list.extend(x). As shown in the last example above, the former adds one element to the list, while the latter adds a group of elements.
# ------------------------------------------------------- #
Syntax:
a_list.insert(i, x)
Example:
Code Output
a_list = ['a', 'b', 'c']
a_list.insert(1, 'x')
print a_list
a_list.insert(0, 'y')
print a_list
a_list.insert(5, 'z')
print a_list
['a', 'x', 'b', 'c']
['y', 'a', 'x', 'b', 'c']
['y', 'a', 'x', 'b', 'c', 'z']
Inserts an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# ------------------------------------------------------- #
Syntax:
a_list.remove(x)
Example:
Code Output
a_list = ['a', 'b', 'c', 'b']
a_list.remove('b')
print a_list
['a', 'c', 'b']
Removes the first item from the list whose value is x. It is an error if there is no such item.
# ------------------------------------------------------- #
Syntax:
a_list.pop([index])
Example:
Code Output
a_list = ['a', 'b', 'c']
print a_list.pop(1)
print a_list
b
['a', 'c']
Removes the item at the given index in the list a_list, and returns it. If no index is specified, it defaults to the last item.
# ------------------------------------------------------- #
Syntax:
a_list.reverse()
Example:
Code Output
a_list = [1, 2, 3]
a_list.reverse()
print a_list
[3, 2, 1]
Reverses the elements of the list a_list in place.
# ------------------------------------------------------- #

Syntax:
a_list.sort()
a_list.sort(reverse=rev_bool, key=key_fn)
Examples:
Code Output
a_list = [2, 1, 3, 2]
a_list.sort()
print a_list
[1, 2, 2, 3]
a_list = [2, 1, 3, 2]
a_list.sort(reverse=True)
print a_list
[3, 2, 2, 1]
See also:
sorted() — Sort an iterable
Sorts the items of the list a_list in ascending order in place.
I.e., it mutates a_list. It returns None.

By default or when rev_bool is False, the elements are in ascending order.
When rev_bool is True, the elements are in descending order. (Bug: It reverses when rev_bool is False, too.) If the elements are of different types, then the ascending or descending ordering is based upon their hash values.

Need to explain and provide examples for key argument.

The sort is guaranteed to be stable. Thus, when multiple elements have the same key, their original order is preserved.
# ------------------------------------------------------- #
