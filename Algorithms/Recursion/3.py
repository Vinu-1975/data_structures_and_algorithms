#sum of n natural numbers

def naturalSum(n,sum):
    if n == 0:
        print(sum)
        return
    sum+=n
    naturalSum(n-1,sum)


def fun(n):
    if n <= 1:
        return n
    return n+fun(n-1)


print(fun(5))

naturalSum(5,0)