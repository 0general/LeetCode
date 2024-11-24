class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        before_num = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4]}
        dp = [[0] * 10 for _ in range(n)] # dp[i][j] : i번째 이동으로 j번호에 서 있을 수 있는 방법
        dp[0] = [1] * 10
        for i in range(1, n):
            for j in range(10):
                for x in before_num[j]:
                    dp[i][j] += dp[i-1][x]
                dp[i][j] %= mod
        return sum(dp[n-1]) % mod