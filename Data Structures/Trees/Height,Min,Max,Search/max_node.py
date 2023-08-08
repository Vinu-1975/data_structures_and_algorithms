class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def treeMax(root):
    if root is None:
        return float("-inf")
    else:
        leftMax = treeMax(root.left)
        rightMax = treeMax(root.right)
        return max(root.val, leftMax, rightMax)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(treeMax(root))
