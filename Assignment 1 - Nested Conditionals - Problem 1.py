#!/usr/bin/env python
# coding: utf-8

# In[21]:


'''
Programmer: Nami Huyen T. Tram
Date: 9/26/2019
Comments: Fall 2019 - Python for Analytics - Assignment 1 - Nested conditionals: Problem 1:
'''

# Problem definition: 
''' 
Write a program that will ask for user input how many books they are buying, then responde accordingly to their answers: 
if they buy less than 5 books, check another conditions:
if they buy less than 4 books, check them out 
or if they buy 4 books, notify them that they could qualify for free shipping if they buy 1 more book,
if they buy 5 books or more, offer them free shipping!
'''

try: # check for errors
    orderQuantity = int(input("How many books are you buying today? ")) #declare variable, data type, and ask for input
    if orderQuantity < 5: #check if user buying less than 5 or not
        if orderQuantity < 4: #check if user buying less than 4 or not
            if orderQuantity == 0: #check if user are buying or not
                print ("We're sorry that you couldn't find any book today. We will work on expanding our selection! See you again!")
            else: #check if user are buying less than 4 but more than 0 or not
                print ("Please go ahead and enter your payment method!")
        else: #check if user buying 4 books or not
            print ("If you buy 1 more book, you could qualify for free shipping!")
    else: #check if user buying 5 or more than 5 books
        print ("You are qualified for free shipping! Please go ahead and enter your payment method!")
except: # catch errors
    print ("Your input was invalid. Please input the quantity of book you are buying today.")


# In[ ]:




