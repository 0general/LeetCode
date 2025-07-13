class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for j in range(n):
            col = j
            for row in range(m):
                dir = grid[row][col]
                n_col = col + dir
                if not (0 <= n_col < n and grid[row][n_col] == dir):
                    col = -1
                    break
                col = n_col
            ans.append(col)
        return ans