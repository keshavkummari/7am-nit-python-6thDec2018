#!/usr/bin/python


dict1 = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print(dict1,type(dict1),id(dict1),len(dict1),dict(enumerate(dict1)))

dict1['Age'] = 8 # update existing entry

print(dict1)

dict1['School'] = "DPS School" # Add new entry

print(dict1)

print ("dict['Age']: ", dict1['Age'])

print ("dict['School']: ", dict1['School'])

print(dict1)
