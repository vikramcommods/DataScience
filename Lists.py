# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:14:31 2019

@author: reddy
"""

#Lists are ordered sequences that can hold a variety of object types

my_list = ["string", 100, 22/7]

print(my_list[2]) #does the division for you

print("{a:0.3f}".format(a=my_list[2])) #get used to using the precision function

len(my_list) #calculates the length of the list

#you can combine lists 

another_list = ["four", 2]

combined_list = my_list + another_list

print(combined_list[2:]) #takes the same arguments as strings to splice

#VERY IMPORTANT ----> You can change the value in a list unlike a string

my_list[0]= "new inserted string"

#some useful built in functions for lists

# .append allows you to place any item at the end of a list

my_list.append(4) #adds the number 4 to the end of the list

# .insert takes the index position and the value as arguments and inserts into the list

my_list.insert(2, "added value")

# .pop pops off an iten at the end of a list

my_list.pop() #this is will return the item being removed as well as removing it

popped_item = my_list.pop()

#if you use the function call .del() you won't be able to access the value like .pop()


#when you pass no index position you simply remove the item at the end
#but you can also pass an index position into the pop function 
#my_list.pop(0)


#you can also sort alphabetically and numberically

num_list = [3, 1, 6, 3]

num_list.sort() # this will just sort the list NOTE it will not return as a function arugment the sorted list

num_list.reverse() #opposite of sort is .reverse()
