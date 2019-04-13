# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:14:05 2018

@author: hp
"""

class Animal():

    def __init__(self):
        print(" Animal created ")

    def whoAmI(self):
        print(" Animal ")
    
    def eat(self):
        print(" eating ")

class Dog(Animal):

		def __init__(self):
			Animal.__init__(self)
			print("Dog created")

		def whoAmI(self):
			print(" Dog ")

		def bark(self):
			print(" Woolf")

class boxer(Dog):
    def __init__(self):
        Dog.__init__(self)
        print("Boxer Created")
        
    def Who(self):
        print("Boxer")
        
    def eat(self):
        print("Eating")
        


d = boxer()
d.eat()
d.bark()
d.eat()
d.Who()
d.