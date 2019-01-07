# Python file operations :

"""
1. Open a file
2. Read or write (perform operation)
3. Close the file

# Builtin Functions:
1. open()
2. close()

f = open("test_1.txt")    # open file in current directory
f = open("C:/Users/Jessicah Princess/Desktop/test_1.txt")  # specifying full path


# Python File Modes:
------------------
Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation.
                If the file already exists, the operation fails.
'a'		Open for appending at the end of the file
                without truncating it.
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
"""

import os
print(os.getcwd())
print(os.listdir())

#a = open("OS_Module.py")

#print(file.readline())

#print(file.readlines())

#print(file.read())

#a.close()

#print(a.read())


# Open a File for File Operations & Close in a secured  way is using try...finally method
#try..finally method :

"""
try:
    a = open("OS_Module.py")
    'Perform File Operations'
    #a.readline()
    #a.readlines()
    print(a.read())

finally:
    a.close()
"""

with open("OS_Module.py") as a:
    'Perform File Operations'
    print(a.readline())
    #print(a.readlines())
    #print(a.read())

print(a.read())