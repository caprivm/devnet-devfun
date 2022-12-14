# Input function always return a string
# answer = input("What is the highest-grossing musical of all time? ")

# Displaying output
cables = 2
# print("I have", cables, "cables")

# slide.py
## TRYIT: Import the required math functions
from math import degrees, sqrt, atan
from urllib import robotparser

# TRYIT: Create variables to store the triangle sides input by the user
a = input("Enter the rise of the slide's ladder: ")
b = input("Enter the run of the base of the slide: ")

# TRYIT: Use the int() function to convert the input string values to integers
rise = int(a)
run = int(b)

# TRYIT: Calculate the values
sidea = rise * rise
sideb = run * run
slide = int(sqrt(sidea + sideb))

angle = int(degrees(atan(rise/run)))

# TRYIT: Create a Boolean variable to store true or false if the slide length meets safety standards
slidesafe = False

# TRYIT: Create an if...elif...else statement to test the measurements of the slide
if angle > 40:
    slidesafe = False
elif rise > 6:
    slidesafe = False
else:
    slidesafe = True

# TRYIT Use an if...else statement to test whether the Boolean variable is True or False, and print the results
if slidesafe == True:
    print("Safe! The angle is " + str(angle) + " degrees and your slide length is: " + str(slide))
else:
    print("Unsafe! The angle is " + str(angle) + " degrees and your slide length is: " + str(slide))