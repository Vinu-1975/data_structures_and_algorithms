#factorial
# import sys
def Factorial(n,ans):
    if n == 1:
        print(ans)
        return
    ans*=n
    Factorial(n-1,ans)

def Factorial2(n):
    if n==1:
        return 1
    return n*Factorial2(n-1)

Factorial(4,1)
print(Factorial2(5))

# print(sys.maxsize)