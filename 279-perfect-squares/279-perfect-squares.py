from collections import deque

class Solution:
    # 이거 DP다. 
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        q = deque()
        arr = []
        i = 1
        while i**2 <= n:
            a = i**2
            arr.append(a)
            q.append(a)
            dp[a] = 1
            i += 1
        while q and dp[n] == 0:
            now = q.popleft()
            for j in arr:
                next = now + j
                if next > n:
                    break
                if dp[next] == 0:
                    dp[next] = dp[now] + 1
                    q.append(next)
        return dp[n]
        
        