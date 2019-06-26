#Imports
from math import *

#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in xrange(2, n))

#Initial
number = 600851475143
factors = []
i = 1

#Run For All Numbers <= the Number You Want
while i < number:
    if is_prime(i) == True:
        if number % i == 0:
            factors.append(i)
            print factors
    i += 1

#Output
print max(factors)
