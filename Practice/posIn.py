class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(postOrder,inOrder,l,r,postIndex):
    if l>r:
        return None
    tNode = Node(postOrder[postIndex[0]])
    postIndex[0]-=1

    if l == r:
        return tNode
    
    inIndex = inOrder.index(tNode.val)

    tNode.right = buildTree(postOrder,inOrder,inIndex+1,r,postIndex)
    tNode.left = buildTree(postOrder,inOrder,l,inIndex-1,postIndex)
    return tNode

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)


if __name__ == "__main__":
    inOrder = ["D", "B", "E", "A", "F", "C"]
    postOrder = ["D", "E", "B", "F", "C", "A"]

    postIndex = [len(inOrder) - 1]
    root = buildTree(postOrder,inOrder,0,len(inOrder)-1,postIndex)

    printInOrder(root)