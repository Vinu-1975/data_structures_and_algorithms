#print numbers from 5 to 1

def printN(n):
    if n==0:
        return
    print(n,end=" ")
    printN(n-1)

printN(5)