#Import
import numpy as np
from fractions import Fraction

#Lowest Denominator Function
def low_den(num, den):
    return Fraction(num, den)

#Curious Fraction Function
def curious(num, den):
    #Convert to Strings
    str1 = str(num)
    str2 = str(den)

    #Check If Numerator and Denominator Share a Number
    comp1 = [i in str2 for i in str1]
    comp2 = [i in str1 for i in str2]

    #Stop If Multiple 11
    if comp1[0] == comp1[1] or comp2[0] == comp2[1]:
        return False

    #Run If Shared Number
    if comp1:
        #Index Shared Number
        index1 = int(np.nonzero(comp1)[0])
        index2 = int(np.nonzero(comp2)[0])
        
        #Remove Shared Number
        new_num = float(str1[1 - index1])
        new_den = float(str2[1 - index2])

        #Check if Equal to Original Fraction - Return False if Den Is 0
        if new_den == 0:
            return False
        else:
            return new_num / new_den == float(num) / float(den)
    #If No Shared Number, Not Curious
    else:
        return False

#Initial
product = 1
curious_nums = []

#Iterate Over Numerator
for i in range(10, 100):
    #Iterate Over Denominator
    for j in range(10, 100):
        #Stop if Greater Than 1
        if i > j:
            continue
        n
        #Find If Curious
        if i != j and (i % 10 != 0 or j % 10 != 0):
            if curious(i, j):
                #Store Numerator and Denominator
                curious_nums.append([i, j])

#Iterate For All Curious Numbers
for i in range(len(curious_nums)):
    #Find Lowest Denominator and Multiply By Product
    product *= low_den(curious_nums[i][0], curious_nums[i][1])

#Output
print product**(-1)
