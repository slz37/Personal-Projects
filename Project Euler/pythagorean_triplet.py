#Imports
from math import *

#Check For All a
for a in range(1, 1000):
    #Check For All b
    for b in range(1, 1000):
        #Check For All c
        for c in range(1, 1000):
            #Check For Conditions
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                #Output
                print a * b * c
