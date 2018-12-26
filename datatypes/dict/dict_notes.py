Python Data Types - Dictionaries

#!/usr/bin/python

''' >>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
 '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy',
 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''

# ------------------------------------------------------- #
A dictionary is a mutable mapping from keys to values.

A dictionary with no keys is called an empty dictionary.

Dictionaries are also known in some programming languages as
associative memories,associative arrays, or hashmaps.

Unlike sequences, which are indexed by a range of integers,
dictionaries are indexed by keys, which can be of any immutable type.

Thus, dictionaries are also unordered.

When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.

# ------------------------------------------------------- #

# Operations:

1. a_dict.get               # Methods
2. []                       # Index
3. []=                      # Index
4. a_dict.has_key           # Methods
5. a_dict.pop               # Methods
6. a_dict.items             # Methods
7. a_dict.keys              # Methods
8. a_dict.values            # Methods
9. a_str.join               # Methods
10. dict        # Functions
11. len         # Functions
12. sum         # Functions
13. max         # Functions
14. min         # Functions
15. zip         # Functions
16. sorted      # Functions
17. map         # Functions
18. filter      # Functions
19. reduce      # Functions
20. any         # Functions
21. all         # Functions
22. enumerate   # Functions
23. type        # Functions
24. isinstance  # Functions
25. dir         # Functions
26. hasattr     # Functions
27. str         # Functions
28. repr        # Functions
29. ==      # Operator
30. !=      # Operator
31. is          # Identity Operator
32. is not      # Identity Operator
33. in      # Membership Operator
34. not in  # Membership Operator

# ------------------------------------------------------- #
1. Dictionary Constants                            =       {}
2. Convert Iterable of Pairs into Dictionary       =       dict()
3. Get Value in Dictionary by Key                  =       a_dict[], a_dict.get()
4. Set Value for Key in Dictionary                 =       a_dict[key] = value
5. Check if Key is in Dictionary                   =       a_dict.has_key()
6. Remove Key from Dictionary and Return its Value =       a_dict.pop()
7. Get List of all Key/Value Pairs in Dictionary   =       a_dict.items()
8. Get List of all Keys in Dictionary              =       a_dict.keys()
9. Get List of all Values in Dictionary            =       a_dict.values()

# ------------------------------------------------------- #
# Unsupported Dictionary Operations :
dict() with keyword arguments
a_dict.clear()
a_dict.copy()
a_dict.iteritems()
a_dict.iterkeys()
a_dict.itervalues()
a_dict.popitem()
a_dict.setdefault()
a_dict.update()
# ------------------------------------------------------- #
1. Dictionary Constants                            =       {}

Syntax:
{key<sub>0</sub>: value<sub>0</sub>, key<sub>1</sub>: value<sub>1</sub>, … }

# Examples:

print {}
Output : {}

print {1: 'a', 2: 'b', 9: 'c'}
Output : {1: 'a', 2: 'b', 9: 'c'}

print {1: 'a', (5, 'item'): [100], 'key': {True: 'hello', -9: 0}}
Output : {1: 'a', (5, 'item'): [100], 'key': {True: 'hello', -9: 0}}

'''Note : A dictionary is an unordered collection of key: value pairs,
with each key in a dictionary being distinct.'''
# ------------------------------------------------------- #
2. Convert Iterable of Pairs into Dictionary       =       dict()

# Syntax:
dict()
dict(an_iter)

# Examples:

print (dict())
Output : {}

print (dict([(1, 'a'), (2, 'b'), (3, 'c')]))
Output : {1: 'a', 2: 'b', 3: 'c'}

print (dict(((1, 'a'), (2, 'b'), (3, 'c'), (3, 'd'))))
Output : {1: 'a', 2: 'b', 3: 'd'}

print (dict(set([(1, 'a'), (2, 'b'), (3, 'c')])))
Output : {1: 'a', 2: 'b', 3: 'c'}

print (dict({1: 'a', 2: 'b', 3: 'c'}))
Output : {1: 'a', 2: 'b', 3: 'c'}

print (dict(enumerate(['a', 'b', 'c', 'd'])))
Output : {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

"""
Returns a new dictionary with the data from an_iter.

The iterable or iterator an_iter must consist of pairs of a valid key (i.e., of immutable type)
and value.

If any key occurs multiple times, then the last value encountered for that
key will be in the resulting dictionary.

If an_iter is already a dictionary, it returns a copy, i.e., a new
dictionary with the same elements.
"""
# ------------------------------------------------------- #
3. Get Value in Dictionary by Key    =       a_dict[], a_dict.get()

# Syntax:
a_dict[key]
a_dict.get(key)
a_dict.get(key, default)

# Examples:
print ({1: 'a', 2: 'b', 3: 'c'}[2])
Output: b

print ({1: 'a', 2: 'b', 3: 'c'}.get(2))
Output : b

print ({1: 'a', 2: 'b', 3: 'c'}.get(7))
Output : None

print ({1: 'a', 2: 'b', 3: 'c'}.get(7, 'not here'))
Output : not here

'''
Returns the value associated with the given key the dictionary a_dict.

