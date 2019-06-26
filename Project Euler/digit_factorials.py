#Factorial Function
def factorial(n):
    #End Loop
    if n == 0:
        return 1

    #Recursively Multiply
    else:
        return n * factorial(n - 1)

#Initial
total_sum = 0

#Iterate For Natural Numbers
for i in range(10, 2177281):
    #Convert to String
    SUM = 0
    string = str(i)

    #Iterate Over Digits
    for j in range(len(string)):
        SUM += factorial(int(string[j]))

    #Record if Factorion
    if SUM == i:
        total_sum += i

#Output
print total_sum
