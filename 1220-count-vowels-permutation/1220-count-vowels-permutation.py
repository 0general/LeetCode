class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [1] * 5
        for _ in range(1, n):
            a, e, i, o, u = (dp[1] + dp[2] + dp[4]) % mod, (dp[0] + dp[2]) % mod, (dp[1] + dp[3]) % mod, dp[2], (dp[2] + dp[3]) % mod
            dp = [a, e, i, o, u]
        return sum(dp) % mod
            
        