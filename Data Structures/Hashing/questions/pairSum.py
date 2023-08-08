def findPairs(num,target):
    d={}
    for i,e in enumerate(num):
        if target - e in d:
            print('pair found',(num[d.get(target-e)],num[i]))
        
        d[e] = i
        


a = [8, 7, 2, 5, 3, 1]
target = 10

findPairs(a,target)