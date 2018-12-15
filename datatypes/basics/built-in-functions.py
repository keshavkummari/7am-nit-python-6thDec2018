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

firstname = 'Guido'

print('Left to Right Indexing : ',firstname[0])
print('Right to Left Indexing : ',firstname[-5])

