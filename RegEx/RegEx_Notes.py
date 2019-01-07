# Regular Expressions :

A regular expression is a special sequence of characters that helps you
match or find other strings or sets of strings, using a specialized syntax held in a pattern.

Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions in Python.

The "re" module raises the exception re.error if an error occurs while compiling or
using a regular expression.

We would cover two important functions, which would be used to handle regular expressions.

But a small thing first: There are various characters,
which would have special meaning when they are used in regular expression.

To avoid any confusion while dealing with regular expressions,
we would use Raw Strings as r'expression'.

'''*******************************************************************'''
# Basic patterns which match single chars :

a, X, 9, <      -- ordinary characters just match themselves exactly.
. (a period)    -- matches any single character except newline '\n'
\w              -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
\W              -- matches any non-word character.
\b              -- boundary between word and non-word
\s              -- matches a single whitespace character -- space, newline, return, tab
\S              -- matches any non-whitespace character.
\t, \n, \r      -- tab, newline, return
\d              -- decimal digit [0-9]
^                = matches start of the string
$                = match the end of the string
\               -- inhibit the "specialness" of a character.
'''*******************************************************************'''
# Compilation flags :

Compilation flags let you modify some aspects of how regular expressions work.

Flags are available in the re module under two names,

a long name such as IGNORECASE and a short, one-letter form such as I.

---------------------------------------------------------------
Flag	        Meaning
---------------------------------------------------------------
ASCII, A	  Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S	  Make . match any character, including newlines
IGNORECASE, I	  Do case-insensitive matches
LOCALE, L	  Do a locale-aware match
MULTILINE, M	  Multi-line matching, affecting ^ and $
VERBOSE, X
(for ‘extended’)  Enable verbose REs, which can be organized more cleanly and understandably
'''*******************************************************************'''
# The match Function :

This function attempts to match RE pattern to string with optional flags.

# Syntax : re.match(pattern, string, flags=0)

pattern	: This is the regular expression to be matched.
string	: This is the string, which would be searched to match
          the pattern at the beginning of string.
flags	: You can specify different flags using bitwise OR (|).

The re.match function returns a match object on success,
None on failure.

We use group(num) or groups() function of match object to get matched
expression.


group(num=0)	This method returns entire match (or specific subgroup num)

groups()	This method returns all matching subgroups in a tuple
(empty if there were not any)
'''*******************************************************************'''
#!/usr/bin/python3

import re # Module has been imported

line = "Python and Perl are programming and scripting languages" # String Variable

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I) # Variable and calling the module and expression

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   print ("matchObj.groups() : ", matchObj.groups())
else:
   print ("No match!!")


# Here’s a complete list of the metacharacters :

'''
. ^ $ * + ? { } [ ] \ | ( )

1. .
2. ^
3. $
4. *
5. +
6. ?
7. { }
8. [ ]
9. \
10. | \
11. ( )

For a complete list of sequences and expanded class definitions for Unicode string patterns, see the last part of Regular Expression Syntax.

1. \d : Matches any decimal digit; this is equivalent to the class [0-9].
2. \D : Matches any non-digit character; this is equivalent to the class [^0-9].
3. \s : Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
4. \S : Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
5. \w : Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
6. \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
These sequences can be included inside a character class.
For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.

The final metacharacter in this section is .. It matches anything except a newline character,
and there’s an alternate mode (re.DOTALL) where it will match even a newline.

7. '.' is often used where you want to match “any character”.
'''


# Compiling Regular Expressions :
'''
Regular expressions are compiled into pattern objects, which have methods for various operations such
as searching for pattern matches or performing string substitutions.
'''
# Example 1:
import re
p = re.compile('ab*')
print(p)


# Performing Matches
"""
Once you have an object representing a compiled regular expression, what do you do with it?

Pattern objects have several methods and attributes.

Only the most significant ones will be covered here; consult the re docs for a complete listing.

------------------------------------
Method/Attribute	| Purpose
------------------------------------
match()	            | Determine if the RE matches at the beginning of the string.
search()	        | Scan through a string, looking for any location where this RE matches.
findall()	        | Find all substrings where the RE matches, and returns them as a list.
finditer()	        | Find all substrings where the RE matches, and returns them as an iterator.

match() and search() return None if no match can be found.
If they’re successful, a match object instance is returned,
containing information about the match: where it starts and ends, the substring it matched, and more.

"""

# match object instances also have several methods and attributes; the most important ones are:
"""
====================================
Method/Attribute	Purpose
====================================
group()         	Return the string matched by the RE
start()	            Return the starting position of the match
end()	            Return the ending position of the match
span()	            Return a tuple containing the (start, end) positions of the match
"""



'''*******************************************************************'''
# The search Function :

This function searches for first occurrence of RE pattern within string with optional flags.

# Sytax : re.search(pattern, string, flags=0)

pattern	    This is the regular expression to be matched.
string	    This is the string, which would be searched to
            match the pattern anywhere in the string.
flags	    You can specify different flags using bitwise OR (|).

Note :
The re.search function returns a match object on success, none on failure.

We use group(num) or groups() function of match object to get matched expression.

group(num=0)	This method returns entire match (or specific subgroup num)
groups()	This method returns all matching subgroups in a tuple (empty if there weren't any)
'''*******************************************************************'''
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")
'''*******************************************************************'''
# Matching Versus Searching :

Python offers two different primitive operations based on regular expressions:
match checks for a match only at the beginning of the string,
while search checks for a match anywhere in the string (this is what Perl does by default).

#!/usr/bin/python3

import re

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M|re.I)

if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search(r'dogs', line, re.M|re.I)

if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
'''*******************************************************************'''
# Search and Replace :

One of the most important re methods that use regular expressions is sub.

# Syntax : re.sub(pattern, repl, string, max=0)

This method replaces all occurrences of the RE pattern in string with repl,
substituting all occurrences unless max provided.

This method returns modified string.


#!/usr/bin/python3
import re

phone = "2004-959-559 # This is Phone Number"  # String Data Type

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)

print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)

print ("Phone Num : ", num)
'''*******************************************************************'''
# Regular Expression Modifiers: Option Flags

Regular expression literals may include an optional modifier to control
various aspects of matching.

The modifiers are specified as an optional flag.

You can provide multiple modifiers using exclusive OR (|),
as shown previously and may be represented by one of these.

----------------------------------------------------
Modifier	Description
----------------------------------------------------
re.I	Performs case-insensitive matching.
re.L	Interprets words according to the current locale.
        This interpretation affects the alphabetic group (\w and \W),
        as well as word boundary behavior (\b and \B).
re.M	Makes $ match the end of a line (not just the end of the string)
        and makes ^ match the start of any line (not just the start of the string).
re.S	Makes a period (dot) match any character, including a newline.
re.U	Interprets letters according to the Unicode character set.
        This flag affects the behavior of \w, \W, \b, \B.
re.X	Permits "cuter" regular expression syntax.
        It ignores whitespace (except inside a set [] or when escaped by a backslash)
        and treats unescaped # as a comment marker.

'''*******************************************************************'''
# Regular Expression Patterns :

Except for control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves.

You can escape a control character by preceding it with a backslash.

Following table lists the regular expression syntax that is available in Python

