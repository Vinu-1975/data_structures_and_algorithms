



class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_TREE:

    def getHeight(self,root):
        if root is None:
            return 0
        return root.height

    def getBalanceFactor(self,root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self,root,val):
        if root is None:
            return Node(val)
        
        if root.val < val:
            root.right = self.insert(root.right,val)
        else:
            root.left = self.insert(root.left,val)
        
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalanceFactor(root)

        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def leftRotate(self,z):
        y = z.right
        t3 = y.left

        y.left = z
        z.right = t3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y
    
    def rightRotate(self,z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y
    
    def getMinValueNode(self,root):
        if root.left is None and root.right is None:
            return root
        return self.getMinValueNode(root.left)
    
    def delete(self,root,val):
        if root is None:
            return root
        
        if val < root.val:
            root.left = self.delete(root.left,val)
        elif val > root.val:
            root.right = self.delete(root.right,val)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)

        if root is None:
            return root
        
        root.height = self.getHeight(root)

        balance = self.getBalanceFactor(root)

        if balance > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotate(root)
        
        if balance < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotate(root)
        
        if balance > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate((root))
        
    def preOrder(self,root):
        if root:
            print(root.val,end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)
        
if __name__ == "__main__":
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    avl = AVL_TREE()
    for i in nums:
        root = avl.insert(root,i)

    # root = avl.insert(root, 10)
    # root = avl.insert(root, 20)
    # root = avl.insert(root, 30)
    # root = avl.insert(root, 40)
    # root = avl.insert(root, 50)
    # root = avl.insert(root, 25)

    avl.preOrder(root)

    root = avl.delete(root,10)
    print()

    avl.preOrder(root)
    


    
    
    