# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dfs = deque()
        if root:
            dfs.append((1, root))
        x = 0
        while dfs:
            num, node = dfs.popleft()
            if num != (x + 1):
                return False
            if node.left:
                dfs.append((num*2, node.left))
                if node.right:
                    dfs.append(((num*2 + 1), node.right))
            else:
                if node.right:
                    return False
            x += 1
        return True
            