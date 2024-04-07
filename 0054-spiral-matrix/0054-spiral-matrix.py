class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        visited = [[False]* m for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        out = []
        
        i, j, d = 0, 0, 0
        visited[i][j] = True
        out.append(matrix[i][j])
        while True:
            ni, nj = i + direction[d][0], j + direction[d][1]
            if ni >= n or nj >= m or visited[ni][nj]:
                d = d + 1 if d < 3 else 0
                ni, nj = i + direction[d][0], j + direction[d][1]
                if ni >= n or nj >= m or visited[ni][nj]:
                    return out
            visited[ni][nj] = True
            out.append(matrix[ni][nj])
            i, j = ni, nj