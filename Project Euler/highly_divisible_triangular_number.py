#Imports
from math import *

#Triangular Number Function
def triangular_num(x):
    #Initial
    SUM = 0

    #Add All Natural Numbers Up To x
    for i in range(1, x + 1):
        SUM += i

    #Return
    return SUM

#Divisors Function
def divisors(n):
    return sum(2 for i in range(1, int(round(sqrt(n)+1))) if not n % i)

#Initial
i = 1
div = divisors(triangular_num(i))

#Run Until Over 500 Divisors
while div <= 500:
    #Increment
    i += 1

    #New Number of Divisors
    div = divisors(triangular_num(i))

#Output
print triangular_num(i)
