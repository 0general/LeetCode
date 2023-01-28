# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        # dp[n] = n개로 만들 수 있는 fbt 
        dp = [[] for _ in range(n+1)]
        dp[1].append(TreeNode(0))
        for num in range(3, n+1, 2):
            for i in range(1, num, 2): # 왼쪽 자식 트리 => 풀 바이너리라 num이 최대가 될 수 없음
                j = num - 1 - i # 오른쪽 자식 트리
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[num].append(root)
        return dp[n]
                
                
        