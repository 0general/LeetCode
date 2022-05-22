class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n
        temp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                x, y = i,j+k
                x += y//n
                y = y%n
                x %= m
                temp[x][y] = grid[i][j]
    
        return temp