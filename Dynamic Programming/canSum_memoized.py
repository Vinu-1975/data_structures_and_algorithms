def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))