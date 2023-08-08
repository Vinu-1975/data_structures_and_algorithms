def howSum(targetSum,numbers,memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0 :
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder,numbers,memo)
        if remainderResult is not None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]
        
    memo[targetSum] = None
    return memo[targetSum]

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))