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

#Abundant Function
def is_abundant(x):
    return factors_sum(x) > x

#Initial
SUM = 0
abundant_numbers = set()

#Check Positive Integers Up To Limit
for i in range(1, 28123):
    if is_abundant(i):
        abundant_numbers.add(i)
    if not any((i - a in abundant_numbers) for a in abundant_numbers):
        SUM += i

#Output
print SUM
