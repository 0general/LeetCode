import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = []
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        heapq.heappush(h, (grid[0][0], 0, 0))
        visited[0][0] = True
        
        while h:
            s, x, y = heapq.heappop(h)
            if x == m - 1 and y == n - 1:
                return s
            for xx, yy in [(1,0), (0,1)]:
                nx, ny = x + xx, y + yy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(h, (s + grid[nx][ny], nx, ny))           
        
        