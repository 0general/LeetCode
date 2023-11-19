class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        diff = abs(startPos - endPos)
        if diff > k or (k - diff) % 2:
            return 0
        # k 번 중에 diff + (k - diff) // 2 만큼을 같은 방향으로 이동해야함
        num = (diff + k) // 2
        
        def pascal_triangle(n, r):
            if r == 0:
                return 1
        dp = [[1 for j_ in range(i+1)] for i in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(1, i):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
        return dp[k][num]