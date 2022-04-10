class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        length = 0
        for i in range(n):
            matrix[i] = list(map(int, matrix[i]))
            for j in range(m):
                if matrix[i][j] == 0:
                    continue
                if i != 0 and j != 0:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + 1
                length = max(length,matrix[i][j])
        
        return length**2