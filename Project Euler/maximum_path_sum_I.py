#Initial
triangle = "75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
SUM = []
flag_center = 0
triangle_split = []

#Split Triangle Into Rows and Columns
for line in triangle.split('\n'):
    triangle_split.append(map(int, line.split()))

#Iterate For Each Row Up to Second to Last Row
for i in range(len(triangle_split) - 1):
    #Run For Each Number in Current Row
    for j in range(len(triangle_split[i])):
        #Run For Each Number Directly Below - Replacing With the Sum of Number Above
        k = j
        while k < j + 2:
            #Flag to Skip Next k After Doing a Center
            if flag_center == 1:
                k += 1
                
            #Edge Cases
            if k == 0 or k == len(triangle_split[i + 1]) - 1:
                #Reset Flag
                flag_center = 0
                
                #Calculate Current Sum
                current_sum = int(triangle_split[i][j]) + int(triangle_split[i + 1][k])
                
                #Replace if Current Sum is Higher Than Old Sum in Same Position
                if current_sum > triangle_split[i + 1][k]:
                    triangle_split[i + 1][k] = current_sum
            #Center Cases
            else:
                #Set Flag
                flag_center = 1
                
                #Calculate Current Sum
                current_sum = int(triangle_split[i][j]) + int(triangle_split[i + 1][k])

                #Calculate Next Sum
                next_sum = int(triangle_split[i][j + 1]) + int(triangle_split[i + 1][k])
                
                #Replace if Sum Is Higher Than Old Sum in Same Position
                if max(current_sum, next_sum) > triangle_split[i + 1][k]:
                    triangle_split[i + 1][k] = max(current_sum, next_sum)
            k += 1
                    
#Output
for i in range(len(triangle_split)):
    print triangle_split[i]
print max(triangle_split[len(triangle_split) -1])
