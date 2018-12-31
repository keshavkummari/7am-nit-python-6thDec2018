Number data types store numeric values.

They are immutable data types, means that changing the value of a number
data type results in a newly allocated object.

Number objects are created when you assign a value to them.

For example :
var1 = 1
var2 = 10

You can also delete the reference to a number object by using the del statement.

The syntax of the del statement is:

Syntax: del var1[,var2[,var3[....,varN]]]]

You can delete a single object or multiple objects by using the del statement.

For example:

del var
del var_a, var_b

******************************************************
Python supports four different numerical types -

1. int (signed integers): They are often called just integers or ints,
are positive or negative whole numbers with no decimal point.

Example : 0-9 ; price = 10

2. long (long integers ):
Also called longs, they are integers of unlimited size,
written like integers and followed by an uppercase or lowercase L.

Example : 0-9 ; price = 10903938l


3. float (floating point real values) :
Also called floats, they represent real numbers and are written with
a decimal point dividing the integer and fractional parts.

Floats may also be in scientific notation,
with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).

Example : 0-9 ; price = 10.75


4. complex (complex numbers) : are of the form a + bJ,
where a and b are floats and J (or j) represents the square root of -1
(which is an imaginary number). The real part of the number is a,
and the imaginary part is b. Complex numbers are not used much in Python programming.


******************************************************
Here are some examples of numbers:

int	    long				float		complex
10	    51924361L		 	0.0		     3.14j
-100	-0x19323L		 	15.20		 45.j
-786	0122L				-21.9		  9.322e-36j
080	    0xDEFABCECBDAECBFBAEL	32.3+e18      .876j
-0490	535633629843L		-90.           -.654 5+0J
-0x260	-052318172735L		-32.54e100	3e+26J
0x69	-4721885298529L		70.2-E12	4.53e-7j
******************************************************
Note:
Python allows you to use a lowercase L with long,
but it is recommended that you use only an uppercase L to avoid confusion with the number 1.

Python displays long integers with an uppercase L.

A complex number consists of an ordered pair of real floating point numbers denoted by a + bj,
where a is the real part and b is the imaginary part of the complex number.
******************************************************

Number Type Conversion:
***********************
Python converts numbers internally in an expression containing mixed types to a common type for evaluation.

But sometimes, you need to coerce a number explicitly from one type to another to satisfy the requirements of an operator or function parameter.

Type int(x) to convert x to a plain integer.

Type long(x) to convert x to a long integer.

Type float(x) to convert x to a floating-point number.

Type complex(x) to convert x to a complex number
with real part x and imaginary part zero.

Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions
******************************************************
LIST OF NUMBER FUNCTIONS:

1. Mathematical Functions:
2. Random Number Functions:
3. Trigonometric Functions:
4. Mathematical Constants:
******************************************************

Mathematical Functions:
*****************************************************
+ plus
- minus
/ slash
* asterisk
% percent
< less-than
> greater-than
<= less-than-equal
>= greater-than-equal

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
*****************************************************

SNO		Function		Returns ( description )
1	.	abs(x)			:	The absolute value of x: the (positive) distance between x and zero.
2	.	ceil(x)			:	The ceiling of x: the smallest integer not less than x
#3	.	cmp(x, y)		:	-1 if x < y, 0 if x == y, or 1 if x > y
4	.	exp(x)			:	The exponential of x: ex
5	.	fabs(x)			:	The absolute value of x.
6	.	floor(x)		:	The floor of x: the largest integer not greater than x
7	.	log(x)			:	The natural logarithm of x, for x> 0
8	.	log10(x)		:	The base-10 logarithm of x for x> 0 .
9	.	max(x1, x2,...)	:	The largest of its arguments: the value closest to positive infinity
10	.	min(x1, x2,...)	:	The smallest of its arguments: the value closest to negative infinity
11	.	modf(x)			:	The fractional and integer parts of x in a two-item tuple.
							Both parts have the same sign as x.
							The integer part is returned as a float.
12	.	pow(x, y)		:	The value of x**y.
13	.	round(x [,n])	:	x rounded to n digits from the decimal point. Python rounds away 						from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
14	.	sqrt(x)			:	The square root of x for x > 0

