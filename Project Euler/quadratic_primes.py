#Imports
from time import *
from math import *

#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in xrange(2, n))

#Quadratic Formula Function
def quad(a, b, n):
    return is_prime(n**2 + a * n + b)

#Initial
a = -999
b = -1000
alim = 1000
blim = 1000
max_count = 0

#Initial Time
tinit = clock()

#Iterate Over a
for i in range(a, alim + 1):
    #Iterate Over b
    for j in range(b, blim + 1):
        #Store n and Count Number Consecutive Primes
        n = 0
        count = 0

        #Run For Given (a, b) Until 1st Non Prime quad(n)
        while True:
            #Update Prime Count if Prime and Increment, Else End
            if quad(i, j, n):
                n += 1
                count += 1
            else:
                break

        #Store if Max
        if count > max_count:
            amax = i
            bmax = j
            max_count = count
            
#Output
print 'a * b = ', amax * bmax, ' time = ', clock() - tinit, 's'
