
def fib(n,memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    
    if n<=1:
        memo[n] = n
        return memo[n]
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]


print(fib(6))
print(fib(16))
print(fib(116))
