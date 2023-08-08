# check whether a binary tree is balanced or not

# A balanced binary tree, also referred to as a height-balanced
# binary tree, is defined as a binary tree in which the height of
# the left and right subtree of any node differ by not more than 1.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isHeightBalanced(root, isBalanced=True):
    if root is None or not isBalanced:
        return 0, isBalanced
    else:
        lh, isBalanced = isHeightBalanced(root.left, isBalanced)
        rh, isBalanced = isHeightBalanced(root.left, isBalanced)

        # tree is unbalanced if the absolute difference between the height of
        # its left and right subtree is more than 1
        if abs(lh - rh) > 1:
            isBalanced = False
        
        return 1 + max(lh,rh), isBalanced

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
