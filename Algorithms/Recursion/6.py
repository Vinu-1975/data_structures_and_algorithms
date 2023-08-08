#fibonacci series method 2

def fib2(a,b,n):
    if n==0:
        return
    print(a)
    fib2(b,a+b,n-1)

fib2(0,1,200)