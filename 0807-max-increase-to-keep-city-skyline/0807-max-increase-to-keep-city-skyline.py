class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        li, lj = [0] * n, [0] * n
        ans = 0
        for i in range(n):
            for j in range(n):
                li[i] = max(li[i], grid[i][j])
                lj[j] = max(lj[j], grid[i][j])
        for i in range(n):
            for j in range(n):
                mx = min(li[i], lj[j])
                ans += mx - grid[i][j]
        return ans