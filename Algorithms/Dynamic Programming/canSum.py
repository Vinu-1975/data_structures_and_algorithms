# Write a canSum(targetSum,numbers) that takes in a targetSum and an array of numbers as arguments.
# The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

def canSum(targetSum,numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder,numbers):
            return True
        
    return False

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))