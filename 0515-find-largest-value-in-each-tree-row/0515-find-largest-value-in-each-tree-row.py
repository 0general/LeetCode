# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        if root:
            q.append((0, root))
        while q:
            index, node = q.popleft()
            if len(result) <= index:
                result.append(node.val)
            else:
                result[index] = max(result[index], node.val)
            if node.left:
                q.append((index + 1, node.left))
            if node.right:
                q.append((index + 1, node.right))
        return result