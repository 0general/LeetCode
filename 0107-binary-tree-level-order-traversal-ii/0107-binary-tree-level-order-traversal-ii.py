# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans= []
        q = deque()
        if root:
            q.append((root, 0))
            ans.append([])
        while q:
            x, d = q.popleft()
            if d < len(ans):
                ans[d].append(x.val)
            else:
                ans.append([x.val])
            if x.left:
                q.append((x.left, d + 1))
            if x.right:
                q.append((x.right, d + 1))
        ans.reverse()
        return ans
        