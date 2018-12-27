sql_01 = ('aws','26.889','learn') #Tuple variable
dict_01 = dict.fromkeys(sql_01)
print("new disc: %s" %(dict_01))

dict_02 = dict.fromkeys(sql_01, 'pyworld')
print("update values to all the keys: %s" %(dict_02))


#UPDATE METHOD
variable1 = {'name1:''FirstN','Name2:''nono'}
variable2 = {'name2:''yes', 'Name2:''no'}
variable1.update(variable2)

print("The updated values: %s" %(variable1))
