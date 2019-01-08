

"""
Expection Handling in Python

1. Standard Exceptions
2. Assertions

Sanity-Check of your python code

raise-if-not statement

From Python 1.5 version

Syntax : assert Expression[, Arguments]
"""

def k(Temp):
    assert (Temp >= 0), "Colder than absolute zero!"
    return ((Temp-273)*1.8)+32

print(k(273))
print(int(k(505.78)))
print(k(-5))
