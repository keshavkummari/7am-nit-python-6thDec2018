#SETS

print ('Print the First output for set', set('aAaaadbcdefjrhADFJM')) #Sets print only UNIQUE value and no repetition.

print ('Printing a list', set ([12324, 'absdddd', 1020, 1020, 12324])) #with list
print ('Printing a string ', set ((12324, 'absdddd', 1020, 1020, 12324))) #With String
print('Printing a dict ',set({1:10, 2:20, 3:30,1:123,2:2431,3:213})) # with KEYS only unique not repeated, duplicates are skipped.

#union method
print ('printing union',set([1,2,3,4,5,6]).union(set([4,5,6,7,'abc'])))

list1= [1,2,3,3,4,5,6,7,8,8,9,5,3,5,7,8,3,5,6]
string2 = "I love python code"

print(set(list1).union(set(string2)))

#intersection method

x=[1,2,3,4,5]
y=[5,6,7]

print ('Intersection value', set(x).intersection(set(y)))

#Difference method - prints set of unique values in the FIRST variable compared to the second

print('Difference value',set(x).difference(set(y)))
print('Difference value in string',set(list1).difference(set(y)))

#symmetric difference - prints set of unique value in FIRST and Second variable

print('Symmetric Difference value',set(x).symmetric_difference(set(y)))

#update method
s1= set([1,2,3,4,5])
s1.update(set([1,2,3,4,6,7,8]))
print('Update Method output',s1)

#intersection_update

#difference_update-similar to difference

#add
'''
s2= set([2])
s2.add([9,10,11])
print('add Method output',s2)
'''
#remove #remove element if available, if not error
#discard - remove element if available, if not prints the avaialble element


#pop

#issubset

s6= set(("abc", "efg"))
s7= [1,3]

print("issubset", set(s6).issubset(set(s7))) #if s6/s7 is different prints false

s11= [1,2,3,3,4,5,6,7,8,8,9,5,3,5,7,8,3,5,6]
s12= [1,2,3,4,5,6,7]
print("issubset2", set(s11).issubset(set(s12))) # if both variables have EQUAL matching elements then TRUE
print("issubset3", set(s12).issubset(set(s11))) #compares variable 1 with variable 2, if available TRUE

#issuperset - Elements in variable A should EXACTLY match with elements in variable B- condition TRUE
s13= set([2,9,7,1])
s14= set([2,9,7,1])
print("issuperset", set(s12).issubset(set(s14)))

#copy

s15 = set(("abc"))
s16 = set (("123"))

print(s15)