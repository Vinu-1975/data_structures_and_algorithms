#fibonacci series method 1

def fib1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib1(n-1)+fib1(n-2)

for i in range(0,14):
    print(fib1(i))