"""
Data Structures: Sets

A set is an unordered collection without duplicates. 

When printed, iterated upon, or converted into a sequence, 
its elements will appear in an arbitrary, implementation-dependent order.

"""

"""
1	Convert Iterable into Set 					=		set()
2	Set Union  									=		a_set.union()
3	Set Intersection   							=		a_set.intersection()
4	Set Difference 								=		a_set.difference()
5	Set Symmetric Difference 					=		a_set.symmetric_difference()
6	Set Union with Mutation  					=		a_set.update()
7	Set Intersection with Mutation 				=		a_set.intersection_update()
8	Set Difference with Mutation 				=		a_set.difference_update()
9	Set Symmetric Difference with Mutation      =		a_set.symmetric_difference_update()
10	Add Element into Set                        =		a_set.add()
11	Remove Specified Element from Set           =		a_set.remove(), a_set.discard()
12	Remove Arbitrary Element from Set           =       a_set.pop()
13	Test for Subset                             =		a_set.issubset()
14	Test for Superset                           =		a_set.issuperset()
15	Copy Set                                    =		a_set.copy()
"""

print(set('abcdefABCDEFabcdef'))

print(set(['abcdef','ABCDEF','abcdef',1020,1020]))

print(set(('abcdef','ABCDEF','abcdef',1020,1020)))

print(set({1:10,2:20,3:30,2:40}))

# Union Method :

a=[1,2,3,4,5]
b=[5,6,7]

#print(set(a).union(set(b)))

#print(set([1,2,3,4,5]).union(set([5,6,7])))


# intersection()

#print(set(a).intersection(set(b)))

# difference()

print("difference",set(a).difference(set(b)))

# symmetric_difference()

print("symmetric_difference",set(a).symmetric_difference(set(b)))

# update()

#s1 = set([1,2,3,4,5])

#s1.update(set([5,6,7]))

#print(s1)

# intersection_update()

#s1 = set([1,2,3,4,5])
#s1.intersection_update(set([5,6,7]))

#print("Intersection_update: ",s1)

# difference_update()

"""
s1 = set([1,2,3,4,5])
s1.difference_update(set([5,6,7]))

print('Difference_update : ',s1)
"""

# symmetric_difference_update()

s = set([1,2,3,4,5])
s.symmetric_difference_update(set([5,6,7]))

print('symmetric_difference_update',s)

# add()

s3 = set([1,2,3,4,5])
s3.add('Pyworld')

print(s3)

# remove()

s4 = set([1,2,3,4,5])
s4.remove(4)
print('remove : ',s4)

# discard()

s4.discard(6)

print("Discard : ", s4)

# pop()
s5 = set([1,2,3,4,5])
s5.pop()
print('pop : ',s5)

# issubset()

s6 = set([2,9,7,1])
s8 = set([2,9,7,1])

print("set8",s6.issubset(s8))

s7 = [1,7]

print("issubset: ",set(s6).issubset(set(s7)))

s9  = set([2,9,7,1])
s10 = set([1,2,3,4])

print("issubset: ",set(s9).issubset(s10))

s11  = set([2,9,7,1])
s12 = set([1,2,3,4,5,6,7,8,9])

print("issubset: ",set(s11).issubset(s12))

# issuperset()

"""
s15 = set([2,9,7,1])
s16 = set([2,9,7,1])
print("issuperset(): ",set(s15).issuperset(s16))

s15 = set([2,9,7,1])
s16 = set([2,9,7,1,4,8])
print("issuperset(): ",set(s15).issuperset(s16))

s15 = set([2,9,7,1])
s16 = set([1,2,3,4,5,6,7,8,9])
print("issuperset(): ",set(s15).issuperset(s16))

s15 = set([1,2,3,4,5,6,7,8,9])
s16 = set([2,9,7,1])
print("issuperset(): ",set(s15).issuperset(s16))

"""

s17 = set([1,2,3,4,5,6,7,8,9])

s18 = s17.copy()

print(s17,id(s17),type(s17))

print(s18,id(s18),type(s18))

print(s17 is s18)



