
# Private Methods

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving....")

    def __updateSoftware(self):
        print("Updating Software...")

audi = Car()

audi.drive()

audi._Car__updateSoftware()


"""

class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "SuperCar"

    def drive(self):
        print('Your driving speed is', self.__maxspeed)


bmw = Car()
bmw.drive()

bmw._Car__maxspeed = 10
bmw.drive()

"""
Public Methods : Accessible from Anywhere

Private Methods : Accessible only in their own class. starts with two underscores

Public Variables : Accessible from anywhere

Private Variables : Accessible only in their own class or by a method if defined starts with two underscores.
"""


"""