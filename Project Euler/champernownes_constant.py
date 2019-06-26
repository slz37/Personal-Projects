#Initial
i = 1
string = ''

#Run Up To 1000000 Digit
while len(string) < 1000000:
    string += str(i)
    i += 1

#Output
print int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])
