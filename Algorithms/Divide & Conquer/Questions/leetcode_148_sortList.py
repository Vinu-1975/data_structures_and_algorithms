class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def get_mid(l):
    slow = l
    fast = l
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sort(l):
    if not l or not l.next:
        return l
    mid = get_mid(l)
    next_to_mid = mid.next
    mid.next = None

    left = merge_sort(l)
    right = merge_sort(next_to_mid)

    sorted_list = merge(left,right)
    return sorted_list

def merge(left,right):
    """
    4,5
    r = 4

    """
    if not left:
        return right
    if not right:
        return left
    
    if left.val <= right.val:
        result = left
        result.next = merge(left.next,right)
    else:
        result = right
        result.next = merge(left,right.next)
    return result



l = Node(4,Node(2,Node(1,Node(3))))
print(get_mid(l))
new_lst = merge_sort(l)
while new_lst:
    print(new_lst.val)
    new_lst = new_lst.next



