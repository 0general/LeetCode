class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        ans = 0
        for idx, num in enumerate(nums):
            if not s or nums[s[-1]] > num:
                s.append(idx)
        for i in range(len(nums) - 1, -1, -1):
            while s and nums[s[-1]] <= nums[i]:
                ans = max(ans, i - s.pop())
        return ans