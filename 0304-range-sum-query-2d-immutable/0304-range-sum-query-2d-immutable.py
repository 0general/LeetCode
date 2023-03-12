class NumMatrix:
    dp = []
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num1 = self.dp[i-1][j] if i > 0 else 0
                num2 = self.dp[i][j-1] if j > 0 else 0
                num3 = self.dp[i-1][j-1] if i > 0 and j > 0 else 0
                self.dp[i][j] = matrix[i][j] + num1 + num2 - num3
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        num3 = self.dp[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        num1 = self.dp[row2][col1-1] if col1 > 0 else 0
        num2 = self.dp[row1-1][col2] if row1 > 0 else 0
        return self.dp[row2][col2] - num1 - num2 + num3
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)