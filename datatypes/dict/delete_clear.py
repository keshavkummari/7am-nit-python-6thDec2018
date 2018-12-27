#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])

#del dict['Name']; # remove entry with key 'Name'

#del dict

#print ("dict['Name']: ", dict['Name'])
#print ("dict['Age']: ", dict['Age'])
#print ("dict['Class']: ", dict['Class'])

dict.clear()     # remove all entries in dict

print(dict)

dict1 = {'Name':"Guido Van Rossum"}

dict2 = dict1.copy()

print(dict2)


a = {0:1,1:2}

b = a.copy()

