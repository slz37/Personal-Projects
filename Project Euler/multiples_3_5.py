#Initial
SUM = 0

#Add Any Multiples of 3 or 5
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        SUM += i

#Output
print SUM
