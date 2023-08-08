def selection_sort(a):
    n=len(a)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(a[min_index]>a[j]):
                min_index=j

        a[i],a[min_index]=a[min_index],a[i]


a=[2,5,8,1,5,3,7]
print(a)
selection_sort(a)
print(a)