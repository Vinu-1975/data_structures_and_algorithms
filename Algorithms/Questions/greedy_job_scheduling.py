
def printJobScheduling(arr,k):
    n = len(arr)
    
    arr.sort(key = lambda x:x[2],reverse = True)
    is_occ = [False] * k
    job_seq = [''] * k
    for i in range(n):
        for j in range(min(k-1,arr[i][1]-1),-1,-1):
            if not is_occ[j]:
                is_occ[j] = True
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
    k = 3
    printJobScheduling(arr, k)