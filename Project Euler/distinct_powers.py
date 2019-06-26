#Initial
terms = []

#Iterate Over a
for a in range(2, 101):
    #Iterate Over b
    for b in range(2, 101):
        #Append If Not In terms
        if a**b not in terms:
            terms.append(a**b)

#Output
print len(terms)
