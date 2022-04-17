# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
    
        self.arr = inOrder(root)
        self.N = len(self.arr)
        self.pointer = -1
        

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]
        

    def hasNext(self) -> bool:
        return self.pointer < self.N-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()