# def

'''
defining function:

def my_function():
  print("Hello from a function")

  calling:
  my_function()
'''
#example1
def my_function():
  print("Hello from a function")

my_function()

def course (parameters):
    print("the value of the funtion:", parameters)
    return
a= course("python")

#example2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Example 3:
'creating a function'
def os(a):
    'Our First Custom Funtion'
    print(a)
    return
#creating a variable

name = "Guido Van Rossum"

os(name)

#Features of FUNCTION

'''
1. Required Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-length Arguments


'''
# 1. Required Arguments - Number of arguments should match the function definition

def languages(a,b,c):
    print(a)
    print(b)
    print(c)
    return
languages('tamil','english','French')

# 2. Keyword Arguments - Caller identifies arguments by parameter name

languages(a='tamil', b='French', c='english') #keword in the arguments should be exactly same

# 3. Default Arguments

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#another example
def languagesdefault(a,b,c,d='chinese'):
    print(a)
    print(b)
    print(c)
    print(d)
    return
languagesdefault('tamil','english','French','madarin') #if value is provided it takes the value, if not default value is taken

languagesdefault('tamil','english','French') #even if default argument is ignrored, it gives the output
languages( b='French',a='tamil',c='english') #even if order of arguments is changed

# 4. Variable-length Arguments

def info(arg1,*vartuple): #* is placed before variable name 'variable-length Arguments'
    print(arg1)
    for var in vartuple:
        print(var)

    return
info("variable-length argument","aws","azure","devops")