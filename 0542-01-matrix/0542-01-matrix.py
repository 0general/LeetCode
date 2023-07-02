from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        lx, ly = len(mat), len(mat[0])
        visited = [[-1 for _ in range(ly)] for _ in range(lx)]
        q = deque()
        for i in range(lx):
            for j in range(ly):
                if mat[i][j] == 0:
                    visited[i][j] = 0
                    q.append((i,j,0))
        while q:
            x, y, num = q.popleft()
            for ix, jy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = x+ix, y+jy
                if 0 <= nx < lx and 0 <= ny < ly and visited[nx][ny] < 0:
                    visited[nx][ny] = num + 1
                    q.append((nx, ny, num + 1))
                
        return visited
                    
        
        