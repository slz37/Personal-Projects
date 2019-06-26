#Initial
total = 200
count = [1] + [0] * total
coins = [1, 2, 5, 10, 20, 50, 100, 200]

#Iterate For Each Type of Coin
for coin in coins:
    #Start At Value of Coin and Add Previous Values For Every Multiple of Coin
    for i in range(coin, total + 1):
        #Add to Count
        count[i] += count[i - coin]

#Output
print count[total]
