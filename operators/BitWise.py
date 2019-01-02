'''--------------------------------------------------------------'''
# 5. Bitwise Operators :
'''--------------------------------------------------------------'''
"""
Bitwise operator works on bits and performs bit-by-bit operation.

Assume if a = 60 and b = 13

Now in binary format they will be as follows :
bin(a)
bin(b)
a = 0011 1100
b = 0000 1101

# Note: Python's built-in function bin() can be used to obtain binary
representation of an integer number.

For example, 2 is 10 in binary and 7 is 111.

In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

# Bitwise operators in Python :

Operator	Meaning	Example
1. &			Bitwise AND	x & y = 0 (0000 0000)
2. |			Bitwise OR	x | y = 14 (0000 1110)
3. ~			Bitwise NOT	~x = -11 (1111 0101)
4. ^			Bitwise XOR	x ^ y = 14 (0000 1110)
5. >>			Bitwise right shift	x>> 2 = 2 (0000 0010)
6. <<			Bitwise left shift	x<< 2 = 40 (0010 1000)
"""
# Bitwise AND OPERATION:
True  = 1
False = 0

a=15
b=10

print(bin(a))
'0b1111'

print(bin(b))
'0b1010'

print("Results of" ,bin(a), "AND" ,bin(b),bin(a&b))
'0b1010'

0b1111
0b1010
-------
  1010  # Output (Results will be true when both bits are true)
-------
# Bitwise OR OPERATION:
print(bin(a))
'0b1111'

print(bin(b))
'0b1010'

print(bin(a|b))
'0b1111'

0b1111
0b1010
-------
  1111
-------

# Output (Results will be true even if any one of the two
bits it's true)

# Bitwise XOR OPERATION:
print(bin(a))
'0b1111'

print(bin(b))
'0b1010'


print(bin(a^b))
'0b101'

0b1111
0b1010
-------
  0101  # Output 1+1=0 1+0=1 1+1=0 1+0=1
  (Bits has to be differenet then its true condition)
-------





