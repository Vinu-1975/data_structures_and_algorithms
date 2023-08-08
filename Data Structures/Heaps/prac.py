"""
4
C 1 2 3 4 5 6 7
PO
PL
RM
"""

n = int(input())
for _ in range(n):
    inp = input().split()
    print(inp)
    if len(inp)>1:
        a=[]
        for i in range(1,len(inp)):
            a.append(int(inp[i]))
        print(a)