********** Mathematical Functions Examples :**********

Python includes following functions that perform mathematical calculations.

1. abs(x)  : The absolute value of x: the (positive) distance between x and zero.

Python Number abs() Method:
#!/usr/bin/python
print "abs(-45) : ", abs(-45)  # 0 -45  45
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)

output:
abs(-45) :  45
abs(100.12) :  100.12
abs(119L) :  119

----------------------------------------------------------------
2. ceil(x) : The ceiling of x: the smallest integer not less than x

Python Number ceil() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(119L) : ", math.ceil(119L)
print "math.ceil(math.pi) : ", math.ceil(math.pi)

#ceil() Method round off to the nearest integer (not less)

print "ceil method", math.ceil(66.1)
print "ceil method", math.ceil(-45.4)

Output:
math.ceil(-45.17) :  -45.0
math.ceil(100.12) :  101.0
math.ceil(100.72) :  101.0
math.ceil(119L)   :  119.0
math.ceil(math.pi) : 4.0
----------------------------------------------------------------
3. cmp(x, y) : -1 if x < y, 0 if x == y, or 1 if x > y
Python Number cmp() Method:
#!/usr/bin/python
print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)

#cmp() Method -1 for x<y, 0 for x==y and 1 for x>y

print "cmp method", cmp(20, 30)
print "cmp method", cmp(20, 20)
print "cmp method", cmp(30, 20)


Output:
cmp(80, 100) :  -1
cmp(180, 100) :  1
cmp(-80, 100) :  -1
cmp(80, -100) :  1
----------------------------------------------------------------
4. exp(x) : The exponential of x: ex

Python Number exp() Method:

#!/usr/bin/python
import math   # This will import math module

print "math.exp(-45.17) : ", math.exp(-45.17)
print "math.exp(100.12) : ", math.exp(100.12)
print "math.exp(100.72) : ", math.exp(100.72)
print "math.exp(119L) : ", math.exp(119L)
print "math.exp(math.pi) : ", math.exp(math.pi)

#exp() Method; gives exponential value in for of e

print "exp method", math.exp(66.1)
print "exp method", math.exp(-45.4)

Output:
math.exp(-45.17) :  2.41500621326e-20
math.exp(100.12) :  3.03084361407e+43
math.exp(100.72) :  5.52255713025e+43
math.exp(119L) :  4.7978133273e+51
math.exp(math.pi) :  23.1406926328
----------------------------------------------------------------
5. fabs(x) : The absolute value of x.
Python Number fabs() Method:

#!/usr/bin/python
import math   # This will import math module

print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)

#fabs() Method; Absolute distance value

print "fabs method", math.fabs(-11.1)
print "fabs method", math.fabs(31.6)

Output:
math.fabs(-45.17) :  45.17
math.fabs(100.12) :  100.12
math.fabs(100.72) :  100.72
math.fabs(119L) :  119.0
math.fabs(math.pi) :  3.14159265359

----------------------------------------------------------------
6. floor(x) : The floor of x: the largest integer not greater than x

Python Number floor() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.floor(-45.17) : ", math.floor(-45.17)
print "math.floor(100.12) : ", math.floor(100.12)
print "math.floor(100.72) : ", math.floor(100.72)
print "math.floor(119L) : ", math.floor(119L)
print "math.floor(math.pi) : ", math.floor(math.pi)

#floor() Method round off to the nearest integer (not greater)

print "floor method", math.floor(66.1)
print "floor method", math.floor(-45.4)


Output:
math.floor(-45.17) :  -46.0
math.floor(100.12) :  100.0
math.floor(100.72) :  100.0
math.floor(119L) :  119.0
math.floor(math.pi) :  3.0
----------------------------------------------------------------
7. log(x) : The natural logarithm of x, for x> 0
Python Number log() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.log(100.12) : ", math.log(100.12)
print "math.log(100.72) : ", math.log(100.72)
print "math.log(119L) : ", math.log(119L)
print "math.log(math.pi) : ", math.log(math.pi)

#log() Method;

print "log method", math.log(math.pi)
print "log10 method", math.log10(math.pi)
print "log1p method", math.log1p(math.pi)


