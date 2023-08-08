def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))
print(fib(77))

# Time Complexity : O(2^n)
# space Complexity : O(n)