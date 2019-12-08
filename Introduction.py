# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")

a = 5; b = 6

a+b #addition
a-b #subtraction 
a/b #division 
a*b 

a**b # exponent

type(a/b)
print(a)
print(b)
type(a)

mystring = "helloworld"

first = "vikram"
last= "reddy"

fullname = first + " " + last

# simple methods that act on strings are 
#title.(), upper.(), and lower.()



print(fullname)

print("hello" +" " "world" + " " + str(a))

#use the str() method to display numbers in a print()

#strings are immutable ... have to use concatanate methods

#use the command \n within a string to go to the next line

print("This is how you \ngo to the next line")

#format() method adds string to an existing string

print("This is a string {}".format("Inserted"))

print("The {} {} {}".format("fox", "brown", "quick"))

print("The {b} {b} {c}".format(a="fox", b="brown", c="quick"))

#you can also format float numbers to a certain precision and width

pi = 22/7

print("I am going to present pi to 3 decimal places ... {p:1.3f}".format(p=pi))

#the format is {value:width.prescision f}

