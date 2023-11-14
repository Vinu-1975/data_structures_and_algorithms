def min_denomination(a,d,memo = None):
    if memo is None:
        memo = {}
    if a in memo:
        return memo[a]
    if a == 0:
        return []
    if a < 0:
        return None
    shortestCombination = None
    for num in d:
        remains = a - num
        remainResult = min_denomination(remains,d,memo)
        if remainResult is not None:
            combination = remainResult + [num]
            if shortestCombination is None or len(shortestCombination) > len(combination):
                shortestCombination = combination
    memo[a] = shortestCombination
    return shortestCombination

a = 10
d = [7,2,3,6]
print(min_denomination(a,d))
