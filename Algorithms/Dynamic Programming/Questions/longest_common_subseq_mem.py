
def LCS(x,y,m,n,memo=None):
    if memo is None:
        memo = {}
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]:
        memo[(m,n)] =  1 + LCS(x,y,m-1,n-1)
        return memo[(m,n)]
    else:
        memo[(m,n)] =  max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))
        return memo[(m,n)]

X = "AGGTAB"
Y = "GXTXAYB"
print(LCS(X,Y,len(X),len(Y)))