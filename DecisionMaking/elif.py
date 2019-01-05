"""
fee_1 = 10

if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 15:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print("4 - Got a false expression value")
   print(fee_1)

print("Good bye!")

"""

#!/usr/bin/python
# True or False (Keywords)
balance = 100

if balance > 200:   # False
    print ("This is block 1")
    print ("THis is block 1 part 1")
#elif True:                              # Keywords [i.e. True|False]
elif balance >= 200:  # False
    print ("This is block 2")
elif balance == 200:   # False
    print ("This is block 3")
#elif balance == 200:
elif True:
    print("4th Elif")

else:
    print ("This is final else")