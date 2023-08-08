class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inOrder, postOrder, l, r,postIndex):
    if l > r:
        return None

    tNode = Node(postOrder[postIndex[0]])
    postIndex[0] -= 1

    if l == r:  # if the nodes has no child
        return tNode

    inIndex = search(inOrder, l, r, tNode.val)

    tNode.right = buildTree(inOrder, postOrder, inIndex + 1, r,postIndex)
    tNode.left = buildTree(inOrder, postOrder, l, inIndex - 1,postIndex)

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
    postOrder = ["D", "E", "B", "F", "C", "A"]

    postIndex = [len(inOrder) - 1]
    root = buildTree(inOrder, postOrder, 0, len(inOrder) - 1,postIndex)

    printInOrder(root)
