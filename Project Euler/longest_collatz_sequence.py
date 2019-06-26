#Collatz Function
def collatz(n):
    global num_terms
    
    #One
    if n == 1:
        num_terms += 1
        return num_terms
    
    #Even
    if n % 2 == 0:
        num_terms += 1
        return collatz(n / 2)

    #Odd
    if n % 2 != 0:
        num_terms += 1
        return collatz((3 * n) + 1)

#Initial
num = 1
max_term = 0
limit = 1000000

#Run For All Numbers From 1 to 1,000,000
while num < limit:
    #Reset Number of Terms
    num_terms = 0

    #Run Collatz Sequence and Gather Number of Terms
    number_terms = collatz(num)

    #Store If Maximum So Far
    if number_terms > max_term:
        max_term = number_terms
        max_number = num

    #Update
    num += 1

#Output
print max_number
