class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = word1의 i번째 문자와 word2의 j번째 문자까지 맞추기 위해 필요한 최소 변환 횟수
        # dp[i][j] -> dp[i][j+1] : insert -> + 1
        # dp[i][j] -> dp[i+1][j+1] : + int(word1[i+1] != word2[j+1])
        # dp[i][j] -> dp[i+1][j] : delete -> + 1
        n = len(word1)
        m = len(word2)
        if n==0 or m==0:
            return max(n,m)
        dp = [[1001]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = j + int(word1[i] != word2[j])
                if j == 0:
                    dp[i][j] = i + int(word1[i] != word2[j])
                if i >= 1 and j >= 1:
                    dp[i][j] = dp[i-1][j-1] + int(word1[i] != word2[j])
                if i >= 1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                if j >= 1:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                    
        return dp[n-1][m-1]