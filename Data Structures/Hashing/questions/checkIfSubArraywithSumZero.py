
def hasZeroSumSublist(nums):
    s = set()
    s.add(0)
    total = 0

    for i in nums:
        total+=i

        if total in s:
            return True
        s.add(total)
    return False

if __name__ == '__main__':

    nums = [4, -6, 3, -1, 4, 2, 7]

    if hasZeroSumSublist(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exist')
