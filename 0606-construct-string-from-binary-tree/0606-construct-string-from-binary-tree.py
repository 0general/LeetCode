# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode], string = "", depth = 0) -> str:
        string += str(root.val)
        if root.left:
            string = self.tree2str(root.left, string + "(", depth + 1) + ")"
        elif root.right:
            string += "()"
        if root.right:
            string = self.tree2str(root.right, string + "(", depth + 1) + ")"
        return string
        
        