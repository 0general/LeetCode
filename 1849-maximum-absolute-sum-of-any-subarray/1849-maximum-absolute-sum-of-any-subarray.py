class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end = min_end = 0
        ans = 0
        for x in nums:
            max_end = max(x, max_end + x)
            ans = max(ans, max_end)
            min_end = min(x, min_end + x)
            ans = max(ans, -min_end)
        return ans