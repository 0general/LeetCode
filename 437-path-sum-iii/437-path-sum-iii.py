# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = 0
    
    def dfs(self, node:Optional[TreeNode], Sum, targetSum):
        
        if node is None:
            return
        Sum += node.val
        if Sum == targetSum:
            self.ans += 1
        self.dfs(node.left,Sum,targetSum)
        self.dfs(node.right,Sum,targetSum)

    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    
        self.dfs(root, 0, targetSum)
        if root is not None:
            self.pathSum(root.right,targetSum)
            self.pathSum(root.left,targetSum)
                
        return self.ans
            