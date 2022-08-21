# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            if root.left:
                next = root.left
                while next.right:
                    next = next.right
                next.right = root.right
                root.right = root.left
                root.left = None
            if root.right:
                self.flatten(root.right)
            
        