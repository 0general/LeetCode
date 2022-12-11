from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_num = 0
        time = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_num += 1
                    continue
                elif grid[i][j] == 2:
                    q.append((0,i,j))
                visited[i][j] = True
                
        while q:
            day, i, j = q.popleft()
            time = max(time, day)
            for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                x, y = i + d[0], j + d[1]
                if x < 0 or y < 0 or x >= m or y >= n or visited[x][y]:
                    continue
                visited[x][y] = True
                q.append((day+1, x, y))
                fresh_num -= 1
        if fresh_num > 0:
            return -1
        return time
                     
        