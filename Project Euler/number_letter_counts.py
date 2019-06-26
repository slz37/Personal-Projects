#Count Function
def count(x):
    #Less Than 100
    if x < 100:
        #Teens Case
        if x < 20:
            return one_twenty[x]
        #Non Teens
        else:
            return twenty_above[x / 10] + one_twenty[x % 10]
    #Less Than 1,000
    else:
        #Multiple of 100 - 7 for hunded
        if x % 100 == 0:
            return one_twenty[x / 100] + 7
        #Last Two Digits < 20
        elif x % 100 < 20:
            return hundreds[x / 100] + one_twenty[x % 100]
        #Last Two Digits >= 20
        else:
            return hundreds[x / 100] + twenty_above[(x % 100) / 10] + one_twenty[x % 10]
        

#Initial
one_twenty = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7:5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
twenty_above = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
hundreds = {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14} #Includes "and"
total = 0

#Run For 1 to 1,000
for i in range(1, 1000):
    total = total + count(i)

#Output - 11 For 1,000
print total + 11
