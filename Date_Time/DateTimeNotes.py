"""***************************************************************"""
"""
A Python program can handle date and time in several ways.

Converting between date formats is a common chore for computers.

Python's time and calendar modules help track dates and times.

What is Tick?

Time intervals are floating-point numbers inof seconds.

Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

There is a popular time module available in Python which provides
functions for working with times,and for converting between representations.

The function time.time() returns the current system
time in ticks since 12:00am, January 1, 1970(epoch)."""

# Examle:

#!/usr/bin/python3
import time  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

OUTPUT:
Number of ticks since 12:00am, January 1, 1970: 1483293277.766407
"""***************************************************************"""
NOTE:
Date arithmetic is easy to do with ticks.

However, dates before the epoch cannot be represented in this form.

Dates in the far future also cannot be represented this way -
the cutoff point is sometime in 2038 for UNIX and Windows.
"""***************************************************************"""
# TimeTuple?

Many of Pythons time functions handle time as a tuple of 9 numbers,
as shown below:

---------------------------------------------------------
Index	Field	         Values
---------------------------------------------------------
0	4-digit year	 2017
1	Month	         1 to 12
2	Day	         1 to 31
3	Hour	         0 to 23
4	Minute	         0 to 59
5	Second	         0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	 0 to 6 (0 is Monday)
7	Day of year	 1 to 366 (Julian day)
8	Daylight savings -1, 0, 1, -1 means library determines DST
"""***************************************************************"""
# Example:

#!/usr/bin/python3
import time;  # This is required to include time module.

print (time.localtime())

>>> print (time.localtime())
time.struct_time(tm_year=2017, tm_mon=1, tm_mday=3, tm_hour=10, tm_min=15,
tm_sec=32, tm_wday=1, tm_yday=3, tm_isdst=0)
"""***************************************************************"""
The above tuple is equivalent to struct_time structure.

-----------------------------------------------------------------
Index	Attributes	Values
-----------------------------------------------------------------
0	tm_year	        2016
1	tm_mon	        1 to 12
2	tm_mday	        1 to 31
3	tm_hour	        0 to 23
4	tm_min	        0 to 59
5	tm_sec	        0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	        0 to 6 (0 is Monday)
7	tm_yday	        1 to 366 (Julian day)
8	tm_isdst       -1, 0, 1, -1 means library determines DST
"""***************************************************************"""
# Getting current time :

To translate a time instant from a seconds since the
epoch floating-point
value into a time-tuple, pass the floating-point value to a
function
(e.g., localtime) that returns a time-tuple with all nine
items valid.

#!/usr/bin/python3
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

OUTPUT:
Local current time : time.struct_time(tm_year=2017, tm_mon=1, tm_mday=1,
tm_hour=23, tm_min=54, tm_sec=55, tm_wday=6, tm_yday=1, tm_isdst=0)
"""***************************************************************"""
# Getting formatted time :

"""
You can format any time as per your requirement,
but simple method to get time in readable format is asctime()"""

#!/usr/bin/python3
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
"""***************************************************************"""
# Getting calendar for a month :
'''
The calendar module gives a wide range of methods to play with yearly and monthly calendars.
Here, we print a calendar for a given month ( Jan 2008 )
'''

#!/usr/bin/python3
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

>>> import calendar
>>> cal=calendar.month(2017,1)
>>> print (cal)
    January 2017
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
"""***************************************************************"""
# The time Module :
'''
There is a popular time module available in Python which provides functions
for working with times and for converting between representations.
'''
# Below are the list of all available methods :

----------------------------------------------------------
SN	Function with Description
----------------------------------------------------------
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

"""***************************************************************"""
1. time.altzone() :

The offset of the local DST timezone,in seconds west of UTC,
if one is defined.

This is negative if the local DST timezone is east of UTC
(as in Western Europe, including the UK).

Only use this if daylight is nonzero.

# Syntax : time.altzone

#!/usr/bin/python3
import time

print ("time.altzone : ", time.altzone)

Output: time.altzone :  -23400
"""---------------------------------------------------------------"""
2. time.asctime([tupletime]) :

