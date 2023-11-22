
def fib(n):
    if n<=1:
        return n
    dp = [0]* (n+1)
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fib(6))
print(fib(16))
print(fib(116))