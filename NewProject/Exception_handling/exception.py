'''
Exception Handling
1. Standard Exceptions.
2. Assertions sanity check of a program - raise-if statement and raise-if-not statement

Syntax:
assert Expression[, Arguments]


'''
# EXAMPLE

def K(Temp):
   assert (Temp >= 0),"Colder than absolute zero!"
   return ((Temp-273)*1.8)+32

print ('line1',K(273))
print ('line2',int(K(505.78)))
print (K(-5)) # this will provide an assertion output

