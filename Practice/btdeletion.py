class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def deletion(root,key):
    if root is None:
        return None
    if not root.left and not root.right:
        if root.val == key:
            return None
        else:
            return root
        
    key_node = None
    temp = None
    last = None
    q=[]
    q.append(root)
    while len(q)>0:
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            last = temp
            q.append(temp.left)
        if temp.right:
            last = temp
            q.append(temp.right)
    if key_node is not None:
        key_node.data = temp.data
        if last.right == temp:
            last.right = None
        else:
            last .left = None

    return root

if __name__ == '__main__':
    root = Node(9)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.right = Node(8)

    print("Inorder traversal before deletion : ", end="")
    inorder(root)

    key = 7
    root = deletion(root, key)
    print()
    print("Inorder traversal after deletion : ", end="")
    inorder(root)