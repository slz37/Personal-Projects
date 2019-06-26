#Triangle Number Definition
def triangle(n):
    #First Term
    i = 1
    term = 0.5 * i * (i + 1)
    
    #Run Until Term >= Sum of Digits
    while term < n:
        #Update i
        i += 1

        #New Term
        term = 0.5 * i * (i + 1)

    #Boolean if Triangle Word
    if term == n:
        return True
    else:
        return False

#Open File and Store Names
words = open('words.txt', 'r')
words = words.read().split(',')

#Initial
count = 0
alphabet = {'A': 1, 'B':2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, \
            'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

#Iterate For All Words
for i in range(len(words)):
    #Length of Word
    size = len(words[i]) - 2

    #Sum
    SUM = 0

    #Iterate For Each Letter
    for j in range(1, size + 1):
        SUM += alphabet[words[i][j]]

    #Triangle Number
    if triangle(SUM):
        count += 1

#Output
print count
