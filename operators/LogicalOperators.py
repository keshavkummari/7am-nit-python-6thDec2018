"""
''--------------------------------------------------------------'''
# 4. Logical Operators :
'''--------------------------------------------------------------'''
# Example:  variable a holds True and variable b holds False

1. and Logical AND		= (a and b) is False.
2. or Logical OR		= (a or b) is True.
3. not Logical NOT		= Not(a and b) is True.

"""

# Example : Logical Operators in Python

x = True
y = False

# Output: x and y is False
print('x and y is',id(x),id(y),type(x),type(y),x and y)

# Output: x or y is True
print('x or y is',id(x),id(y),type(x),type(y),x or y)

# Output: not x is False
print('not x is',id(x),id(y),type(x),type(y),not x)