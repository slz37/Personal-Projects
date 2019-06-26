#Initial Terms
previous_value = 1
current_value = 2
sum_evens = current_value
next_value = previous_value + current_value

#Run For All Values Less Than 4,000,000
while next_value < 4000000:
    previous_value = current_value
    current_value = next_value
    next_value = previous_value + current_value

    #Add If Even
    if next_value % 2 == 0:
        sum_evens += next_value

#Output
print sum_evens
