"""
1. Required Arguments

2. Keyword Arguments

3. Default Arguments

4. Variable-length Arguments
"""

# 1. Required Arguments:

"""
def languages(firstname,middlename,lastname):
    'Required Arguments'
    print(firstname)
    print(middlename)
    print(lastname)
    return

# Calling a Function
languages('Guido','Van','Rossum')

# 2. Keyword Arguments

def keywordArguments(firstname,middlename,lastname):
    'Required Arguments'
    print(firstname)
    print(middlename)
    print(lastname)
    return

# Calling a Function
keywordArguments(firstname='Guido',middlename='Van',lastname='Rossum')

# 3. Default Arguments

def defaultArguments(firstname,middlename,lastname,age=50):
    'Required Arguments'
    print(firstname)
    print(middlename)
    print(lastname)
    print(age)
    return

# Calling a Function
#defaultArguments(firstname='Guido',middlename='Van',lastname='Rossum',age=30)

#defaultArguments(firstname='Guido',middlename='Van',lastname='Rossum')

#defaultArguments(firstname='Guido',middlename='Van',age=30)

# 4. Variable-length Arguments

# * : Asterisk is placed before the variable name

def info(arg1, *vartuple):
    'Variable-Length Arguments'
    print(arg1)

    for var in vartuple:
        print(var)

    return

# Calling a Function
#info(1020)

info("Variable-Length Argument","AWS","AZURE","DevOps","Python")
"""
def info(*vartuple):
    'Variable-Length Arguments'

    for var in vartuple:
        print(var)

    return

# Calling a Function

info("Variable-Length Argument","AWS","AZURE","DevOps","Python")


