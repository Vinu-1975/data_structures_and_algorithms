def merge(a, L, R):
    i = j = k = 0
    inv_count = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            inv_count += len(L) - i  # Count inversions
        k += 1

    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1

    return inv_count


def merge_sort(a):
    inv_count = 0
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        inv_count += merge_sort(L)
        inv_count += merge_sort(R)

        inv_count += merge(a, L, R)

    return inv_count


# Test the function
a = [23, 5, 54, 34, 64, 32, 6, 2]
print("Original array:", a)
inversion_count = merge_sort(a)
print("Sorted array:", a)
print("Inversion count:", inversion_count)
