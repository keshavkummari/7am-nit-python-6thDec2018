'''--------------------------------------------------------------'''
# 7. Identity Operators :
'''--------------------------------------------------------------'''

'''
is and is not are the identity operators in Python. 

They are used to check if two values (or variables) are located on the same part of the memory. 

Two variables that are equal does not imply that they are identical.

# Identity operators compare the memory locations of two objects.

1. is		= x is y, here is results in 1 if id(x) equals id(y).
2. is not	= x is not y, here is not results in 1 if id(x) is not equal to id(y).
'''
'''--------------------- Examples ----------------------------'''
# Example : Identity operators in Python

x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)
print(x1,y1,type(x1),type(y1),id(x1),id(y1))

# Output: True
print(x2 is y2)
print(x2,y2,type(x2),type(y2),id(x2),id(y2))

# Output: False
print(x3 is y3)
print(x3,y3,type(x3),type(y3),id(x3),id(y3))