#!/usr/bin/python



# Open a file
#fo = open("C:\\Users\\Jessicah Princess\\Desktop\\sample.txt", "r+")
fo = open("/Users/keshavkummari/sample.txt", "r+")
str = fo.readline()
#str = fo.read(3)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
print("Position of the cursuer",position)
str_1 = fo.read(10)
print ("Again read String is : ", str_1)
position1 = fo.tell()
print("Position of the cursuer",position1)

position = fo.seek(2, 0)
print("Position of the cursuer",position)

# Close opend file
fo.close()

