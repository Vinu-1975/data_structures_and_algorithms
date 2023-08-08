class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(level,ino):
    if ino:
        for i in range(0,len(level)):
            if level[i] in ino:
                node = Node(level[i])

                in_index = ino.index(level[i])
                break
        node.left = buildTree(level,ino[0:in_index])
        node.right = buildTree(level,ino[in_index + 1:len(ino)])

        return node
    else:
        return None

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)



levelOrder = ["A","B","C","D","E","F"]
inOrder = ["D","B","E","A","F","C"]

root = buildTree(levelOrder,inOrder)

printInOrder(root)