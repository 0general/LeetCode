class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        mx = 1
        last = None
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and last != 1) or (diff < 0 and last != -1):
                mx += 1
                last = 1 if diff > 0 else -1
        return mx