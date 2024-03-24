class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                s, e = 0, n
                while (s < e):
                    mid=(s + e) // 2
                    
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        s = mid + 1
                    else:
                        e = mid   
        return False