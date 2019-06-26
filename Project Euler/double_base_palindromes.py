#Palindrome Function
def pal(n):
    return str(n) == str(n)[::-1]

#Convert to Base 2
def base_conv(n):
    #Store Digits
    string = ''

    #Run Until Fully Converted
    while n / 2 != 0:
        #Add Remainder to String
        string += str(n % 2)

        #Start With New n
        n = n / 2

    #Add Last Base 2 Digit
    string += str(n % 2)
    
    #Reverse String and Return Number
    return string[::-1]

#Initial
SUM = 0

#Iterate Up To 1000000
for i in range(1000000):
    #Check if Palindrome
    if pal(i):
        #Check if Palindrome In Base 2
        if pal(base_conv(i)):
            SUM += i

#Output
print SUM
