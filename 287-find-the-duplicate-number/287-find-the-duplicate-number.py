class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        number = [0]*(int(1e5)+1)
        for num in nums:
            if not number[num]:
                number[num] = 1
            else:
                return num