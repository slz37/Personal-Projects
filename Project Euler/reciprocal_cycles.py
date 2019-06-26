#Initial
d = 1
i = 0
max_dig = 0
limit = 1000

while d < limit:
    #Store Remainders
    remain = []

    #Start With Ones Digit
    dig = 1

    #Store Remainder Until Repeated
    while True:
        #Get Remainder
        i = dig % d

        #Break If Repeat
        if i in remain:
            break

        #Store i
        remain.append(i)

        #Increment to Next Digit
        dig *= 10

    #Store Max
    if len(remain) > max_dig:
        max_dig = len(remain)
        max_d = d

    #Increment
    d += 1

#Output
print max_d, ' with ', max_dig, ' digits.'
