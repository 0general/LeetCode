class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = dict()
        
        def bf(idx, total):
            nonlocal ans
            if (idx, total) not in ans:
                if idx >= len(nums):
                    ans[(idx, total)] = int(total == target)
                else:
                    ans[(idx, total)] = bf(idx+1, total+nums[idx]) + bf(idx+1, total-nums[idx])
            return ans[(idx, total)]
        
        return bf(0, 0)
        