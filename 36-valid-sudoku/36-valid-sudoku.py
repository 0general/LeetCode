class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0]*10 for _ in range(9)]
        col = [[0]*10 for _ in range(9)]
        box = [[[0]*10 for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    if row[i][x]:
                        return False
                    else:
                        row[i][x] = 1
                    if col[j][x]:
                        return False
                    else:
                        col[j][x] = 1
                    if box[i//3][j//3][x]:
                        return False
                    else:
                        box[i//3][j//3][x] = 1
        return True
        