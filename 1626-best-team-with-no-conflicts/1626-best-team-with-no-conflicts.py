class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ls = sorted(zip(scores, ages))
        dp = [0]*1001 # dp[age]
        ans = 0
        for score, age in ls:
            dp[age] = max(dp[:age+1]) + score
            ans = max(ans, dp[age])
        return ans