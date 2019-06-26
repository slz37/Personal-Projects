#Factorial Function
def factorial(n):
    #End Loop
    if n == 0:
        return 1

    #Recursively Multiply
    else:
        return n * factorial(n - 1)

#Initial
SUM = 0

#Find 100! and convert to string
x = str(factorial(100))

#Length of x
leng = len(x)

#Iterate Over Digits
for i in range(leng):
    SUM += int(x[i])

#Output
print SUM
