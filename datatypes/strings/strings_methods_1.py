"""
8. isalnum()
9. isnumeric()
10. isdigit()
11. isdecimal()
12. islower()
13. isupper()
14. swapcase()
15. isspace()
"""
"""
name = "37"

print(name,type(name),id(name),len(name))

print("isalnum method: ",name.isalnum())

print("isnumeric method: ", name.isnumeric())

print("isdigit method: ", name.isdigit())

print("isdecimal method: ",name.isdecimal())

print("islower method check: ", name.islower())

print("isupper method check: ", name.isupper())

print("swapcase method check: ", name.swapcase())

print("isspace method", name.isspace(),id(name),type(name),len(name))

print("istitle method: ",name.istitle())

name = "0Guido 1Van 2Rossum"
print("istitle method: ",name.istitle())
print("islower method check: ", name.islower())
print("isupper method check: ", name.isupper())
print("swapcase method check: ", name.swapcase())

print(name,type(name),id(name),len(name))
print(name.ljust(20,'9'))
print(name.rjust(20,'#'))

name = "0$#Guido Van Rossum"

#print(name.rstrip('0'))
print(name.lstrip('0$'))
print(name.strip('0$'))
"""

name = "Guido Van Rossum"

print("min method: ", min(name))
print("max method: ", max(name))

values = "0123456789"

print("min method: ", min(values))
print("max method: ", max(values))



