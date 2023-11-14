
#* bottom_up approach
# !kadane's algorithm

def maxSubArray(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num,curr_sum + num)
        max_sum = max(curr_sum,max_sum)
    return max_sum

# Test case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubArray(nums)
print(result) 
