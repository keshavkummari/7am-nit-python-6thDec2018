
1. Write a Python program to calculate the length of a string.
 Ans: 
#!/usr/bin/python
#write a program to calculate the length of the string
#Method:1
string1 = ("python","aws","azure")
print("length of the string1 :",len(string1))

#Method:2
string2 = "manohardharmala"
print("length of the string2 is :%s" %(len(string2)))

#Method:3
string3 = input("enter your name:")
print("length of the string3:",len(string3))

Output:
    length of the string1 : 3
    length of the string2 is :15
    enter your name:manohar
    length of the string3: 7 

2. Write a Python program to count the number of characters (character frequency) in a string.

Ans:
#Method :1
character1 = "Guido Van Rossum"
print("count of number of chars:",character1.count('o'))

#Method:2
from collections import Counter
character2 = ("name1","name2","name3","name1")
character3 = Counter(character2)
print(character3)

Output:
    count of number of chars: 2
    Counter({'name1': 2, 'name2': 1, 'name3': 1})

3. Write a Python program to get the last part of a string before a specified character.

Ans:
    pyworld = 'python1' 'python2''python3'
    print("last part of the string:",pyworld[-1])

Output:
    last part of the string: 3
4. Write a Python program to check whether a string starts with specified characters.
Ans:
    specified_name = "Hello Python World"
    print("check starts with specified chars :", specified_name.startswith("Hello",0,20))
    print("check starts with specified chars:",specified_name.startswith("Hello"))
    print("check starts with specified chars:",specified_name.startswith("hello")) #condition is false due to case sensitive
Output:
    check starts with specified chars : True
    check starts with specified chars: True
    check starts with specified chars: False
5. Write a Python program to print the index of the character in a string.
Ans:
    print("Index of the string :",name.index("rama"),type(name))
    print("Index of the string:",name.index("sita"))
Output:
     Index of the string : 0 <class 'str'>
     Index of the string: 5

  
