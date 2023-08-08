from msvcrt import kbhit


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertLvlWise(self,arr,i,n):
        self.root = self._insertLvlWise(arr,i,n)

    def _insertLvlWise(self,arr,i,n):
        tree = None
        if i < n:
            tree = Node(arr[i])
            tree.left = self._insertLvlWise(arr,2*i+1,n)
            tree.right = self._insertLvlWise(arr,2*i+2,n)
        return tree
    
    def lvlOrderTraversal(self):
        if self.root is None:
            return
        q = [self.root]
        while q:
            temp = q.pop(0)
            print(temp.val,end = " ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    n = len(arr)
    tree = BinaryTree()
    tree.insertLvlWise(arr,0,n)
    tree.lvlOrderTraversal()