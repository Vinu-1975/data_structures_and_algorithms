def binary(n):
    if n==0:
        return
    binary(n//2)
    print(n%2,end="")

binary(10)