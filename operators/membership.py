'''--------------------------------------------------------------'''
# 6. Membership Operators :
'''--------------------------------------------------------------'''

'''
in and not in are the membership operators in Python. 

They are used to test whether a value or variable is found in a sequence
(string, list, tuple, set and dictionary).

# Membership operators test for membership in a sequence, such as
# strings, lists, or tuples.

1. in	    = x in y, here in results in a 1 if x is a member of sequence y.
2. not in   = x not in y, here not in results in a 1 if x is not a member of sequence y.
'''
'''--------------------- Examples ----------------------------'''
#Example #5: Membership operators in Python

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
