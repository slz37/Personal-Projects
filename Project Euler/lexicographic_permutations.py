#Imports
from itertools import permutations

#Store Permutations
print sorted({i for i in permutations('0123456789', 10)})[999999]
