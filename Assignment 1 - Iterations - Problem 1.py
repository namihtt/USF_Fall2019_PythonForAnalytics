#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
Programmer: Nami Huyen T. Tram
Date: 9/26/2019
Comments: Fall 2019 - Python for Analytics - Assignment 1 -  Iterations: Problem 1:
'''

# Problem definition: 
''' 
Write a program that will notify the hour until deparature time, which is at 5:00, then notify customers to be ready!
'''

try: # check for errors
    countingTime = 5 #declare variable and the starting number of counting
    while countingTime > 0: #run the loop while counting time is still more than 0
        print("Hour until departure:", countingTime) #print statement for counting time
        countingTime -= 1 #count time
    # print the notification of departure time to let everyone be ready    
    print ("The flight will depart at 5:00 PM. There is 60 minutes left until departure. Please be ready to get on board!")
except: # catch errors
    print ("The program doesn't work at this time. Please turn it off and try it out another time.")


# In[ ]:




