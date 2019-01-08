"""
Regular Expressions :

Module : re

Raw String : r'expression' or R'expression'

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
\D              -- Non-digits

# Compilation Flags:
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

#----------------- Method | Functions ---------------------#

re.match() : This Function attempts to match RE Pattern to string with optional flags

Symtax : re.match(pattern,string,flags)

Pattern : Regular Expression to be matched
String  : Which would be searched to march the pattern at the beginning of the string.
Flags   : You can specify different flags using bitwise OR (|)

If the re.match function returns a Match Object on Success, None on Failure.

We use group(num) or groups() function of match object to get matched expression

group(num=0) : Returns entire match(or specific subgroup num)
groups()     : Returns all matching subgroups in a tuple output. 


import re

rawInformation = "Python is a Programming and is Scripting is Language"

matchObj = re.match(r'(.*) is', rawInformation, re.M|re.I)

if matchObj:
    print("Match Function: Yes there is match",matchObj.group())
    print("Match Function: Yes there is match", matchObj.groups())
else:
    print("Match Function: No Match Found")

import re

rawInformation = "Python is a Programming and is Scripting is Language"

matchObj = re.search(r'(.*)and(.*)', rawInformation, re.M|re.I)

if matchObj:
    print("Match Function: Yes there is match",matchObj.group())
    print("Match Function: Yes there is match", matchObj.groups())
else:
    print("Match Function: No Match Found")

# Search and Replace :

# syntax  : re.sub(pattern,replace,string,max=0)

import re

mobilenumber = "99-088-2307 # This is a Phone Number"

# Delete Python-Style Comments
num = re.sub(r'#.*$',"",mobilenumber)

print(num)

# remove anything other than digits
num = re.sub(r'\D',"",mobilenumber)

print(num)

import re

text = 'abbaaabbbbaaaaaab'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found "%s"' % match)
"""
import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text),)

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')










