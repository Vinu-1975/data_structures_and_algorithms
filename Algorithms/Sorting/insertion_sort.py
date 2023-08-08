
def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

def insertion(a):
    for i in range(1,len(a)):
        j=i
        while a[j]<a[j-1] and j>0:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
    return a



a=[32,45,23,5,65,34,6,4]
print(a)
insertion(a)
print(a)