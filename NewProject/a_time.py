import time

atime = time.time() #prints number of seconds since 1970
print("calling time module", atime)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)


import calendar

cal = calendar.month(2019,1)
print(cal)

print(time.altzone)