Accepts a time-tuple and returns a readable 24-character string such
as 'Tue Dec 11 18:07:14 2008'.

# Syntax :  time.asctime([t]))

Note: t -- This is a tuple of 9 elements or struct_time representing a time as returned
by gmtime() or localtime() function.

The method asctime() converts a tuple or struct_time representing a time as returned by gmtime()
or localtime() to a 24-character string of the following form:
    'Tue Feb 17 23:21:05 2009'.

#!/usr/bin/python3
import time

t = time.localtime()
print ("asctime : ",time.asctime(t))

Output: asctime :  Mon Jan  2 00:46:25 2017
"""---------------------------------------------------------------"""
3. time.clock( ) :

Returns the current CPU time as a floating-point number of
seconds.
To measure computational costs of different approaches,
the value of time.clock is more useful than that of time.time().

#!/usr/bin/python3
import time

def procedure():
    time.sleep(10)

# measure process time
t0 = time.clock()
procedure()
print (time.clock() - t0, "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")

Output:
2.5021119668817975 seconds process time
2.5041909217834473 seconds wall time
"""---------------------------------------------------------------"""
4. time.ctime([secs]):

Like asctime(localtime(secs)) and without
arguments is like asctime( )

# Syntax : time.ctime([ sec ])

sec -- These are the number of seconds to be
converted into string representation.

#!/usr/bin/python3
import time

print ("ctime : ", time.ctime())

Output: ctime :  Mon Jan  2 00:51:15 2017
"""---------------------------------------------------------------"""
5. time.gmtime([secs]) :

Accepts an instant expressed in seconds since the epoch and returns a time-tuple t
with the UTC time.

Note : t.tm_isdst is always 0

# Syntax : time.gmtime([ sec ])

sec -- These are the number of seconds to be converted into structure struct_time representation.

#!/usr/bin/python3
import time

print ("gmtime :", time.gmtime(1455508609.34375))

Output : gmtime : time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=3, tm_min=56,
tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)
"""---------------------------------------------------------------"""
6. time.localtime([secs]) :

Accepts an instant expressed in seconds since the epoch
and returns a time-tuple t
with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to
instant secs by local rules).

# Syntax : time.localtime([ sec ])

sec -- These are the number of seconds to be converted into
structure struct_time representation.

#!/usr/bin/python3
import time

print ("time.localtime() : %s" , time.localtime())

Output:
time.localtime() : %s time.struct_time(tm_year=2017, tm_mon=1, tm_mday=2, tm_hour=0,
tm_min=54, tm_sec=18, tm_wday=0, tm_yday=2, tm_isdst=0)
"""---------------------------------------------------------------"""
7. time.mktime(tupletime) :

Accepts an instant expressed as a time-tuple in local time and returns a
floating-point value with the instant expressed in seconds since the epoch.

# Syntax : time.mktime(t)

t -- This is the struct_time or full 9-tuple.

#!/usr/bin/python3
import time

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d = time.mktime(t)
print ("time.mktime(t) : %f" %  d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))

Output:
time.mktime(t) : 1455511418.000000
asctime(localtime(secs)): Mon Feb 15 10:13:38 2016
"""---------------------------------------------------------------"""
8. time.sleep(secs) :

Suspends the calling thread for secs seconds.

# Syntax : time.sleep(t)

t -- This is the number of seconds execution to be suspended.

#!/usr/bin/python3
import time

print ("Start : %s" % time.ctime())
time.sleep( 5 ) # Its wait for 5 sec and than it will execute below print function
print ("End : %s" % time.ctime())

Output:
Start : Mon Jan  2 00:57:54 2017
End : Mon Jan  2 00:57:59 2017
"""---------------------------------------------------------------"""
9. time.strftime(fmt[,tupletime]) :

Accepts an instant expressed as a time-tuple in local time and returns a string
representing the instant as specified by string fmt.

The method strftime() converts a tuple or struct_time representing a
time as returned by gmtime()
or localtime() to a string as specified by the format argument.

If t is not provided, the current time as returned by localtime() is used.
format must be a string. An exception ValueError is raised if any field in t is
outside of the allowed range.

# Syntax : time.strftime(format[, t])