If the key is not in the dictionary, a_dict[key] raises a KeyError error. However, a_dict.get(key) returns the default value default if provided, and None otherwise.
'''
# ------------------------------------------------------- #
4. Set Value for Key in Dictionary     =       a_dict[key] = value

# Syntax:
a_dict[key] = value

# Example:
d = {1: 'a', 2: 'b', 3: 'c'}
d[2] = 'd'

print (d)
d[5] = 'e'
print (d)
{1: 'a', 2: 'd', 3: 'c'}
{1: 'a', 2: 'd', 3: 'c', 5: 'e'}

'''
Note:
Mutates the dictionary a_dict so that the given key now maps to the given value.
'''

# ------------------------------------------------------- #
5. Check if Key is in Dictionary      =       a_dict.has_key()

# Syntax:
a_dict.has_key(key)

# Examples:
print ({1: 'a', 2: 'b', 3: 'c'}.has_key(2))
Output : True

print ({1: 'a', 2: 'b', 3: 'c'}.has_key(4))
Output: False

'''
Returns whether the given key is a key in the dictionary a_dict.
The equivalent key in a_dict is considered better style.
'''
# ------------------------------------------------------- #
6. Remove Key from Dictionary and Return its Value =       a_dict.pop()
# Syntax:
a_dict.pop(key)
a_dict.pop(key, default)

# Examples:

d = {1: 'a', 2: 'b', 3: 'c'}
print (d.pop(1))
Output : a

print (d)
Output : {2: 'b', 3: 'c'}

d = {1: 'a', 2: 'b', 3: 'c'}
print (d.pop(1, 'xyz'))
Output : a

print (d)
Output : {2: 'b', 3: 'c'}

d = {1: 'a', 2: 'b', 3: 'c'}

print (d.pop(4))
Output : Line 2: KeyError: 4

print (d)
Output : {1: 'a', 2: 'b', 3: 'c'}

d = {1: 'a', 2: 'b', 3: 'c'}

print (d.pop(4, 'xyz'))
Output : xyz

print (d)
Output : {1: 'a', 2: 'b', 3: 'c'}

'''
If key is a key in the dictionary, this removes it from the dictionary and
returns its value.

The value default is ignored in this case.

If key is not a key in the dictionary, this returns the value default.

If no default is provided, a KeyError is raised.
'''
# ------------------------------------------------------- #
7. Get List of all Key/Value Pairs in Dictionary   =       a_dict.items()

# Syntax:
a_dict.items()

# Examples:

print {1: 'a', 2: 'b', 3: 'c'}.items()
Output : [(1, 'a'), (2, 'b'), (3, 'c')]

sample_dict = {1: 'a', 2: 'b', 3: 'c'}
for key, value in sample_dict.items():
    print (key, 'maps to', value)

Output :
1 maps to a
2 maps to b
3 maps to c

'''
Returns a list of (key, value) pairs, for all the keys in dictionary a_dict.
'''

A common usage is to loop over all key/value pairs in a dictionary, as in the last example above.

# ------------------------------------------------------- #
8. Get List of all Keys in Dictionary   =       a_dict.keys()

# Syntax:
a_dict.keys()

# Example:

print ({1: 'a', 2: 'b', 3: 'c'}.keys())
Output : [1, 2, 3]

'''
Returns a list of the keys in dictionary a_dict.

While you can test if something is a dictionary key explicitly,
like key in a_dict.keys(), the simpler expression key in a_dict is equivalent.

The same applies to for-loops.
'''
# ------------------------------------------------------- #
9. Get List of all Values in Dictionary  =       a_dict.values()

# Syntax:
a_dict.values()

# Examples:

print ({1: 'a', 2: 'b', 3: 'c'}.values())
['a', 'b', 'c']

sample_dict = {1: 'a', 2: 'b', 3: 'c'}
for value in sample_dict.values():
    print (value, 'is a value in the dictionary')

Output:
a is a value in the dictionary
b is a value in the dictionary
c is a value in the dictionary

'''
Returns a list of the values in dictionary a_dict.

A common usage is to loop over all values in a dictionary, as in the last example above.
'''
# ------------------------------------------------------- #
