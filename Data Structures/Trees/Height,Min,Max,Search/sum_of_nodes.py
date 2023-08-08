class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def printSum(root):
    if root is None:
        return 0
    else:
        leftSum = printSum(root.left)
        rightSum = printSum(root.right)
        return root.val + leftSum + rightSum

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(printSum(root))