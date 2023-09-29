def max_subarray_sum(arr):
    """
    Return the maximum subarray sum using Kadane's algorithm.
    """
    # Initialize current_sum and max_sum to the first element
    current_sum = max_sum = arr[0]

    # Traverse the array starting from the second element
    for num in arr[1:]:
        # If current_sum becomes negative, reset it to the current element
        # Otherwise, add the current number to the current_sum
        current_sum = max(num, current_sum + num)

        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum

def max_subarray2(arr):
    """
    Return the maximum subarray sum and the subarray itself using Kadane's algorithm.
    """
    # Initializations
    current_sum = arr[0]
    max_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0

    # Traverse the array
    for i in range(1, len(arr)):
        # If the current number is greater than current_sum + current number
        # Update current_sum to the current number and reset temp_start
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        # If current_sum is greater than max_sum
        # Update max_sum and modify the actual start and end pointers
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end+1]

# Test
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output: 6 (subarray [4, -1, 2, 1])
max_sum, subarray = max_subarray2(arr)
print(f"Subarray: {subarray} and {max_sum}")