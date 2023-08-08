class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(N):
    if N is None:
        return 0
    else:
        lh = height(N.left)
        rh = height(N.right)

        # if lh > rh:
        #     return lh+1
        # else:
        #     return rh+1

        return 1 + max(lh, rh)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root.left.left.left=Node(8)

    print(height(root))
