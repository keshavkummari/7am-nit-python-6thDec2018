# for loop
'''

for iterating_var in sequence:
   statements(s)
'''

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('Current fruit :', fruits[index])

print ("Good bye!")

#range index example for for loop
for x in range(2, 6):
  print(x)
for x in range(6):
  print(x)
#Loop control : break and continue

#Nested FOR loop

#example with LIST

tech = ['cloud', 'bigdata', 'AI', 'Devops'] #variable 1
cloud_ven = ['aws','azure', 'gcp'] #variable 2

for i in tech:  #outer loop
    for var in cloud_ven: #inner loop (Important: inner loop will be execute one time for each iteration of the outer loop)
        print(i,var)

#example with dict

tech1 ={'value1': "Iam new", 'value2': "Iam old"}
cloud_ven2 = ['slow', 'learner', 'ican do it right']

for i in tech1:  #outer loop
    for var in cloud_ven2: #inner loop (Important: inner loop will be execute one time for each iteration of the outer loop)
        print(i,var)

#While loop
'''
while expression:
   statement(s)
'''
#example 1
data = 1
while data < 8:
    print(data)#infinity loop (so needs an end condition to terminate)
    data +=1 # 1+1, 2+1 continues until data < 8 and stops at 8< 8, condition is FALSE.

#example 2

data = 2
while data < 8:
    print(data)
    data +=1

    if data ==5 :
        break # 4+1=5, it stops the iteration

#example 3:
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1

    print("Good bye!")

var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   print ("You entered: ", num)

print("Good bye!")