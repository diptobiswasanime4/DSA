# find out the minimum number of coins required to get sum
# return -1 otherwise

sum = 5
coins = [1, 2, 3]

def min_coins_rec(sum, coins):
    if sum == 0:
        return 0
    if sum < 0:
        return -1
    
    minCoins = -1
    for coin in coins:
        res = min_coins_rec(sum - coin, coins)
        if res != -1:
            numCoins = res + 1
            if numCoins < minCoins or minCoins == -1:
                minCoins = numCoins
        print("res:", res)
    
    return minCoins

def min_coins_dp(sum, coins, memo): # may have issues
    if sum == 0:
        return 0
    if sum in memo is not None:
        return sum
    for coin in coins:
        if (sum - coin) >= 0:
            res = 1 + min_coins_dp(sum - coin, coins, memo)
            if (sum - coin) in memo is not None:
                if res < memo[sum - coin]:
                    memo[sum - coin] = res
                else:
                    continue
            # print("res:", res)
    return res

print(min_coins_rec(sum, coins))
print(min_coins_dp(sum, coins, {}))