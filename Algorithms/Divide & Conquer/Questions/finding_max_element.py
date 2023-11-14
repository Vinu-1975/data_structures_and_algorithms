
def maximum_DAC(a):
    if len(a) == 1:
        return a[0]
    if len(a) > 1:
        mid = len(a) // 2

        L = a[:mid]
        R = a[mid:]

        max_L = maximum_DAC(L)
        max_R = maximum_DAC(R)

        return max(max_L,max_R)


a = [4,6,3,7,8,8,5,4,3,21,9,0]

print(maximum_DAC(a))