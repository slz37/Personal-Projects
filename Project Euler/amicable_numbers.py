#Imports
from math import *

#Factors Function
def factors_sum(n):
    #Find All Factors of n
    x = set(reduce(list.__add__, ([i, n / i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    #Remove i = n
    x.remove(n)

    #Return
    return sum(x)

#Initial
SUM = 0

#Run For Numbers Up to 10,000
for i in range(2, 10000):
    #Find Factors Sums
    first = factors_sum(i)
    second = factors_sum(first)

    #Add to Sum if Amicable - Ignore Perfect Numbers
    if second == i and factors_sum(i) != i:
        SUM += i

#Output
print SUM
