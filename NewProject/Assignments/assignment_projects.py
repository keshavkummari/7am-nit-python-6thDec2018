'''1. Write a Python program to calculate the length of a string.

2. Write a Python program to count the number of characters (character frequency) in a string.

3. Write a Python program to get the last part of a string before a specified character.

4. Write a Python program to check whether a string starts with specified characters.

5. Write a Python program to print the index of the character in a string.
'''


#1.length of string

variable1 = "Iam first program in python:"
variable2 = "I can calculate the length:"
print("1.The string length var1:", id(variable1), len(variable1), type(variable1),enumerate(variable1))
print("1.a.The string length var2:",id(variable2), len(variable2), type(variable2), enumerate(variable2))

#2.Count characters in string
'''
#sample
txt = "PYTHON"
def count_chars(txt):
	result = 0
	for char in txt:
	    result += 1     # same as result = result + 1
	return result
print(count_chars(txt))
'''

string1="betty bought a butter"
print("2.The character count is :", string1.count('b'))
print("2.a.The character count is :", string1.count('0'))

# 3.Last part of string

print("3.The last part of string is :", string1.endswith('r'))

# 4. startswith
print("4.Print if the string starts with e :", string1.startswith('e'))

# 5. index
print("5.Printing the index in string :", string1.index('butter'))

'''
#sample 2

a = 'have a nice day'
symbol = 'abcdefghijklmnopqrstuvwxyz'
for key in symbol:
    print(key, a.count(key))
'''