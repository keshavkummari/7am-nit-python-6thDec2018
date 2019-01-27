# Python Objects and Class :


""" Table of Contents :

1. What are classes and objects in Python?

2. Defining a Class in Python

3. Creating an Object in Python

4. Constructors in Python

5. Deleting Attributes and Objects
"""

"""
What are classes and objects in Python?

Python is an object oriented programming language. 

Unlike procedure oriented programming, where the main emphasis is on functions, 
object oriented programming stress on objects.

Object is simply a collection of data (variables) and methods (functions) that act on those data. 

And, class is a blueprint for the object.

We can think of class as a sketch (prototype) of a house. 

It contains all the details about the floors, doors, windows etc. 

Based on these descriptions we build the house. 

House is the object.

As, many houses can be made from a description, we can create many objects from a class. 

An object is also called an instance of a class and the process of creating this object is 
called instantiation.
"""

"""
Defining a Class in Python?


Like function definitions begin with the keyword def, in Python, 
we define a class using the keyword class.

The first string is called docstring and has a brief description about the class. 

Although not mandatory, this is recommended.

Here is a simple class definition.

class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
"""

"""
A class creates a new local namespace where all its attributes are defined. 

Attributes may be data or functions.

There are also special attributes in it that begins with double underscores (__). 

For example, __doc__ gives us the docstring of that class.

As soon as we define a class, a new class object is created with the same name. 

This class object allows us to access the different attributes as well as to 
instantiate new objects of that class.

"""

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)


"""
Creating an Object in Python:

We saw that the class object could be used to access different attributes.

It can also be used to create new object instances (instantiation) of that class. 

The procedure to create an object is similar to a function call.

>>> ob = MyClass()
"""

"""
This will create a new instance object named ob. 

We can access attributes of objects using the object name prefix.

Attributes may be data or method. Method of an object are corresponding functions of that class. 

Any function object that is a class attribute defines a method for objects of that class.

This means to say, since MyClass.func is a function object (attribute of class), 
ob.func will be a method object.

"""

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()


"""
You may have noticed the self parameter in function definition inside the class but, 
we called the method simply as ob.func() without any arguments. It still worked.

This is because, whenever an object calls its method, the object itself is passed 
as the first argument. So, ob.func() translates into MyClass.func(ob).

In general, calling a method with a list of n arguments is equivalent to calling the 
corresponding function with an argument list that is created by inserting the method's 
object before the first argument.

For these reasons, the first argument of the function in class must be the object itself. 
This is conventionally called self. 

It can be named otherwise but we highly recommend to follow the convention.

Now you must be familiar with class object, instance object, function object, 
method object and their differences.



"""