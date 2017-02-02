# This program display s the concept of compund interest


'''Have the user enter their investment amount and expected interest.
   Each year their investment will increase by their investment + their investment * rate is..
   print 10 years earnings'''


import os
import sys
import random

# Ask for money invested + interest rate
mi = input("Money invested: ")
exi = input("How much interest: " )

# Convert value to float
mi = float(mi)

# Convert value to a float and round percentage rate by 2 digits
exi = float(exi) *.01

# Cycle through 10 years using a for loop and range from 0 to 9
for i in range (10):
    mi = mi + (mi * exi)

print('Investment after 10 years :{:.2f}'.format(mi))


# The {:.2f} rounds to 2 decimal places in a floating point number