Output:
math.log(100.12) :  4.60636946656
math.log(100.72) :  4.61234438974
math.log(119L) :  4.77912349311
math.log(math.pi) :  1.14472988585

----------------------------------------------------------------
8. log10(x) : The base-10 logarithm of x for x> 0 .
Python Number log10() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.log10(100.12) : ", math.log10(100.12)
print "math.log10(100.72) : ", math.log10(100.72)
print "math.log10(119L) : ", math.log10(119L)
print "math.log10(math.pi) : ", math.log10(math.pi)

Output:
math.log10(100.12) :  2.00052084094
math.log10(100.72) :  2.0031157171
math.log10(119L) :  2.07554696139
math.log10(math.pi) :  0.497149872694

----------------------------------------------------------------
9. max(x1, x2,...) : The largest of its arguments: the value closest to positive infinity

Python Number max() Method:
#!/usr/bin/python
print "max(80, 100, 1000) : ", max(80, 100, 1000)
print "max(-20, 100, 400) : ", max(-20, 100, 400)
print "max(-80, -20, -10) : ", max(-80, -20, -10)
print "max(0, 100, -400) : ", max(0, 100, -400)

#max() Method; min() Method

print "max method", max(30, -30, 40, 50)
print "min method", min(30, -30, 40, 50)


Output:
max(80, 100, 1000) :  1000
max(-20, 100, 400) :  400
max(-80, -20, -10) :  -10
max(0, 100, -400) :  100
----------------------------------------------------------------
10. min(x1, x2,...): The smallest of its arguments: the value closest to negative infinity
Python Number min() Method:
#!/usr/bin/python
print "min(80, 100, 1000) : ", min(80, 100, 1000)
print "min(-20, 100, 400) : ", min(-20, 100, 400)
print "min(-80, -20, -10) : ", min(-80, -20, -10)
print "min(0, 100, -400) : ", min(0, 100, -400)

Output:

min(80, 100, 1000) :  80
min(-20, 100, 400) :  -20
min(-80, -20, -10) :  -80
min(0, 100, -400) :  -400
----------------------------------------------------------------
11. modf(x) : The fractional and integer parts of x in a two-item 
tuple.
Both parts have the same sign as x.
The integer part is returned as a float.

Python modf() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

#modf()
print "modf method", math.modf(22.67)

Output:
math.modf(100.12) :  (0.12000000000000455, 100.0)
math.modf(100.72) :  (0.71999999999999886, 100.0)
math.modf(119L) :    (0.0, 119.0)
math.modf(math.pi) :  (0.14159265358979312, 3.0)
----------------------------------------------------------------
12. pow(x, y) : The value of x**y.
Python Number pow() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.pow(100, 2) : ", math.pow(100, 2)
print "math.pow(100, -2) : ", math.pow(100, -2)
print "math.pow(2, 4) : ", math.pow(2, 4)
print "math.pow(3, 0) : ", math.pow(3, 0)

#pow()
print "pow method", math.pow(10, 3)


Output:
math.pow(100, 2) :  10000.0
math.pow(100, -2) :  0.0001
math.pow(2, 4) :  16.0
math.pow(3, 0) :  1.0
----------------------------------------------------------------
13. round(x [,n]) : x rounded to n digits from the decimal point.
Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

Python Number round() Method:

#!/usr/bin/python

print "round(80.23456, 2) : ", round(80.23456, 2)
print "round(100.000056, 3) : ", round(100.000056, 3)
print "round(-100.000056, 3) : ", round(-100.000056, 3)

#round()
print "round method", round(22.67453424, 3)


Output:
round(80.23456, 2) :  80.23
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
----------------------------------------------------------------
14. sqrt(x) : The square root of x for x > 0

Python Number sqrt() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.sqrt(100) : ", math.sqrt(100)
print "math.sqrt(7) : ", math.sqrt(7)
print "math.sqrt(math.pi) : ", math.sqrt(math.pi)

#sqrt()
print "sqrt method", math.sqrt(49)


Output:
math.sqrt(100) :  10.0
math.sqrt(7) :  2.64575131106
math.sqrt(math.pi) :  1.77245385091
----------------------------------------------------------------

