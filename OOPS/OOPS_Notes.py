"""
1. What Is Object-Oriented Programming (OOP)?

Object-oriented Programming, or OOP for short, is a programming paradigm which 
provides a means of structuring programs so that properties and behaviors are 
bundled into individual objects.


For instance, an object could represent a person with a name property, 
age, 
address, 
etc., 

with behaviors like :

walking, 
talking, 
breathing, and 
running. 

Or an email with properties like :

recipient list, 
subject, 
body, etc., 

and behaviors like adding attachments and sending.


Put another way, object-oriented programming is an approach for modeling concrete, 
real-world things like cars as well as relations between things like companies and 
employees, students and teachers, etc. 

OOP models real-world entities as software objects, which have some data associated 
with them and can perform certain functions.


Another common programming paradigm is procedural programming which structures a 
program like a recipe in that it provides a set of steps, in the form of functions 
and code blocks, which flow sequentially in order to complete a task.

The key takeaway is that objects are at the center of the object-oriented programming 
paradigm, not only representing the data, as in procedural programming, but in the 
overall structure of the program as well.
"""

"""
NOTE: Since Python is a multi-paradigm programming language, you can choose the
paradigm that best suits the problem at hand, mix different paradigms in one program,
and/or switch from one paradigm to another as your program evolves.
"""

"""
Table of Contents :

1. Introduction to OOP in Python
2. Class
3. Object
4. Methods
5. Inheritance
6. Encapsulation
7. Polymorphism
"""

"""
Introduction to OOPs in Python:

Python is a multi-paradigm programming language.

Meaning, it supports different programming approach.

One of the popular approach to solve a programming problem is by creating objects.

This is known as Object-Oriented Programming (OOP).


An object has two characteristics:

attributes
behavior

Let's take an example:

Parrot is an object,

name, age, color are attributes
singing, dancing are behavior

The concept of OOP in Python focuses on creating reusable code.
This concept is also known as DRY (Don't Repeat Yourself).
"""

"""
In Python, the concept of OOP follows some basic principles:

Inheritance	  : A process of using details from a new class without modifying existing class.

Encapsulation : Hiding the private details of a class from other objects.

Polymorphism  : A concept of using common operation in different ways for different data input.

"""


"""
Class :

A class is a blueprint for the object.

We can think of class as an sketch of a parrot with labels. 
It contains all the details about the name, colors, size etc. 
Based on these descriptions, we can study about the parrot. 

Here, parrot is an object.

The example for class of parrot can be :

class Parrot:
    pass


Here, we use class keyword to define an empty class Parrot. 

From class, we construct instances. 

An instance is a specific object created from a particular class.
    
"""

"""
Object :

An object (instance) is an instantiation of a class. 

When class is defined, only the description for the object is defined. 

Therefore, no memory or storage is allocated.

The example for object of parrot class can be:

obj = Parrot()
Here, obj is object of class Parrot.

"""

"""
Suppose we have details of parrot. 

Now, we are going to show how to build the class and objects of parrot.

"""

# Example : Creating Class and Object in Python

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


"""
Note:  Then, we define attributes. The attributes are a characteristic of an object.

Then, we access the class attribute using __class __.species.

 Similarly, we access the instance attributes using blu.name and blu.age. 
 
 However, instance attributes are different for every instance of a class.
"""