'''
- Number of overall digits is limited to 9, so product is limited to:
  - One Digit and Four Digit
    - Ignore 1
  - Two Digit and Three Digit
- Can skip any numbers containing 0
- Include products only once
'''
#Imports
from time import *

#Pandigital Function
def pandigital(a, b, c):
    #Convert to String
    string = str(a) + str(b) + str(c)

    #Must Be 9 Digits
    if len(string) != 9 or '0' in string:
        return False

    #Return Boolean of Pandigital
    return all(i in string for i in list_nums)
    
#Initial
SUM = 0
list_pan = []
list_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Begin Time
tinit = clock()

#Iterate For Single and Double Digit Numbers
for i in range(2, 99):
    #Iterate For Three and Four Digit Numbers
    for j in range(100, 10000):
        #Check if Product, Multiplier, Multiplicand Are Pandigital
        if pandigital(i, j, i * j):
            #Add If Product Is Not Already Recorded
            if i * j not in list_pan:
                #Add Sum
                SUM += i * j

                #Track Products
                list_pan.append(i * j)

#One Digit and Four Digit
print SUM, clock() - tinit
