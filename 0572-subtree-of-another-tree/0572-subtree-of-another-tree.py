# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(croot, target):
            if (croot is None and target is not None) or (croot is not None and target is None):
                return False
            elif (croot is None and target is None):
                return True
            
            return ((croot.val == target.val) and check(croot.left, target.left) and check(croot.right, target.right))
        
        if check(root, subRoot):
            return True
        if root is None:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)