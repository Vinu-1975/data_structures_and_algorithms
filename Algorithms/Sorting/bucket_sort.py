def sort_bucket(arr):
    n_buckets = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    range_v = max_val - min_val

    buckets = [[] for _ in range(n_buckets)]

    for num in arr:
        index = int((num - min_val) / (range_v / (n_buckets - 1)))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr


arr = [12, 45, 76, 3, 6, 87, 34]
print(arr)
b = sort_bucket(arr)
print(b)
