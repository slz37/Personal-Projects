#Imports
from math import *

#Initial
sum_squares = 0
square_sums = 0

#Find the Sum of the Squares
for i in range(1, 101):
    sum_squares += i**2

#Find Square of Sums
for i in range(1, 101):
    square_sums += i

#Square Sums
square_sums = square_sums**2

#Output
print abs(square_sums - sum_squares)
