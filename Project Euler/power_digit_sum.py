#Imports
from math import *

#Initial
SUM = 0s
num = 2**1000

#Convert to String
string = str(num)

#Length of String
length = len(string)

#Add Digits Together
for i in range(length):
    SUM += int(string[i])

#Output
print SUM
