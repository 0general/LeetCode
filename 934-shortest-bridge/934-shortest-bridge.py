import heapq
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    heapq.heappush(q, (0,i,j))
                    break
            else:
                continue
            break
            
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            num,i,j = heapq.heappop(q)
            for d in dir:
                x, y = i+d[0],j+d[1]
                if x < 0 or y < 0 or x >= n or y >= n or visited[x][y]:
                    continue
                    
                visited[x][y] = True
                if grid[x][y] == 0:
                    heapq.heappush(q,(num+1,x,y))
                else:
                    if num == 0:
                        heapq.heappush(q,(0,x,y))
                    else:
                        return num
                