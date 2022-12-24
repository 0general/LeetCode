from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        visited = [[False]*m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    k = 1
                    q.append((i,j))
                    while q:
                        x, y = q.popleft()
                        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + d[0], y + d[1]
                            if nx < 0 or ny < 0 or nx >= n or ny >= m or not grid[nx][ny] or visited[nx][ny]:
                                continue
                            visited[nx][ny] = True
                            k += 1
                            q.append((nx, ny))
                    ans = max(ans, k)
        return ans
        