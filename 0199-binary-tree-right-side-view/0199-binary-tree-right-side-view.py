# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        if root:
            q.append((0, root))
        while q:
            depth, root = q.popleft()
            if len(result) == depth:
                result.append(root.val)
            else:
                result[depth] = root.val
            if root.left:
                q.append((depth+1, root.left))
            if root.right:
                q.append((depth+1, root.right))
        return result
        
        