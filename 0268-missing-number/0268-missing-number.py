class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = set([i for i in range(len(nums)+1)])
        for num in nums:
            S.discard(num)
        return S.pop()
        