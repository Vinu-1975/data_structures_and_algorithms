#print from 1 to 5

def printN(n):
    if n==6:
        return
    print(n)
    printN(n+1)

printN(1)