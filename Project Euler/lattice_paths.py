#See https://copingwithcomputers.com/2013/07/06/lattice-paths/ for information
#relating Pascal's Triangle with Lattice Paths. In this situation, we are looking for
#40 choose 20.

#Factorial Function
def factorial(n):
    #End Loop
    if n == 0:
        return 1

    #Recursively Multiply
    else:
        return n * factorial(n - 1)

#Combination Function
def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

#Initial
n = 40
k = 20

#Run Combination
ans = combination(n, k)

#Output
print ans
