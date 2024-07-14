class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        length = 0
        for num in nums:
            if num == 0:
                result = max(length, result)
                length = 0
            else:
                length += 1
        return max(length, result)
        