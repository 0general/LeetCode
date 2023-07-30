class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        triangle = [[-1]*length for _ in range(length)]
        triangle[0] = nums
        for i in range(1, length):
            for j in range(length - i):
                triangle[i][j] = (triangle[i-1][j] + triangle[i-1][j+1]) % 10
        return triangle[length-1][0]
        