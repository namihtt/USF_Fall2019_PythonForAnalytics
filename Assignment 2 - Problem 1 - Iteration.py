'''
Programmer: Nami Huyen T. Tram
Date: 10/27/2019
Comments: Fall 2019 - Python for Analytics - Assignment 2 -  Iteration: Problem 1:
'''

# Problem definition: 
''' 
Write a program that will count the distance (10 miles total) to destination to the driver when there are 2 more miles left.
'''

try: # check for errors
    distance = 10 #declare variable and the starting number of the counting
    while distance > 1: #run the loop while distance is still more than 1
        print("Distance to destination:", distance, "miles") #print statement for distance
        distance -= 1 #count distance
    # print the notification of distance to driver    
    print ("There are 2 more miles to arrive at your destination!")
except: #catch errors
    print ("The program doesn't work at this time. Please turn it off and try it out another time.")
