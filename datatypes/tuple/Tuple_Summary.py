        #  0      1        2          3
atuple = 'dev', "tst", '''acc''', """prd"""

atuple = 'dev', 'tst', 'acc', 'prd'

atuple1 = ('dev',1.0,'tst',2.0,'acc',3.0,'prd',4.0)


print(atuple,type(atuple),id(atuple),len(atuple))


print(atuple1,type(atuple1),id(atuple1),len(atuple1))

print(tuple(enumerate(atuple1)))

#Python Data Types - Tuple
#!/usr/bin/python

'''
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', 'count', 'index']

'''
# ------------------------------------------------------- #
'''
A tuple is an immutable sequence of values of any type.
Tuple elements are indexed by sequential integers, starting with zero.

Tuples are constructed by the comma operator,
with or without enclosing parentheses.

An empty tuple must have the enclosing parentheses.

A single item tuple must have a trailing comma.
'''
# ------------------------------------------------------- #

# Operations:
1 + # Concatenation Operators
2 * # Repetition Operator
3 [] # Slice Operator
4 [:] # Range Slice Operator
5 [::] # 0-Based Indexing
6 in  # Membership Operators
7 not in  # Membership Operators
8 is   # Identity Operators
9 is not   # Identity Operators
10 < # Comparison Operators
11 <= # Comparison Operators
12 > # Comparison Operators
13 >= # Comparison Operators
14 == # Comparison Operators
15 != # Comparison Operators
16 a_seq.index   # Methods
17 a_seq.count   # Methods
18 a_matrix.shape   # Methods
19 a_str.join   # Methods
20 random.shuffle  # Module & Method
21 tuple # Function
22 len # Function
23 sum # Function
24 max # Function
25 min # Function
26 zip # Function
27 sorted # Function
28 map # Function
29 filter # Function
30 reduce # Function
31 any # Function
32 all # Function
33 enumerate # Function
34 type         # Function
35 isinstance # Function
36 dir         # Function
37 hasattr         # Function
38 str         # Function
39 repr         # Function

# ------------------------------------------------------- #

# Syntax:
(val<sub>0</sub>, val<sub>1</sub>, …)

# Examples:

print ()
Output :()

print (1,)
Output : (1,)

t = 1,
print(t)
Output : (1,)

print (1, 2, 3, 8, 9)
Output : (1, 2, 3, 8, 9)

t = 1, 2, 3, 8, 9
print (t)
Output : (1, 2, 3, 8, 9)

print ((1, 2), 'hello', 3, ['a', 'b', 'c'])
Output : ((1, 2), 'hello', 3, ['a', 'b', 'c'])

t = 1, 2, 3
print(t)
Output : (1, 2, 3)

'''
Tuples are constructed by the comma operator,
with or without enclosing parentheses.

An empty tuple must have the enclosing parentheses.

A single item tuple must have a trailing comma.
'''
# ------------------------------------------------------- #
# Syntax:
tuple()
tuple(an_iter)

# Examples:

print tuple()
Output : ()

print tuple('abc')
Output :  ('a' ,'b', 'c')

print tuple([1, 2, 3, 4, 5])
Output : (1, 2, 3, 4, 5)

print tuple((1, 2, 3, 4, 5))
Output : (1, 2, 3, 4, 5)

print tuple(set([1, 2, 3, 4]))
Output : (1, 2, 3, 4)

print tuple({1: 2, 3: 4})
Output : (1, 3)

print tuple(enumerate(['a', 'b', 'c', 'd']))
Output : ((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'))

'''
Converts any iterable into a tuple.

If the argument is already a tuple, it returns a copy, i.e., 
a new tuple with the same elements.
'''
# ------------------------------------------------------- #
