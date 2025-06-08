class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # 참고 : https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/294265/python-in-depth-explanation-dp-for-beginners/
        n = len(values)
        dp = [[0] * n for i in range(n)]
        for l in range(2, n):
            for left in range(0, n - l):
                right = left + l
                dp[left][right] = float("Inf")
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + values[left] * values[right] * values[k])
        return dp[0][-1]