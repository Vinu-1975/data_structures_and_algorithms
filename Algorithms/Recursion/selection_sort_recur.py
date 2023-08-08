import sys

def minIndex(arr,s,e):
    sl=sys.maxsize
    min_index = 0

    for i in range(s,e):
        if(sl>arr[i]):
            sl=arr[i]
            min_index=i
    return min_index

def selection_sort(arr,start_index,end_index):
    if(start_index>=end_index):
        return
    min_index=minIndex(arr,start_index,end_index)
    a[start_index],a[min_index]=a[min_index],a[start_index]
    selection_sort(arr,start_index+1,end_index)


if __name__ == '__main__':
    a=[4,2,6,5,1,3]
    print(a)
    selection_sort(a,0,len(a))
    print(a)