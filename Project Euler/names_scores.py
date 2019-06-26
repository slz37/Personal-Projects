#Open File and Store Names Alphabetically
names = open('names.txt', 'r')
names = names.readlines()
names = sorted(names[0].split(','))

#Dictionary
alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O':  15, 'P': 16, \
            'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

#Initial
scores = []

#Run For Each Name
for i in range(len(names)):
    #Reset Sum
    SUM = 0
    
    #Run For Each Letter and Add Value of Letter to Sum
    for j in range(1, len(names[i]) - 1):
        SUM += alphabet[names[i][j]]

    #Multiply By Position - Python Indexes At 0, So Add 1
    scores.append(SUM * (i + 1))

#Output
print sum(scores)
