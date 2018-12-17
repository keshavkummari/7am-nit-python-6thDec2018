# Creating Variables in Python :

#firstname = 'Guido'
middlename = 'Van'
lastname = "Rossum"

# Accesing Variables in Python :

#print(firstname)
#print("Calling a Variable i.e. FirstName : ", firstname)
#print(firstname,"We have called a Variable call Firstname")
#print("Calling Variable",firstname,"Using Print Function")

# String Special Operators :

'''
1. + : Concatenation

2. * : Repetition

3. []: Slice

4. [:]: Range Slice

5. [::] : Zero Based Indexing

6. % : Format

7. .format()
'''

#names = firstname + lastname

#print(names)
'''
Indexing 

Left to Right
0 1 2 3 4 5 nth 

Right to Left
-nth -5 -4 -3 -2 -1
'''
           #  0   1   2  3   4 Left to Right Indexing
           # -5  -4  -3 -2  -1 Right to Left Indexing
#firstname=' G   u   i  d   o'

firstname = 'Guido Van Rossum'

print('Left to Right Indexing : ',firstname[0])
print('Right to Left Indexing : ',firstname[-5])

# print('Range Slice[:]',firstname[Start index: end index]) end index -1 :

print('Range Slice[:]',firstname[2:5])

print('Range Slice[:]',firstname[1:]) # endindex-1 = 3 (0123)

           # 012121212121212121
numValues = '102030405060708090'

print("Zero Based Indexing",numValues[2::4])

"""
Below are the list of complete set of symbols which can be used along with % :

Format Symbol	Conversion
%c 				character
%s 				string conversion via str()
                                prior to formatting
%i 				signed decimal integer
%d 				signed decimal integer
%u 				unsigned decimal integer
%o 				octal integer
%x 				hexadecimal integer (lowercase letters)
%X 				hexadecimal integer (UPPERcase letters)
%e 				exponential notation (with lowercase 'e')
%E 				exponential notation (with UPPERcase 'E')
%f 				floating point real number
%g 				the shorter of %f and %e
%G 				the shorter of %f and %E
"""

print("FirstName : %s  MiddleName : %s  LastName: %s " %(firstname,middlename,lastname))
print("FirstName :",firstname,"MiddleName : ",middlename,"LastName:",lastname)

print("FirstName : {}  MiddleName : {}  LastName: {} ".format(firstname,middlename,lastname))

# raw sring : r/R r'expression' or R'expression'
print(r'c:\\users\\keshavkummari\\')
print(R'c:\\users\\keshavkummari\\')
