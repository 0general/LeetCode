from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        num_map = defaultdict(int)
        l, n = 0, len(nums)
        for r in range(n):
            num_map[nums[r]] = num_map[nums[r]] + 1
            while num_map[nums[r]] > k:
                num_map[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result