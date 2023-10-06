
# *best case O(n)
# !worst case O(n^2)


def bucket_sort(arr):
    # 1. Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]  # O(n)

    # 2. Insert elements into buckets
    for num in arr:  # O(n)
        index = int(num * num_buckets)
        buckets[index].append(num)

    # 3. Sort each bucket individually
    for bucket in buckets:  # O(n log n)
        bucket.sort()

    # 4. Concatenate the result
    sorted_array = []
    for bucket in buckets:  # O(n)
        sorted_array.extend(bucket)

    return sorted_array


# Test the function
arr = [0.34, 0.58, 0.72, 0.26, 0.49, 0.11]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
