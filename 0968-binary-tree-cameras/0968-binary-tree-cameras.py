# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cameras = 0
        
    def dfs(self, root):
        if root is None:
            return 1
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if left == -1 or right == -1:
            self.cameras += 1 # root 에 카메라를 둬야 함
            return 0
        if left == 0 or right == 0:
            return 1 # 자식에 camera가 있어서 root 는 둘 필요없음
        if left == 1 and right == 1:
            return -1 # root 에 둬야 함
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if (self.dfs(root) == -1): # root에 둬야 하는지 체크
            self.cameras += 1
        return self.cameras