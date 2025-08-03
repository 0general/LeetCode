from copy import deepcopy

class Solution:
    def countPyramids(self, grid: list[list[int]]) -> int:
        # dp[i][j] : 이 정점이 꼭대기인 피라미드의 최대 높이
        def count(dp: list[list[int]]) -> int:
            ans = 0
            m, n = len(dp), len(dp[0])
            for i in range(m - 2, -1, -1):  # 마지막줄은 피라미드 불가
                for j in range(1, n - 1):   # 양쪽 끝은 피라미드 불가
                    if dp[i][j]:
                        dp[i][j] = min(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]) + 1
                        ans += dp[i][j] - 1  # 높이 2 이상만 유효
            return ans
        return count(deepcopy(grid)) + count(deepcopy(grid[::-1]))