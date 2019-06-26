#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in xrange(2, n))

#Initial
i = 0
num_primes = 0

#Run Until 10,001 Prime Is Found
while True:
    #Check if Prime
    if is_prime(i) == True:
        num_primes += 1

    #Break if 10,001st Prime is Found
    if num_primes == 10001:
        print i
        break

    #Increment i
    i += 1
    
