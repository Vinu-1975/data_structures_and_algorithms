def selection(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if(arr[min_idx]>arr[j]):
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx],arr[i]

array = [10, 7, 8, 9, 1, 5]
selection(array)
print(array)