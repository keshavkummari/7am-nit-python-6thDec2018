"""
seq_01 = ('Name','Age','Gender') # Tuple Variable

dict_01 = dict.fromkeys(seq_01) # Part of Built-in Function i.e. dict() calling tuple variable

print("New Dict : %s" %(dict_01))

dict_01['Name']='Guido'
dict_01['Age']=52
dict_01['Gender']='M'

print(dict_01)
"""
var1 = {'Name':'Guido','Language':'Python'}

print("%s" % var1.setdefault('Name',None))

print("%s" % var1.setdefault('Course','Django'))


#var1[0]='Van'

#var1.Name[0]='Van'

print(var1)

