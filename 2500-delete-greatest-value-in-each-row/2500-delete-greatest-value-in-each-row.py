class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            grid[i] = sorted(grid[i])
        for j in range(n):
            x = grid[0][j]
            for i in range(1, m):
                x = max(x, grid[i][j])
            result += x
        return result