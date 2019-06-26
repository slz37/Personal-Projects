#Import
from time import *

#Rotate String Function
def rotate(string, n):
    return string[n:] + string[:n]

#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in xrange(2, int(n**0.5) + 1))

#Initial
count = 0
tinit = clock()

#Iteratue Up To 1,000,000
for i in range(1000000):
    #Convert to String
    string = str(i)

    #Iterate For Each Digit
    for j in range(len(string)):
        if is_prime(int(rotate(string, j))):
            flag = 1
        else:
            flag = 0
            break

    #If All Circles Are Prime
    if flag == 1:
        count += 1

#Output
print count, clock() - tinit
