#Array
pal = []

#First Number
for i in range(100, 1000):
    #Check Multiplication With Every 3-Digit Number
    for j in range(100, 1000):
        product = i * j

        #Check If String is Equal to Reversed String
        if str(product) == str(product)[::-1]:
            pal.append(product)

#Output
print max(pal)
