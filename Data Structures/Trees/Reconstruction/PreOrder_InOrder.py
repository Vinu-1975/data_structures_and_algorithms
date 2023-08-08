class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inOrder, preOrder, l, r):
    if l > r:
        return None

    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if l == r:  # if the nodes has no child
        return tNode

    inIndex = search(inOrder, l, r, tNode.val)

    tNode.left = buildTree(inOrder, preOrder, l, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, r)

    return tNode


def search(inOrder, l, r, val):
    for i in range(l, r + 1):
        if inOrder[i] == val:
            return i


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)
    


if __name__ == "__main__":
    inOrder = ["D", "B", "E", "A", "F", "C"]
    preOrder = ["A", "B", "D", "E", "C", "F"]

    buildTree.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

    printInOrder(root)


