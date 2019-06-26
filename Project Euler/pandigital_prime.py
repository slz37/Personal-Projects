#Pandigital Function
def pandigital(string):
    #Number of Digits
    dig = len(string)
    
    #No Zeros
    if '0' in string:
        return False

    #Return Boolean of Pandigital Up To n Digits
    return all(i in string for i in list_nums[:dig])

#Prime Checker Function
def is_prime(n):
    if (n < 2):
        return False
    else:
        return all(n % i for i in xrange(2, int(n**0.5) + 1))

#Initial
max_prime_pan = 0
list_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Run Up to Nine Digit Number
for i in range(1234567, 7654321):
    #Prime, Pandigital, Max
    if is_prime(i) and pandigital(str(i)) and i > max_prime_pan:
        max_prime_pan = i

#Output
print max_prime_pan