t -- This is the time in number of seconds to be formatted.
format -- This is the directive which would be used to format given time.

The following directives can be embedded in the format string:

Directive
%a - abbreviated weekday name
%A - full weekday name
%b - abbreviated month name
%B - full month name
%c - preferred date and time representation
%C - century number (the year divided by 100, range 00 to 99)
%d - day of the month (01 to 31)
%D - same as %m/%d/%y
%e - day of the month (1 to 31)
%g - like %G, but without the century
%G - 4-digit year corresponding to the ISO week number (see %V).
%h - same as %b
%H - hour, using a 24-hour clock (00 to 23)
%I - hour, using a 12-hour clock (01 to 12)
%j - day of the year (001 to 366)
%m - month (01 to 12)
%M - minute
%n - newline character
%p - either am or pm according to the given time value
%r - time in a.m. and p.m. notation
%R - time in 24 hour notation
%S - second
%t - tab character
%T - current time, equal to %H:%M:%S
%u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
%U - week number of the current year, starting with the first Sunday as the first day of the first week
%V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
%W - week number of the current year, starting with the first Monday as the first day of the first week
%w - day of the week as a decimal, Sunday=0
%x - preferred date representation without the time
%X - preferred time representation without the date
%y - year without a century (range 00 to 99)
%Y - year including the century
%Z or %z - time zone or name or abbreviation
%% - a literal % character

# Below is the example:

#!/usr/bin/python3
import time

t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))

Output: Dec 31 2015 10:39:45

"""---------------------------------------------------------------"""
10. time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') :

Parses str according to format string fmt and returns the instant in time-tuple format.

The format parameter uses the same directives as those used by strftime();
it defaults to "%a %b %d %H:%M:%S %Y" which matches the formatting returned by ctime().

If string cannot be parsed according to format, or if it has excess data after parsing,
ValueError is raised.

# Syntax : time.strptime(string[, format])

string -- This is the time in string format which would be parsed
based on the given format.

format -- This is the directive which would be used to parse the
given string.

# Example:

#!/usr/bin/python3
import time

struct_time = time.strptime("30 12 2015", "%d %m %Y")
print ("tuple : ", struct_time)

Output:
tuple :  time.struct_time(tm_year=2015, tm_mon=12, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=364, tm_isdst=-1)

"""---------------------------------------------------------------"""
11. time.time( ) :

Returns the current time instant, a floating-point number of
seconds since the epoch.

# Syntax : time.time()

#!/usr/bin/python3
import time

print ("time.time(): %f " %  time.time())
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))

Output:
time.time(): 1483299380.359852
time.struct_time(tm_year=2017, tm_mon=1, tm_mday=2, tm_hour=1, tm_min=6, tm_sec=20, tm_wday=0, tm_yday=2, tm_isdst=0)
Mon Jan  2 01:06:20 2017

"""---------------------------------------------------------------"""
12. time.tzset() :

Resets the time conversion rules used by the library routines.
The environment variable TZ specifies how this is done.

The standard format of the TZ environment variable is
(whitespace added for clarity):

std offset [dst [offset [,start[/time], end[/time]]]]

std and dst: Three or more alphanumerics giving the timezone abbreviations. These will be propagated into time.tzname.
offset: The offset has the form: .hh[:mm[:ss]]. This indicates the value added the local time to arrive at UTC. If preceded by a '-', the timezone is east of the Prime Meridian; otherwise, it is west. If no offset follows dst, summer time is assumed to be one hour ahead of standard time.
start[/time], end[/time]: Indicates when to change to and back from DST. The format of the start and end dates are one of the following:
Jn: The Julian day n (1 <= n <= 365). Leap days are not counted, so in all years February 28 is day 59 and March 1 is day 60.
n: The zero-based Julian day (0 <= n <= 365). Leap days are counted, and it is possible to refer to February 29.
Mm.n.d: The d'th day (0 <= d <= 6) or week n of month m of the year (1 <= n <= 5, 1 <= m <= 12, where week 5 means 'the last d day in month m' which may occur in either the fourth or the fifth week). Week 1 is the first week in which the d'th day occurs. Day zero is Sunday.
time: This has the same format as offset except that no leading sign ('-' or '+') is allowed. The default, if time is not given, is 02:00:00.

