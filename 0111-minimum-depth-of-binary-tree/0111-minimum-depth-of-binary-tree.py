# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minimum = 10**5 + 1
        q = deque()
        if root:
            q.append((root, 1))
        else:
            minimum = 0
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                minimum = depth
                break
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return minimum
        