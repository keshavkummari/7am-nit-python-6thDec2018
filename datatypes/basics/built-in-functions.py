FIRSTNAME = 'Guido'
middlename = "Van"
LastName = '''Rosum'''

# Accessing variables in python
print("Calling a variable firstname:", FIRSTNAME)
print(middlename, "We have called a variable middle")
print("Calling variable", LastName, "LastName")

names = FIRSTNAME + LastName
print(names)
middles = middlename * 5
print(middles)
print(FIRSTNAME[1])
print(FIRSTNAME[-1])
print(FIRSTNAME[1:5])
print(FIRSTNAME[2:4])
print(FIRSTNAME[1::2])
