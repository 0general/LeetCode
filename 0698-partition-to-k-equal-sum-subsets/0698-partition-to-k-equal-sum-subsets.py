class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        '''
        https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/2918330/Faster-than-91-Easy-python-solution-with-comments
        ''' 
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        buckets = [0] * k
        
        nums.sort(reverse=True)

        return self.dfs(0, nums, buckets, target)

    def dfs(self, idx, nums, buckets, target):
        for i in range(len(buckets)):
            if buckets[i] + nums[idx] > target:
                continue
            buckets[i] += nums[idx]
            if idx == len(nums) - 1:
                return True
            if self.dfs(idx + 1, nums, buckets, target):
                return True
            
            buckets[i] -= nums[idx]
            
            if buckets[i] == 0:
                return False      
        return False