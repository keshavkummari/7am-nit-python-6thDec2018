"""

if..elif..else

if..elif..else 


The syntax of the nested if...elif...else construct:

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)


if expression1:
   statement(s)
   if expression2:
      statement(s)
elif expression4:
   statement(s)
    if expression2:
    statement(s)
       if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
      
else:
   statement(s)
   
"""


#!/usr/bin/python
mac_os = 100

if mac_os < 200:
   print("Expression value is less than 200")
   if mac_os == 150:
      print("Which is 150")
   elif mac_os == 100:
      print ("Which is 100")
   elif mac_os == 50:
      print("Which is 50")
elif mac_os < 50:
   print("Expression value is less than 50")
else:
   print("Could not find true expression")

print("Good bye!")