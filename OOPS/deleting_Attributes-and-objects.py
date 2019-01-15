# Deleting Attributes and Objects
"""
Any attribute of an object can be deleted anytime, using the del statement. 

Try the following on the Python shell to see the output.

"""

class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
#c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
#c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
#c2 = ComplexNumber(5)
#c2.attr = 10

# Output: (5, 0, 10)
#print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#c1.attr

c1 = ComplexNumber(2,3)
del c1.imag
c1.getData()

del ComplexNumber.getData
c1.getData()


# We can even delete the object itself, using the del statement.

c1 = ComplexNumber(1,3)
del c1
c1
