
def count_and_get_inversions(arr):
    if len(arr) <= 1:
        return 0,[]

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[:mid]

    left_inv_count, left_inv_pairs = count_and_get_inversions(left)
    right_inv_count, right_inv_pairs = count_and_get_inversions(right)

    merge_inv_count , merge_inv_pairs = merge_and_count_inversions(left,right)

    total_inv_count = merge_inv_count + left_inv_count + right_inv_count
    total_inv_pairs = merge_inv_pairs + left_inv_pairs + right_inv_pairs

    return total_inv_count, total_inv_pairs

def merge_and_count_inversions(left,right):
    inv = 0
    i = j =0
    inv_pairs = []

    while i < len(left) and j < len(right):
        if left[i] < left[j]:
            i+=1
        else:
            inv += len(left) - i
            for k in range(i,len(left)):
                inv_pairs.append((left[i],left[j]))
            j += 1
    
    return inv, inv_pairs




if __name__ == "__main__":
    arr = [8, 4, 2, 1]
    inversion_count, inversion_pairs = count_and_get_inversions(arr)
    print(f"Number of inversions: {inversion_count}")
    print(f"Inversion pairs: {inversion_pairs}")