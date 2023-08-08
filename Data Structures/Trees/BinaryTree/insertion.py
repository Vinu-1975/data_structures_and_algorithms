class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def insert(root,val):
    if root is None:
        root = Node(val)
        return root
    
    q=[]
    q.append(root)

    while len(q)>0:
        node = q.pop(0)

        if not node.left:
            node.left = Node(val)
            break
        else:
            q.append(node.left)

        if not node.right:
            node.right = Node(val)
            break
        else:
            q.append(node.right)

    return root

def levelOrder(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while len(q)>0:
        temp = q.pop(0)
        print(temp.val,end=" ")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

if __name__ == "__main__":
    root = None
    root = insert(root,1)
    root = insert(root,2)
    root = insert(root,3)
    root = insert(root,4)

    levelOrder(root)

