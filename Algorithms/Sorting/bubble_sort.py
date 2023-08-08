def bubble_sort(a):
    n=len(a)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if(swapped == False):
            break


a = [2, 5, 8, 1, 5, 3, 7]
print(a)
bubble_sort(a)
print(a)
