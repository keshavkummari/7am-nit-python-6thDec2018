# Strings

'''
Note:
A string is an immutable sequence of characters. 

Many characters are familiar from what you can type on a keyboard —
a letter, a number, a symbol, or a space. 

The string with zero characters is called the empty string.

Example: 
a_str = "Python 007 @ World"

a_str = 'Python 007 @ World'

a_str = """Python 007 @ World"""

a_str = '''
Python
007 @ World
'''
'''

# Operations:

# Methods :

1
a_str.join
2
a_str.capitalize
3
a_str.upper
4
a_str.lower
5
a_str.replace
6
a_str.find
7
a_str.rfind
8
a_str.index
9
a_str.rindex
10
a_str.partition
11
a_str.rpartition
12
a_str.split
13
a_str.isdigit
14
a_str.center
15
a_str.ljust
16
a_str.rjust
17
a_str.startswith
18
a_str.endswith
19
a_str.strip
20
a_str.lstrip
21
a_str.rstrip
22
a_seq.count

# import re
24
re.findall
25
re.search
26
re.match
27
re.split

# import random
28
random.shuffle

# STRING SPECIAL Operators :
29 %
30 +
31 *
32[]
33[:]
34[::]

# Operators : Comp
35 <
36 <=
37 >
38 >=
39 ==
40 !=
# Identity Operators:

41 is
42 is not

# Membership Operators:

43 in
44 not in

# Builtin Functions:

45
len
46
sum
47
max
48
min
49
zip
50
sorted
51
map
52
filter
53
reduce
54
any
55
all
56
enumerate
57
str
58
repr
59
bin
60
oct
61
hex
62
chr
63
ord
64
type
65
isinstance
66
dir
67
hasattr

"""
1. String Constants : 
"…", '…', """…""", '''…''', r"…", r'…', r"""…""", r'''…'''

2. Convert Value into String : 
str()

3. Unambiguous Printable Representation of Object : 
repr()

4. Format String : 
%

5. Concatenate Iterable Sequences into Strings :
a_str.join()

6. Capitalize String : 
a_str.capitalize()

7. Change Case of String : 
a_str.upper(), a_str.lower()

8. Replace Substring : 
a_str.replace()

9. Find Substring : 
a_str.find(), a_str.rfind(), a_str.index(), a_str.rindex()

10. Split String at One Delimeter : 
a_str.partition(), a_str.rpartition()

11. Split String at Multiple Delimeters : 
a_str.split()

12. Test String for Digits : 
a_str.isdigit()

13. Align String : 
a_str.center(), a_str.ljust(), a_str.rjust()

14. Check Prefix : 
a_str.startswith()

15. Check Suffix :
a_str.endswith()

16. Remove Leading and Trailing Characters :
a_str.strip(), a_str.lstrip(), a_str.rstrip()

Unsupported String Operations and Constants
"""

# Escape sequences :
\a and octal
__str__()
on
built - in types
__repr__()
on
built - in types
eval()
intern()
a_str.replace(old, new, count)
a_str.split(sep, maxsplit)
a_str.startswith(prefix)

with a tuple argument

a_str.startswith(prefix, start)
a_str.startswith(prefix, start, end)
a_str.endswith(suffix)

with a tuple argument

a_str.endswith(suffix, start)
a_str.endswith(suffix, start, end)
a_str.decode()
a_str.encode()
a_str.expandtabs()
a_str.format()
a_str.isalnum()
a_str.isalpha()
a_str.islower()
a_str.isspace()
a_str.istitle()
a_str.isupper()
a_str.rsplit()
a_str.splitlines()
a_str.swapcase()
a_str.title()
a_str.translate()
a_str.zfill()
eval()

# -------------------------------------------------------------------------#
1.
String
Constants:

Syntax:
1.
"…"
2.
'…'
3.
"""…"""
4.
'''…'''
5.
r"…"
6.
r'…'
7.
r"""…"""
8.
r'''…'''

# ...................................................................................#
# Examples:
# ...................................................................................#
Code
Output
print
""  # The empty string.
print
'Hello, world.'
Hello, world.
print
"Goodbye, cruel world."
Goodbye, cruel
world.
print
"It's a beautiful day."
It
's a beautiful day.
print
"""This is
a multi-line
string."""
This is
a
multi - line
string.

# ...................................................................................#
''' Note:

1. Typically, string constants are constructed within a matched pair of single or double quotes. 

2. A string with double quotes can contain single quotes, often used as apostrophes. 
Similarly, a string with single quotes can contain double quotes.

3. Using a pair of triple-single or triple-double quotes also creates a string, 
   but also allows the string to span over multiple lines. 
   These are primarily used as documentation strings to document the purpose of a function, method, or class definition.

Strings can contain ASCII characters.

Strings can contain escape sequences:
#...................................................................................#
1.  \'	single quote character
2.  \"	double quote character
3.  \\	backslash character
4.  \b	backspace character
5.  \f	formfeed character
6.  \n	new line character (starts a new line)
7.  \r	carriage return character
8.  \t	horizontal tab character (moves to next tab position, which is every eight characters)
9.  \v	vertical tab character
10. \x<var>NN</var>	ASCII character represented by a hexidecimal number NN

Note: 
However, raw strings, those preceded by an r, do not recognize escape sequences. 
Raw strings are typically used for regular expressions.
'''
# -------------------------------------------------------------------------#

# Convert Value into Stringstr() :

Syntax: str(x)

Examples:
# ------------------------------------------------------#
Code | Output
# ------------------------------------------------------#
print
str()  # The empty list
print
str(4859202)
4859202
print
str(True)
True
print
str('abc')
abc
print
str(None)
None
print
str((1, 2, 3, 4, 5))		(1, 2, 3, 4, 5)
print str([1, 2, 3, 4, 5])			[1, 2, 3, 4, 5]
print str({1: 'a', 2: 'b', 3: 'c'}
) {1: 'a', 2: 'b', 3: 'c'}
print str(set([1, 2, 3, 4, 5])
)		set([1, 2, 3, 4, 5])
print str(str)						<class


'str'>
class Silly:
    def __init__(self, x):
        self.x \


= x
print repr(Silly( 3))
<__main__.
Silly


object>


# .............................................................#
class Silly:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return 'Silly' + str(self


.x)

print str(Silly(3))
Silly3
# .............................................................#

# See also:
repr() —
Emphasizes unambiguity

Note:
Returns a
string that is a
printable
representation of
object an_obj.

The intent is that this8
string
should be human-readable.

For built-in types, this is
the
normal
printed representation.
For user -defined types, this defaults to a string in angle brackets that includes the type of the object.

However, a class can specify what this function returns for its instances by defining a __str__() method.
# -------------------------------------------------------------------------#
