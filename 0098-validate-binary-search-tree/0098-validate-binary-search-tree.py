# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], ls = []) -> bool:
        ls = []
        def isValid(root):
            nonlocal ls
            if not root:
                return True
            if root.left and ((root.val <= root.left.val) or not isValid(root.left)):
                return False
            if ls and (ls[-1] >= root.val):
                return False
            ls.append(root.val)
            if root.right and ((root.val >= root.right.val) or not isValid(root.right)):
                return False
            return True
        return isValid(root)