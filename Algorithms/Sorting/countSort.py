def countSort(arr):
    n = len(arr)

    output = [0] * n

    count = [0] * 256

    ans = [0] * n

    for i in range(n):
        count[ord(arr[i])] += 1

    for i in range(1,256):
        count[i] += count[i-1]

    i = n-1
    while i >=0:
        index = ord(arr[i])
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1

    i = 0

    for i in range(n):
        ans[i] = output[i]

    return ans


    




if __name__ == '__main__':
    arr = "geeksforgeeks"
    ans = countSort(arr)
    print("".join(ans))