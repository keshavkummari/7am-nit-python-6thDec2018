#What is Tick?

"""
Time intervals are floating-point numbers inof seconds.

Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

There is a popular time module available in Python which provides
functions for working with times,and for converting between representations.

The function time.time() returns the current system
time in ticks since 12:00am, January 1, 1970(epoch).

"""
import time

atime = time.time()

print("Calling a Time Module : ", atime)

#Number of ticks(seconds) since 1970

"""***************************************************************
# TimeTuple?

Many of Pythons time functions handle time as a tuple of 9 numbers,
as shown below:

---------------------------------------------------------
Index	Field	         Values
---------------------------------------------------------
0	4-digit year	    2017
1	Month	            1 to 12
2	Day	                1 to 31
3	Hour	            0 to 23
4	Minute	            0 to 59
5	Second	            0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	        0 to 6 (0 is Monday)
7	Day of year	        1 to 366 (Julian day)
8	Daylight savings    -1, 0, 1, -1 means library determines DST
***************************************************************"""

import time
print(time.localtime())

'''time.struct_time(tm_year=2019, tm_mon=1, tm_mday=14, tm_hour=7, tm_min=27, tm_sec=37, 
                 tm_wday=0, tm_yday=14, tm_isdst=0)'''

localtime = time.asctime(time.localtime(time.time()))

print(localtime)  # Mon Jan 14 07:30:09 2019

import calendar

cal = calendar.month(2019,1)

print(cal)


"""
1. time.altzone
2. time.asctime([tupletime])
3. time.clock( )
4. time.ctime([secs])
5. time.gmtime([secs])
6. time.localtime([secs])
7. time.mktime(tupletime)
8. time.sleep(secs)
9. time.strftime(fmt[,tupletime])
10. time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
11. time.time( )
12. time.tzset()

"""

import time
print(time.altzone)

t = time.localtime()
print(time.asctime(t))