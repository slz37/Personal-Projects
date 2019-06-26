#Triangle Function
def is_triangle(a, b, c):
    return a**2 + b**2 == c**2

#Initial
max_p = 0
max_num_solutions = 0

#Iterate Perimeter Values
for p in range(3, 1001):
    #Reset
    num_solutions = 0
    
    #Iterate First Side
    for a in range(1, p):
        #Iterate Second Side
        for b in range(a + 1, p - a):
            #Calculate Third Side
            c = p - a - b
            
            #Count Solution If Sides Form Triangle of Perimeter p
            if is_triangle(a, b, c):
                num_solutions += 1
                
    #Store p and Number of Solutions
    if num_solutions > max_num_solutions:
        max_p = p
        max_num_solutions = num_solutions

#Output
print max_p, max_num_solutions
