class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preOrder,inOrder,l,r):
    if l>r:
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if l == r:
        return tNode
    
    inIndex = inOrder.index(tNode.val)

    tNode.left=buildTree(preOrder,inOrder,l,inIndex-1)
    tNode.right =buildTree(preOrder,inOrder,inIndex+1,r)
    return tNode

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val,end=" ")
        printInOrder(root.right)

if __name__ == "__main__":
    inOrder = ["D", "B", "E", "A", "F", "C"]
    preOrder = ["A", "B", "D", "E", "C", "F"]

    buildTree.preIndex = 0
    root = buildTree(preOrder,inOrder,0,len(inOrder)-1)

    printInOrder(root)