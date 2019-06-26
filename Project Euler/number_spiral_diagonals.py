'''
Corners Follow This Rule:
n^2-n+1	      n^2
               1
n^2-2n+2       n^2-3n+3
'''
#Sum of Corners in nxn Square Functions
def corner_sum(n):
    return (n**2 - n + 1) + (n**2) + (n**2 - 2 * n + 2) + (n**2 - 3 * n + 3)

#Initial
n = 1001
SUM = 1

#Run For Each Corner
for i in range(3, n + 1, 2):
    SUM += corner_sum(i)

#Output
print SUM
