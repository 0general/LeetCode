from itertools import accumulate
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # 참고 : https://leetcode.com/problems/stone-game-vii/discuss/970268/C%2B%2BPython-O(n-*-n)
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        p_sum = [0] + list(accumulate(stones)) # 누적합
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(p_sum[j + 1] - p_sum[i + 1] - dp[i + 1][j], 
                               p_sum[j] - p_sum[i] - dp[i][j - 1]);
        return dp[0][n - 1]