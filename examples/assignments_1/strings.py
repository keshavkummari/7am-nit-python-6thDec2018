
#1. Write a Python program to calculate the length of a string.
str2 = 'Agni Parameswara Rao Chegondi'
print(len(str2))

#2. Write a Python program to count the number of characters (character frequency) in a string.
print(str2.count('a'))
print(str2.count('e'))

#3. Write a Python program to get the last part of a string before a specified character.
special_char = 'R'
print(str2[str2.index(special_char):])

#4. Write a Python program to check whether a string starts with specified characters.
print(str2.startswith('Agni'))
print(str2.endswith('Chegondi'))


#5. Write a Python program to print the index of the character in a string.
special_char2 = 'i'
print(str2.index(special_char2))



