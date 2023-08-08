class Nodes:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

if __name__ == "__main__":
    root = Nodes(1)
    root.left = Nodes(2)
    root.right = Nodes(3)
    root.left.left = Nodes(4)
    root.left.right = Nodes(5)

    print(count_nodes(root))
