tup1=('aws', "sec",'''2050''', 22, '1988', '2005')
tup2=(1,2,3,4,5,6,7)
print(tuple(enumerate(tup1)),type(tup1),id(tup1))
print(tuple(enumerate(tup2)),type(tup2),id(tup2))

print(tup1[:4]) #startindex:endindex (endindex-1

#del - to delete the variable permanently
# del tup1 - delete can only delete the entire keyword of the variable and not the slice.

tup3=(1,2, [3])
print(tuple(enumerate(tup3)))

#min/max values are decided based on the ASCII table- numbers/characters

tuple1, tuple2 =('123','xyz',"uyx","oejf"), ("12", "14")
print ("Min value of tuple1:", min(tuple1))

#built in function list- to convert tuple to list

print("convert tuplie to list", list(tuple1))
# to convert list to tuple

alist=[123]
print("convert to tuple", tuple(alist))

#updating a Tuple varible. - we can only concatenate and cannot modify/insert values in the variable.- IMMUTABLE

