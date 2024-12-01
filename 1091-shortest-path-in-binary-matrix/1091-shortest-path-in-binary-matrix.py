from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n) ]
        d = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        q = deque()
        
        if (grid[0][0] != 0 or grid[n-1][n-1] != 0):
            return -1
        visited[0][0] = True
        q.append((0,0,1))
        while q:
            x, y, num = q.popleft()
            if x == n-1 and y == n-1:
                return num
            for i, j in d:
                nx, ny = x + i, y + j
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, num + 1))
        return -1