tup1 = ("aws",'azure',1997,2050,50.75)

tup2 = (1,2,3,4,5,6,7)

print(tuple(enumerate(tup1)),type(tup1),id(tup1),len(tup1))

print(tuple(enumerate(tup2)),type(tup2),id(tup2),len(tup2))

print(tup1[:5])  # startindex:endindex (endindex-1; 5-1=4)

#del tup1

# del tup1[0] # TypeError: 'tuple' object doesn't support item deletion

print(tup1)#!/usr/bin/python

# tuple1, tuple2 = (123, 'xyz', 'minnu'), (456, 'abc')

tuple1=(123, 'xyz', 'minnu')
tuple2=(456, 'abc')

"""
print ("First tuple length : ", len(tuple1),type(tuple1))
print ("Second tuple length : ", len(tuple2))
"""
tuple1, tuple2 = ('123', 'xyz', 'minnu', 'abc'), (456, 700, 200)

print ("Min value element : ", min(tuple1))
print ("Max value element : ", max(tuple1))

print ("Min value element : ", min(tuple2))
print ("Max value element : ", max(tuple2))


aList = [123, 'xyz', 'minnu', 'abc']
aTuple = tuple(aList)

print ("Tuple elements : ",type(aTuple),aTuple)

print("Convert tuple into list",list(aTuple))
#!/usr/bin/python

# tuple1, tuple2 = (123, 'xyz', 'minnu'), (456, 'abc')

tuple1=(123, 'xyz', 'minnu')
tuple2=(456, 'abc')

"""
print ("First tuple length : ", len(tuple1),type(tuple1))
print ("Second tuple length : ", len(tuple2))
"""
tuple1, tuple2 = ('123', 'xyz', 'minnu', 'abc'), (456, 700, 200)

print ("Min value element : ", min(tuple1))
print ("Max value element : ", max(tuple1))

print ("Min value element : ", min(tuple2))
print ("Max value element : ", max(tuple2))


aList = [123, 'xyz', 'minnu', 'abc']
aTuple = tuple(aList)

print ("Tuple elements : ",type(aTuple),aTuple)

print("Convert tuple into list",list(aTuple))


tup = (1,2, [1,3])

print(tup,type(tup),tuple(enumerate(tup)))
