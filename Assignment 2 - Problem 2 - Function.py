'''
Programmer: Nami Huyen T. Tram
Date: 10/27/2019
Comments: Fall 2019 - Python for Analytics - Assignment 2 -  Functions: Problem 2:
'''

# Problem definition: 
''' 
Write a program that will notify the customer the items in their cart and instruct them how to pay.
'''

try: # check for errors
    def my_function(item): #define the function
      for x in item: #the loop statement
        cart = "Item in your cart: " + x #declare the cart variable which will be call later to display the wanted sentence
        print(cart) #print the cart variable sentence
    beverage = ["coffee", "milk", "tea"] #list of items
    my_function(beverage) #call function to display list of item
    #print notification to customer
    print("Please show this confirmation and pay to the cashier at the check-out kiosk. Thank you!")
except: #catch errors
    print ("The program doesn't work at this time. Please turn it off and try it out another time.")
