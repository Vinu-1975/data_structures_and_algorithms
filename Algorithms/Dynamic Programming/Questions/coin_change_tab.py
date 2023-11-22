# * no of ways of represent amt using denominations


def coin_change(coins, amt):
    dp = [0] * (amt + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amt + 1):
            dp[x] += dp[x - coin]

    return dp[amt]


print(coin_change([1, 2, 5], 5))
print(coin_change([2, 3, 5], 10))
print(coin_change([1], 0))
print(coin_change([2], 3))
print(coin_change([1, 5, 10, 25], 100))
