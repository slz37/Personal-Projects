#Since 20 is GCF, Start and Increment at 20
'''
Remove List
1 - All numbers divisible by 1
2 - Covered by divisible by 20
3 - Covered by divisible by 18
4 - Covered by divisible by 16
5 - Covered by divisible by 20
6 - Covered by divisible by 18
7 - Covered by divisible by 14
8 - Covered by divisible by 16
9 - Covered by divisible by 18
10 - Covered by divisible by 20
12 - Covered by divisible by 18, 20
15 - Covered by divisible by 18, 20
'''

#Initial
i = 20
check = [11, 13, 14, 16, 17, 18, 19, 20]

while True:
    #Check if Divisible Evenly For All Numbers 1 to 20
    if all(i % j == 0 for j in check):
        print i
        break

    #Increment to Next Number
    i += 20
