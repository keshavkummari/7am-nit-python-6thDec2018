"""
seq_01 = ('Name','Age','Gender') # Tuple Variable

dict_01 = dict.fromkeys(seq_01) # Part of Built-in Function i.e. dict() calling tuple variable

print("New Dict : %s" %(dict_01))

dict_02 = dict.fromkeys(seq_01,'PyWorld')

print("Update Values to All the Keys: %s" %(dict_02))
"""

pystudents = {'Name':'Guido','MiddleName':'Van',"LastName":"Rossum"}

javastudents = {'FirstName':'Keshav','LastName':'Kummari'}

pystudents.update(javastudents)

print("Values are : %s" %(pystudents))