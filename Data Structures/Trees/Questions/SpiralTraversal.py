class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def spiralTraversal(root):

    if root is None:
        return
    
    s1 = []
    s2 = []

    s1.append(root)

    while s1 or s2:
        while s1:
            temp = s1.pop()
            print(temp.val,end = " ")

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while s2:
            temp = s2.pop()
            print(temp.val,end = " ")

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
        

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.left = Node(5)
    root.left.right = Node(6)
    root.left.left = Node(7)

    spiralTraversal(root)
