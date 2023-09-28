def printJobScheduling(arr,k):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2] < arr[j+1][2]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    is_job = [False] * k
    job_seq = [''] * k
    # print(arr)
    for i in range(n):
        for j in range(min(k-1,arr[i][1]-1),-1,-1):
            if not is_job[j]:
                is_job[j] = True
                job_seq[j] = arr[i][0]
                break

    print(job_seq)

if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
            ['b', 1, 19],
            ['c', 2, 27],
            ['d', 1, 25],
            ['e', 3, 15]]
 
 
    print("Following is maximum profit sequence of jobs")
 
    printJobScheduling(arr, 3)