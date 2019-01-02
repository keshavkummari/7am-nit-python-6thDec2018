#!/usr/bin/python

# Importing additional functionality

import math

#Various examples discussing the in built math functions

#abs() Method; Absolute distance value

print ("abs method", abs(-11.1))
print ("abs method", abs(31))

#fabs() Method; Absolute distance value

print ("fabs method", math.fabs(-11.1))
print ("fabs method", math.fabs(31))

#ceil() Method round off to the nearest integer (not less)

print ("ceil method", math.ceil(66.1))
print ("ceil method", math.ceil(-45.4))

#floor() Method round off to the nearest integer (not greater)

print ("floor method", math.floor(66.1))
print ("floor method", math.floor(-45.4))

"""
#cmp() Method -1 for x<y, 0 for x==y and 1 for x>y

print ("cmp method", cmp(20, 30))
print ("cmp method", cmp(20, 20))
print ("cmp method", cmp(30, 20))
"""
#exp() Method; gives exponential value in for of e

print ("exp method", math.exp(66.1))
print ("exp method", math.exp(-45.4))

#log() Method; 

print ("log method", math.log(math.pi))
print ("log10 method", math.log10(math.pi))
print ("log1p method", math.log1p(math.pi))

#max() &  min() Functions

print ("min method", min(30, -30, 40, 50))
print ("max method", max(30, -30, 40, 50))

#modf() 

print ("modf method", math.modf(22.67))

#pow() 

print ("pow method", math.pow(10, 3))

#round() 

print ("round method", round(22.67453424, 2))

#sqrt() 

print ("sqrt method", math.sqrt(69))



