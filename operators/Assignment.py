# Assignment Operators
"""
LeftOperand = RightOperand 
x           = 5

-------------------------------------------
Operator |	    Example	 |	Equivatent to
-------------------------------------------
1.   =			x = 5		x = 5
2.  +=			x += 5		x = x + 5	[+= Add AND]
3.  -=			x -= 5		x = x - 5	[-= Subtract AND]
4.  *=			x *= 5		x = x * 5	[*= Multiply AND]
5.  /=			x /= 5		x = x / 5	[/= Divide AND]
6.  %=			x %= 5		x = x % 5	[%= Modulus AND]
7.  //=			x //= 5		x = x // 5	[//= Floor Division]
8.  **=			x **= 5		x = x ** 5	[**= Exponent AND]
"""

a = 21
b = 10
c = 0

c = a + b # 21 + 10 = 31
print ("Line 1 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c += a   # 31 + 21 = 52
print ("Line 2 - Value of c is ", id(a),id(b),id(c),type(c),"c + a", c , sep=':')


print(c) # 52 * 21 = 1113
c *= a
print ("Line 3 - Value of c is ", id(a),id(b),id(c),type(c),c )

print(c) #1113
c /= a
print ("Line 4 - Value of c is ", id(a),id(b),id(c),type(c),c )

c = 2
print(c) # 2
c %= a
print ("Line 5 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c **= a
print ("Line 6 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c //= a
print ("Line 7 - Value of c is ", id(a),id(b),id(c),type(c),c)
