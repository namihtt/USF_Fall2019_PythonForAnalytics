'''
Programmer: Nami Huyen T. Tram
Date: 10/27/2019
Comments: Fall 2019 - Python for Analytics - Assignment 2 -  Iteration: Problem 2:
'''

# Problem definition: 
''' 
Write a program that will notify the customer the items in their cart and instruct them how to pay.
'''

try: # check for errors
    for x in ["coffee", "milk", "tea"]: #the loop statement with the list of picked items
        cart = "Item in your cart: " + x #sentence to display picked item
        print(cart) #print picked item sentence
    #print notification
    print("Please show this confirmation and pay to the cashier at the check-out kiosk. Thank you!")
except: #catch errors
    print ("The program doesn't work at this time. Please turn it off and try it out another time.")

