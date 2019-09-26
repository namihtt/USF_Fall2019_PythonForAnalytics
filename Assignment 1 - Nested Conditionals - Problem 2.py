#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''
Programmer: Nami Huyen T. Tram
Date: 9/26/2019
Comments: Fall 2019 - Python for Analytics - Assignment 1 - Nested conditionals: Problem 2:
'''

# Problem definition: 
''' 
Write a program that will ask for user input if they have an account yet or not, then responde accordingly to their answers: 
if they already have an account, tell them to log in;
if they haven't had an account, ask if they would like to create one or not:
if they would like to create an account, tell them to sign up,
if they wouldn't like to create an account, tell them to continue as a guest.
'''

try: # check for errors
    # declare variable and ask for input
    accountConfirmation = input("Have you ever had an account with us? Please type either 'y' for yes and 'n' for no")
    if accountConfirmation == "y": #check if user has an account
        print ("Please go ahead and sign in with your account information!")
    elif accountConfirmation == "n": #check if user doesn't have an account
        # declare for another variable and ask for user input
        accountInvitation = input("Would you like to create an account with us today? Please type either 'y' for yes and 'n' for no") 
        if accountInvitation == "y": #check if user would like to create an account
            print ("Please go ahead and sign up for your account!")
        elif accountInvitation == "n": #check if user doesn't want to create an account
            print ("You can continue as a guest!")
        else: #check if user input something different from 'y' and 'n' for the accountInvitation
            print ("Your input was invalid. Please type either 'y' for yes and 'n' for no only.")
    else: #check if user input something different from 'y' and 'n' for the accountConfirmation
        print ("Your input was invalid. Please type either 'y' for yes and 'n' for no only.")
except: # catch errors
    print ("Your input was invalid. Please go ahead and try again by enter either 'y' for yes and 'n' for no only.")


# In[ ]:




