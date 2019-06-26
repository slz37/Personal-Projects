#Imports
from math import *

#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in range(2, n))

#Initialize Variables
i = 1
SUM = 0
list_primes = []
num_primes = 0
trunc_primes = []

#Check All Primes Up to 11 Truncatable
while num_primes < 11:
    #Check if Prime
    prime_test_1 = is_prime(i)

    #Store Prime in String
    string = str(i)

    #Begins With Bad Numbers
    begin_test = string.startswith(("1", "4", "6", "8", "9"))

    #Ends With Bad Numbers
    end_test = string.endswith(("0", "1", "4", "6", "8", "9"))

    #Get Number of Digits
    digits = len(str(i))
    
    #Add if Prime and Is At Least  Two Digits
    if prime_test_1 == True and digits > 1 and begin_test == False and end_test == False:
        #Remove Starting From Left and Check For Prime
        for j in range(digits - 1):
            #Remove First Digit
            string = string[1:]

            #Check If Still Prime
            prime_test = is_prime(int(string))

            #Break If Not Prime, Else Continue Checking
            if prime_test == True:
                left_test = 1
            else:
                left_test = 0
                break

        #Store Prime in String
        string = str(i)

        #Remove Starting From Right and Check For Prime
        for j in range(digits - 1):
            #Remove Last Digit
            string = string[:-1]

            #Check If Still Prime
            prime_test = is_prime(int(string))

            #Break If Not Prime, Else Continue Checking
            if prime_test == True:
                right_test = 1
            else:
                right_test = 0
                break

        #Add If Passed Both Truncate Tests
        if left_test == 1 and right_test == 1:
            trunc_primes.append(i)
            num_primes += 1
            SUM += i

    #Move to Next Number
    i += 1

    #Progress Checks Every 100,000 Numbers
    if i % 100000 == 0:
        print (i, 'yes')

#Outputs
print (trunc_primes)
print (SUM)
