class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def isCheckComplete(root):
    if root is None:
        return True
    q=[]
    q.append(root)
    flag = False

    while len(q)>0:
        temp =q.pop(0)

        if temp.left:
            if flag == True:
                return False
            q.append(temp.left)
        else:
            flag = True
        if temp.right:
            if flag == True:
                return False
            q.append(temp.right)
        else:
            flag = True
    return True
        

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(isCheckComplete(root))