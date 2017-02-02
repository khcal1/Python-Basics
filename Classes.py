# This program

import os
import sys
import random

class Pets:

# Constructor

def __int__ (self, name, weight, height, sound):
    self.__name = name
    self.__weight = weight
    self.__height = height
    self.__sound = sound





# Capsulation (if the information here passed is vaild, then pass it)
def set_name(self, name):
    self.__name = name

def get_name(self):
    return self.__name

def set_weight(self, weight):
    self.__weight = weight

def get_weight(self):
    return str(self.__weight) # conversion from and int to a string

def set_height(self, height):
    self.__height = height

def get_height(self):
    return str(self.__height)

def set_sound(self, sound):
    self.__sound = sound

def get_sound(self):
    return self.__sound




# Polymorphism

def get_type(self):
    print('Pets')

def toString(self):
    return "{} is {} cm tall, and {} kilograms, and says {}".format(self.__get_name,
    self.__get_height,
    self.__get_weight,
    self.__get_sound)


# creating the object

snake = Pets('roscoe', 3, 45, 'ssssss') #a bit confused about this error
print(snake.toString())


# If you want to create another class and inherit the variables from that class

class Dog(Pets):
    __owner = ''

def __init__ (self, name, weight, height, sound, owner):
    self.__owner = owner
    super(Dog, self).__init__(name,height,weight,sound)

def set__owner (self,owner):
    self.__owner = owner

def get__owner(self):
    return self.__owner

def get_typee(self):
    print("Dog")

def toDogString(self):
    return "{} is {} cm tall, and {} kilograms, and says {} and owner is {}".format(self.__name,
    self.__height,
    self.__weight,
    self.__sound,
    self.__owner)
