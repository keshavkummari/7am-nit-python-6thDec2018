# Tuple is immutable (cannot be altered), coma seperator, paranthesis or quotes like strings
# creating a variable : atuple =' ', " ", ''' ''', """ """ will be printed in paranthesis or every element/string should have comma seperator.

atuple='dev', "tst", '''acc''', """prd"""
print(atuple,type(atuple),len(atuple),id(atuple))

print("This is enumerate function for tuple:", tuple(enumerate(atuple))) #to find the each element index value