class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_set = set()
        beg, end, sum_num = 0, 0, 0
        ans = 0
        while end < len(nums):
            if nums[end] not in num_set:
                sum_num += nums[end]
                num_set.add(nums[end])
                end += 1
                ans = max(ans, sum_num)
            else:
                sum_num -= nums[beg]
                num_set.remove(nums[beg])
                beg += 1
        
        return ans 