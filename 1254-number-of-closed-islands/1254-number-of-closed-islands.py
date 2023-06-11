class Solution:
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        lx, ly = len(grid), len(grid[0])
        def dfs(i,j,newval):
            if grid[i][j]==0:
                grid[i][j]=2
                if i < lx-1 : dfs(i+1,j,newval)
                if i > 0 : dfs(i-1,j,newval)
                if j < ly-1 : dfs(i,j+1,newval)
                if j > 0 : dfs(i,j-1,newval)
        for i in range(lx):
            for j in range(ly):
                if i == 0 or j == 0 or i == lx - 1 or j == ly - 1:
                    if grid[i][j]==0:
                        dfs(i, j, 2)
        res=0
        for i in range(1, lx - 1):
            for j in range(1, ly - 1):
                if grid[i][j]==0:
                    res += 1
                    dfs(i, j, 2)
        return res
                                
                        
        
        