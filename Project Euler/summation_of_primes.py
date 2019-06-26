#Get Primes
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

#Initial
SUM = 0

#Check Below 2,000,000
prime_nums = get_primes(2000000)

#Output
print sum(prime_nums)
