# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])
        direction = True

        while q:
            level = len(q)
            current = [0] * level

            for i in range(level):
                node = q.popleft()
                index = i if direction else level - 1 - i
                current[index] = node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current)
            direction = not direction
        return result
