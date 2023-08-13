# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.dic = defaultdict(bool)
        self.dfs(root, 0)
        

    def find(self, target: int) -> bool:
        return self.dic[target]
    
    
    def dfs(self, root: Optional[TreeNode], num):
        if root == None: return
        root.val = num
        self.dic[num] = True
        if root.left != None:
            self.dfs(root.left, 2*num + 1)
        if root.right != None:
            self.dfs(root.right, 2*num + 2)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)