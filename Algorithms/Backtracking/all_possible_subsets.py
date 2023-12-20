def subsets(nums):
    def backtrack(start,path):
        result.append(path)
        for i in range(start,len(nums)):
            backtrack(i+1,path + [nums[i]])
    result = []
    backtrack(0,[])
    return result

nums = [0,1,2]
print(subsets(nums))