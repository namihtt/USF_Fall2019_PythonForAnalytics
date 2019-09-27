#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Programmer: Nami Huyen T. Tram
Date: 9/26/2019
Comments: Fall 2019 - Python for Analytics - Assignment 1 -  Iterations: Problem 2:
'''

# Problem definition: 
''' 
Write a program that will print out a list of people who have checked in.
'''

try: # check for errors
    #run the for loop and declare a list of elements
    for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
        checkInList = f + " has checked in." #statement of checking in
        print(checkInList) #print the list of statements of people who have checked in.
except: # catch errors
    print ("The program doesn't work at this time. Please turn it off and try it out another time.")


# In[ ]:




