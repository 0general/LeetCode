class Solution:
    def dfs(self, board, word,visited, stack):
        if len(stack) == len(word):
            return True
        ans = False
        i,j = stack[-1]
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            x,y = i+d[0], j+d[1]
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or visited[x][y]:
                continue
            if board[x][y] == word[len(stack)]:
                visited[x][y] = True
                stack.append((x,y))
                ans = self.dfs(board,word,visited,stack)
                if ans:
                    return True
                visited[x][y] = False
                stack.pop()
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    stack = []
                    visited[i][j] = True
                    stack.append((i,j))
                    if self.dfs(board,word,visited,stack):
                        return True
        return False
        