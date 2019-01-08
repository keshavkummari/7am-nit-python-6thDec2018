#!/usr/bin/python

with open("aws.txt",'w') as fileObject:
	fileObject.write("This is a Test file\n")
	fileObject.write("We are working on Fiel & Dir Mgmt\n\n")
	fileObject.write("Using Python and Using Various Modules")

with open("aws.txt") as afile:
	print(afile.readline())
	print(afile.readlines())
	print(afile.tell())
	print(afile.seek(20))
	print(afile.read())
