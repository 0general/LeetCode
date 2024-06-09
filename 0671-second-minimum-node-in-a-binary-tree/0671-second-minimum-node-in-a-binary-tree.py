# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = [-1, -1]
        tree = []
        if root:
            ans[0] = root.val
            if root.left:
                tree.append(root.left)
            if root.right:
                tree.append(root.right)
        while tree:
            node = tree.pop()
            if node.val < ans[0]:
                ans[1] = ans[0]
                ans[0] = node.val
            elif ans[0] < node.val and (ans[1] < 0 or node.val < ans[1]):
                ans[1] = node.val
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
        return ans[1]
        