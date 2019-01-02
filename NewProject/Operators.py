#Arithmetic, relational, assignmenr, logic, bitwise, membership and Identity operators


x = 15
y = 4

print("Printing the arithmetic operators")
# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)


#comparison operators
print("Printing the Comparison operators")
x = 10
y = 12

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

print("Comparison operators for Strings:","Hello" == "World")
print("Python" != "R")


#Logical operators
'''
For AND operator – It returns TRUE if both the operands (right side and left side) are true
For OR operator- It returns TRUE if either of the operand (right side or left side) is true
For NOT operator- returns TRUE if operand is false (it complements the operand)
'''

print("Printing the Logical operators")
x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)
print('not y is',not y)

print(True and True)
print(True and False)
print(False and False)

print("Logical operators with more than two operands")
print(True and True and True and True)
print(True and True and True and False)
print(False or False or False or False)
print(False or False or False or True)


#Bitwise operators - act on operands as if they were string of binary digits
'''  
Operator	Meaning	Example
&	Bitwise AND	x& y
|	Bitwise OR	x | y
~	Bitwise NOT	~x 
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<
'''
print("Printing the Bitwise operators")
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)


# Assignment operators

'''

Operator	Example	Equivatent to
=	            x = 5	x = 5
+=	            x += 5	x = x + 5
-=	            x -= 5	x = x - 5
*=	            x *= 5	x = x * 5
/=	            x /= 5	x = x / 5
%=	            x %= 5	x = x % 5
//=	            x //= 5	x = x // 5
**=	            x **= 5	x = x ** 5
&=	            x &= 5	x = x & 5
|=	            x |= 5	x = x | 5
^=	            x ^= 5	x = x ^ 5
>>=	            x >>= 5	x = x >> 5
<<=	            x <<= 5	x = x << 5
'''


#Identity operators - compare the memory locations of two objects


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print("Printing the Identity operators")
# Output: False

print("Value for x1 and y1", type(x1),id(x1), type(x2), id(x2))
print("Value for x2 and y2", type(x2),id(x2), type(y2), id(y2))
print("Value for x3 and y3", type(x3),id(x3), type(y3), id(y3))

print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

'Membership Operators'

print("Printing the membership operators")

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
'''
Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive). 
Similary, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.
'''