# Syntax : time.tzset()

# Example:

#!/usr/bin/python3
import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))

"""***************************************************************"""
There are following two important attributes available with time module:

1. time.timezone : Attribute time.timezone is the offset in seconds of the local time zone
(without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).

2. time.tzname : Attribute time.tzname is a pair of locale-dependent strings,
which are the names of the local time zone without and with DST, respectively.
"""***************************************************************"""
# The calendar Module :
'''
The calendar module supplies calendar-related functions,
including functions to print a text calendar for a given month or year.

By default, calendar takes Monday as the first day of the week and Sunday as the last one.

To change this, call calendar.setfirstweekday() function.'''

#!/usr/bin/python3
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

# Example:
import calendar
print(calendar.calendar(2016))

# Below are the list of functions available with the calendar module:

1. calendar.calendar(year,w=2,l=1,c=6)
2. calendar.firstweekday( )
3. calendar.isleap(year)
4. calendar.leapdays(y1,y2)
5. calendar.month(year,month,w=2,l=1)
6. calendar.monthcalendar(year,month)
7. calendar.monthrange(year,month)
8. calendar.prcal(year,w=2,l=1,c=6)
9. calendar.prmonth(year,month,w=2,l=1)
10. calendar.setfirstweekday(weekday)
11. calendar.timegm(tupletime)
12. calendar.weekday(year,month,day)

"""***************************************************************"""
SN	Function with Description
"""***************************************************************"""
1	calendar.calendar(year,w=2,l=1,c=6) :
        Returns a multiline string with a calendar for year year formatted into three
        columns separated by c spaces.
        w is the width in characters of each date; each line has length 21*w+18+2*c.
        l is the number of lines for each week.


"""---------------------------------------------------------------"""
2	calendar.firstweekday( )
	Returns the current setting for the weekday that starts each week.
	By default, when calendar is first imported, this is 0, meaning Monday.
"""---------------------------------------------------------------"""
3	calendar.isleap(year)
	Returns True if year is a leap year; otherwise, False.
"""---------------------------------------------------------------"""
4	calendar.leapdays(y1,y2)
	Returns the total number of leap days in the years within range(y1,y2).
"""---------------------------------------------------------------"""
5	calendar.month(year,month,w=2,l=1)
	Returns a multiline string with a calendar for month month of year year,
	one line per week plus two header lines.
	w is the width in characters of each date; each line has length 7*w+6.
	l is the number of lines for each week.
"""---------------------------------------------------------------"""
6	calendar.monthcalendar(year,month)
	Returns a list of lists of ints. Each sublist denotes a week.
	Days outside month month of year year are set to 0;
	days within the month are set to their day-of-month, 1 and up.
"""---------------------------------------------------------------"""
7	calendar.monthrange(year,month)
	Returns two integers. The first one is the code of the weekday for the first
	day of the month month in year year; the second one is the number of days in the month.
	Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.
"""---------------------------------------------------------------"""
8	calendar.prcal(year,w=2,l=1,c=6)
	Like print calendar.calendar(year,w,l,c).
"""---------------------------------------------------------------"""
9	calendar.prmonth(year,month,w=2,l=1)
	Like print calendar.month(year,month,w,l).
"""---------------------------------------------------------------"""
10	calendar.setfirstweekday(weekday)
	Sets the first day of each week to weekday code weekday.
	Weekday codes are 0 (Monday) to 6 (Sunday).
"""---------------------------------------------------------------"""
11	calendar.timegm(tupletime)
	The inverse of time.gmtime: accepts a time instant in time-tuple form and returns
	the same instant as a floating-point number of seconds since the epoch.
"""---------------------------------------------------------------"""
12	calendar.weekday(year,month,day)
	Returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday);
	month numbers are 1 (January) to 12 (December).
"""---------------------------------------------------------------"""

"""***************************************************************"""
# Other Modules & Functions:

The datetime Module

The pytz Module

The dateutil Module
"""***************************************************************"""

"""***************************************************************"""
