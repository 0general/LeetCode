# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        root.left = self.trimBST(root.left,low, high)
        root.right = self.trimBST(root.right,low,high)
        
        if root.val < low or root.val > high: # 내가 충족이 안 될 때, left가 Not None이면 right는 당연히 안 됨.
            return root.left if root.left else root.right
        
        return root
        
        