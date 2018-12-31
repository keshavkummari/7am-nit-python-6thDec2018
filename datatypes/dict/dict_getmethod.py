studnet = {'Name': 'Minnu', 'Age': 7, 'Education':'Python'}  # Dict Variable

print ("Value :",studnet.get('Age'))

print ("Value :",studnet.get(7)) # We can not call a value

print ("Value : %s" % studnet.get('Age'))

print ("Value : %s" % studnet.get('Education','Java'))

print ("Value : %s" % studnet.get('ProgrammingLanguage','Java'))#this is treated as key-value pair if value doesnot exist