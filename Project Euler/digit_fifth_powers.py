#Sum of Digits Function
def sum_dig(digit):
    #Store Temporary Sum
    temp_sum = 0
    
    #Convert to String
    string = str(digit)

    #Iterate Over All Digits
    for i in range(len(string)):
        temp_sum += int(string[i])**5

    #Return Boolean if Sum of Fift Powers of Digits = Number
    return temp_sum == digit

#Initial
SUM = 0
max_sum = 6 * 9**5

#Iterate Up To Max Number
for i in range(10, max_sum):
    if sum_dig(i):
        print i
        SUM += i

#Output
print SUM