---------------------------------------------------
Pattern	    Description
---------------------------------------------------
^	Matches beginning of line.
$	Matches end of line.
.	Matches any single character except newline. Using m option allows it to match newline as well.
[...]	Matches any single character in brackets.
[^...]	Matches any single character not in brackets
re*	Matches 0 or more occurrences of preceding expression.
re+	Matches 1 or more occurrence of preceding expression.
re?	Matches 0 or 1 occurrence of preceding expression.
re{ n}	Matches exactly n number of occurrences of preceding expression.
re{ n,}	Matches n or more occurrences of preceding expression.
re{ n, m}	Matches at least n and at most m occurrences of preceding expression.
a| b	Matches either a or b.
(re)	Groups regular expressions and remembers matched text.
(?imx)	Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.
(?-imx)	Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.
(?: re)	Groups regular expressions without remembering matched text.
(?imx: re)	Temporarily toggles on i, m, or x options within parentheses.
(?-imx: re)	Temporarily toggles off i, m, or x options within parentheses.
(?#...)	Comment.
(?= re)	Specifies position using a pattern. Doesn't have a range.
(?! re)	Specifies position using pattern negation. Doesn't have a range.
(?> re)	Matches independent pattern without backtracking.
\w	Matches word characters.
\W	Matches nonword characters.
\s	Matches whitespace. Equivalent to [\t\n\r\f].
\S	Matches nonwhitespace.
\d	Matches digits. Equivalent to [0-9].
\D	Matches nondigits.
\A	Matches beginning of string.
\Z	Matches end of string. If a newline exists, it matches just before newline.
\z	Matches end of string.
\G	Matches point where last match finished.
\b	Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.
\B	Matches nonword boundaries.
\n, \t, etc.	Matches newlines, carriage returns, tabs, etc.
\1...\9	Matches nth grouped subexpression.
\10	Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.
'''*******************************************************************'''
# Regular Expression Examples

Literal characters

Example	Description
python	Match "python".

# Character classes

-------------------------------------------------------
Example	        Description
-------------------------------------------------------
[Pp]ython	Match "Python" or "python"
rub[ye]	        Match "ruby" or "rube"
[aeiou]	        Match any one lowercase vowel
[0-9]	        Match any digit; same as [0123456789]
[a-z]	        Match any lowercase ASCII letter
[A-Z]	        Match any uppercase ASCII letter
[a-zA-Z0-9]	Match any of the above
[^aeiou]	Match anything other than a lowercase vowel
[^0-9]	        Match anything other than a digit

# Special Character Classes :
-------------------------------------------------------
Example	    Description
-------------------------------------------------------
.	Match any character except newline
\d	Match a digit: [0-9]
\D	Match a nondigit: [^0-9]
\s	Match a whitespace character: [ \t\r\n\f]
\S	Match nonwhitespace: [^ \t\r\n\f]
\w	Match a single word character: [A-Za-z0-9_]
\W	Match a nonword character: [^A-Za-z0-9_]

# Repetition Cases
-------------------------------------------------------
Example	Description
-------------------------------------------------------
ruby?	Match "rub" or "ruby": the y is optional
ruby*	Match "rub" plus 0 or more ys
ruby+	Match "rub" plus 1 or more ys
\d{3}	Match exactly 3 digits
\d{3,}	Match 3 or more digits
\d{3,5}	Match 3, 4, or 5 digits

# Nongreedy repetition

This matches the smallest number of repetitions −
-------------------------------------------------------
Example	Description
------------------------------------------------------
<.*>	Greedy repetition: matches "<python>perl>"
<.*?>	Nongreedy: matches "<python>" in "<python>perl>"

# Grouping with Parentheses
-------------------------------------------------------
Example	Description
-------------------------------------------------------
\D\d+	No group: + repeats \d
(\D\d)+	Grouped: + repeats \D\d pair
([Pp]ython(, )?)+	Match "Python", "Python, python, python", etc.

# Backreferences
This matches a previously matched group again −
-------------------------------------------------------
Example	Description
-------------------------------------------------------
([Pp])ython&\1ails	Match python&pails or Python&Pails
(['"])[^\1]*\1	Single or double-quoted string. \1 matches whatever the 1st group matched.
                  \2 matches whatever the 2nd group matched, etc.

# Alternatives
-------------------------------------------------------
Example	Description
-------------------------------------------------------
python|perl	Match "python" or "perl"
rub(y|le))	Match "ruby" or "ruble"
Python(!+|\?)	"Python" followed by one or more ! or one ?

# Anchors
This needs to specify match position.

-------------------------------------------------------
Example	Description
-------------------------------------------------------
^Python	Match "Python" at the start of a string or internal line
Python$	Match "Python" at the end of a string or line
\APython	Match "Python" at the start of a string
Python\Z	Match "Python" at the end of a string
\bPython\b	Match "Python" at a word boundary
\brub\B	\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
Python(?=!)	Match "Python", if followed by an exclamation point.
Python(?!!)	Match "Python", if not followed by an exclamation point.

# Special Syntax with Parentheses
-------------------------------------------------------
Example	Description
-------------------------------------------------------

R(?#comment)	Matches "R". All the rest is a comment
R(?i)uby	Case-insensitive while matching "uby"
R(?i:uby)	Same as above
rub(?:y|le))	Group only without creating \1 backreferenc

'''*******************************************************************'''

'''*******************************************************************'''

'''*******************************************************************'''
