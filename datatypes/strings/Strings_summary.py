'''
1# Removing spaces from the string
1. rstrip()===>To remove spaces at right hand side
2. lstrip()===>To remove spaces at left hand side
3. strip() ==>To remove spaces both sides
'''
city =" Hyderabad "
city2 = "Tan uj"
print(city.strip())
print(city.rstrip())
print(city.lstrip())
print(city2.strip())

'''
Output:
Hyderabad
 Hyderabad
Hyderabad 
Tan uj
'''

'''
2. Finding Substrings: We can use the following 4 methods
1. find() : Returns index of first occurrence of the given substring. If it is not available then we will get -1 
2. index() : index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.
For forward direction: 
1. find() 2.index() 
For backward direction: 
1.rfind() 2.rindex() 
Eg: 
1) s="Learning Python is very easy"   
2) print(s.find("Python")) #9   
3) print(s.find("Java"))   # -1   
4) print(s.find("r"))#3   
5) print(s.rfind("r"))#21   
Note: By default find() method can search total string. We can also specify the boundaries to search. 
s.find(substring,bEgin,end) 
It will always search from bEgin index to end-1 index    
1) s="durgaravipavanshiva"   
2) print(s.find('a'))#4       
3) print(s.find('a',7,15))#10     
4) print(s.find('z',7,15))#-1   
index() method: 
index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError. 
  
'''
s = "Hadoop"
print(s.find('o', 0, 4)) #3
print(s.index('o', 0, 4)) #3
print(s.find('doop')) #2
print(s.index('doop')) #2
#print(s.find('z')) #-1
#print(s.index('z'))  # ValueError: substring not found

''' 
#3. Counting substring in the given String: 
We can find the number of occurrences of substring present in the given string by using count() method. 
1. s.count(substring) ==> It will search through out the string 
2. s.count(substring, bEgin, end) ===> It will search from bEgin index to end-1 index 
'''
s="abcabcab"
print(s.count('a')) #3
print(s.count('ab')) #3
print(s.count('a', 3, 7)) #2

'''
#4. Replacing a string with another string: 
s.replace(oldstring,newstring) : inside s, every occurrence of oldstring will be replaced with newstring. 
 
Eg1: 
s="Learning Python is very difficult" 
s1=s.replace("difficult","easy") 
print(s1) 
Output: Learning Python is very easy  
Eg2: All occurrences will be replaced 
s="ababababababab" s1=s.replace("a","b") print(s1) 
Output: bbbbbbbbbbbbbb 
'''
s="sravanthi loves srinivas"
print("Before kid: ", s)
print("After kid: ", s.replace("srinivas", "Tanuj"))

'''
Q. String objects are immutable then how we can change the content by using replace() method. 
Once we creates string object, we cannot change the content.This non changeable behaviour is nothing but immutability. 
If we are trying to change the content by using any method, then with those changes a new object will be created and changes won't be happend in existing object. 
Hence with replace() method also a new object got created but existing object won't be changed. 
Eg: 
s="abab" 
s1=s.replace("a","b") 
print(s,"is available at :",id(s)) 
print(s1,"is available at :",id(s1)) 
 
Output: 
abab is available at : 4568672 
bbbb is available at : 4568704 
In the above example, original object is available and we can see new object which was created because of replace() method. 
'''

'''
#5. Splitting of Strings: 
We can split the given string according to specified seperator by using split() method. 
l=s.split(seperator) 
The default seperator is space. The return type of split() method is List 
'''
s= "Srini Software Solutions"
s1 = "Tanuj,Toys,Industries"
s2='22-02-1989'
print(s.split()) #['Srini', 'Software', 'Solutions']
print(s1.split(',')) #['Tanuj', 'Toys', 'Industries']
print(s2.split('-')) #['22', '02', '1989']

'''
#6. Joining of Strings
We can join a group of strings(list or tuple) wrt the given seperator. 
s=seperator.join(group of strings) 
'''

t=('sunny','bunny','chinny')
s='-'.join(t)
print(s) #Output: sunny-bunny-chinny 
l=['hyderabad','singapore','london','dubai']
s=':'.join(l)
print(s) #hyderabad:singapore:london:dubai 

'''
#7. Changing case of a String
We can change case of a string by using the following  5methods. 
1. upper()===>To convert all characters to upper case 
2. lower() ===>To convert all characters to lower case 
3. swapcase()===>converts all lower case characters to upper case and all upper case characters to lower case 
4. title() ===>To convert all character to title case. i.e first character in every word should be upper case 
and all remaining characters should be in lower case.  
5. capitalize() ==>Only first character will be converted to upper case and all remaining characters can be converted to lower case  
 
'''
s='learning Python is very Easy'
print(s.upper())    #LEARNING PYTHON IS VERY EASY
print(s.lower())    #learning python is very easy
print(s.swapcase()) #LEARNING pYTHON IS VERY eASY
print(s.title())    #Learning Python Is Very Easy
print(s.capitalize()) #Learning python is very easy   

'''
#8. Checking starting and ending part of the string
Python contains the following 2 methods for this purpose 
1. s.startswith(substring) 
2. s.endswith(substring) 
'''
s='learning Python is very easy'
print(s.startswith('learning')) #True
print(s.endswith('learning')) #False
print(s.endswith('easy'))  #True
print(s.startswith('Learning')) #False

'''
# 9. To check type of characters present in a string: 
Python contains the following methods for this purpose. 
1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 ) 
2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z) 
3) isdigit(): Returns True if all characters are digits only( 0 to 9) 
4) islower(): Returns True if all characters are lower case alphabet symbols 
5) isupper(): Returns True if all characters are upper case aplhabet symbols 
6) istitle(): Returns True if string is in title case 
7) isspace(): Returns True if string contains only spaces 

'''

print('Srini786'.isalnum())  # True
print('sriniS786'.isalpha())   #False
print('Srini'.isalpha())    #True
print('srini'.isdigit())   #False
print('786786'.isdigit())    #True
print('abc'.islower())   #True
print('Abc'.islower())  #False
print('abc123'.islower()) #True
print('ABC'.isupper())   #True
print('Learning python is Easy'.istitle()) #False
print('Learning Python Is Easy'.istitle()) #True
print('    '.isspace())  #True





