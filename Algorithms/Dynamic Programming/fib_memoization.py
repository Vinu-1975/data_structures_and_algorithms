def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(6))
print(fib(7))
print(fib(77))

# Time Complexity : O(n)
# Space Complexity : O(n)