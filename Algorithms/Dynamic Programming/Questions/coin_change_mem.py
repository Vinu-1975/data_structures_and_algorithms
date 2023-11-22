# def coin_change(coins,amt,memo=None):
#     if memo is None:
#         memo = {}

#     if amt in memo:
#         return memo[amt]

#     if amt < 0:
#         return 0
#     if amt == 0:
#         return 1
#     ways = 0
#     for coin in coins:
#         ways += coin_change(coins,amt - coin,memo)
#     memo[amt] = ways
#     return memo[amt]


def coin_change(coins, amount,index = 0, memo=None):
    if memo is None:
        memo = {}
    if (amount, index) in memo:
        return memo[(amount, index)]

    if amount == 0:
        return 1

    if amount < 0 or index == len(coins):
        return 0

    # Calculate the number of ways including the current coin
    ways_with_coin = coin_change(coins, amount - coins[index], index, memo)

    # Calculate the number of ways without including the current coin
    ways_without_coin = coin_change(coins, amount, index + 1, memo)

    # Sum both ways
    memo[(amount, index)] = ways_with_coin + ways_without_coin
    return memo[(amount, index)]


print(coin_change([1, 2, 5], 5))
print(coin_change([2, 3, 5], 10))
print(coin_change([1], 0))
print(coin_change([2], 3))
print(coin_change([1, 5, 10, 25], 100))
