# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth, height = defaultdict(int), defaultdict(int)

        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            height[node.val] = max(dfs(node.left, d + 1), dfs(node.right, d + 1)) + 1
            return height[node.val]

        dfs(root, 0)

        dp = defaultdict(list)
        for i, d in depth.items():
            dp[d].append((height[i], i))
            dp[d].sort(reverse=True)
            if len(dp[d]) > 2: # Timelimit
                dp[d].pop()

        ans = []
        for query in queries:
            d = depth[query]
            if len(dp[d]) == 1:
                ans.append(d - 1)
            elif dp[d][0][1] == query:
                ans.append(dp[d][1][0] + d)
            else:
                ans.append(dp[d][0][0] + d)
        return ans