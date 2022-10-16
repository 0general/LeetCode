class Solution:
    
    ans = 0
    def making(self,visited, idx, n):
        if idx >= n:
            self.ans += 1
            return
        for i in range(n):
            if not visited[idx][i]:
                visited[idx][i] = True
                stack = []
                for num in range(1,n-idx):
                    for d in [(1,0),(1,-1),(1,1)]:
                        x, y = idx+d[0]*num, i+d[1]*num
                        if x < 0 or y < 0 or x >= n or y >= n or visited[x][y]:
                            continue
                        stack.append((x,y))
                        visited[x][y] = True
                self.making(visited,idx+1,n)
                while stack:
                    x, y = stack.pop()
                    visited[x][y] = False
                visited[idx][i] = False
                
    
    def totalNQueens(self, n: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(n)]
        self.making(visited,0,n)
        return self.ans
        
        
        
        