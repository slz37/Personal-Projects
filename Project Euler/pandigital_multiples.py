'''
-9 for n=(1...5) gives 918273645
-Must begin with 9
-Two digits n=(1...3) gives 8 digit number and n=(1...4) gives 11 digits
-Three digits gives 7 and 11
-Must be four digit number starting with 9
'''

#Pandigital Function
def pandigital(string):
    #Must Be 9 Digits
    if len(string) != 9 or '0' in string:
        return False

    #Return Boolean of Pandigital
    return all(i in string for i in list_nums)

#Initial
max_pan = 0
string = ''
list_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Iterate Over Given Range
for i in range(9000, 10000):
    #Check If Pandigitial
    if pandigital(str(i * 1) + str(i * 2)):
        #Max
        if int(str(i * 1) + str(i * 2)) > max_pan:
            max_pan = int(str(i * 1) + str(i * 2))

#Output
print max_pan
