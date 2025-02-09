# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((0, root))
        leftmost = [None, None]
        while q:
            depth, node = q.popleft()
            if leftmost[0] is None or leftmost[0] < depth:
                leftmost[0] = depth
                leftmost[1] = node.val
            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))
        return leftmost[1]
