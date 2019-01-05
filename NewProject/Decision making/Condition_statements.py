'''
1. simple if
2. if else
3.elif
4. nested elif

'''

#1. Simple if
'''
if <expression>:
    <statement>
    
Multiple line/ block -  a group of statements defined by indentation is often referred to as a suite
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
'''

var = 100
if var == 100:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

# if else
'''
if <expr>:
    <statement(s)>
else:
    <statement(s)>
'''

var_1 = 50
if var_1 > 100:
    print(var_1,"is less than 100")
    print("IF BLOCK")
else:
    print(var_1,"is not less than 100")
    print("ELSE BLOCK")
print("We are out of IF-ELSE Block")


if var_1 < 100:
    print(var_1,"is less than 100")
    print("IF BLOCK")
else:
    print(var_1,"is less than 100")
    print("ELSE BLOCK")
print("We are out of IF-ELSE Block")

#2. elif

# built-in keywordds ex:True or false (there are 33 keywords in Python)
'''
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>

Once the first condition is met, it will execute the suite and program wil exit.
'''

fee_1 = 100

if fee_1 == 20:
    print("Iam True")
elif fee_1 == 100:
    print("Iam elif block")
elif fee_1 == 100:
    print("Iam elif block2")
print("Iam out of elif")

#EXAMPLE 2 for elif

name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe- Iam example 2')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")


#Example 3

number = 23
guess = int(input('Enter the number:'))

if guess == number:
    print("You guessed it right")
elif guess < number:
    print('No, you are less')
else:
    print('no, The number is more')

'''
names = {
 'Fred': 'Hello Fred',
'Xander': 'Hello Xander',
'Joe': 'Hello Joe',
'Arnold': 'Hello Arnold'
}
if names ==joe:
    print(names.get('Joe', "I don't know who you are!"))
    
else :
    print(names.get('Rick', "I don't know who you are!"))
'''

# 3. Nested condition - if else or elif or if statements inside the nested
'''
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)
'''


#xamples

colors_1 = ['red','green','olive','yellow']

f1 = [1.0,2.0,4.0,3.0]

for var,var1 in enumerate(colors_1):
    a1 = f1[var]
    print("{} {}".format(a1 * 100, var1))

'''
var iterates with a1 and var1 iterates with enumerate(color1).

'''