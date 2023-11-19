class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 배낭문제
        def rec(idx, target):
            if target == 0: 
                return True
            if idx == len(nums) or target < 0: 
                return False 
            elif self.dp[idx][target] != -1:
                return self.dp[idx][target]
            self.dp[idx][target]= rec(idx + 1, target - nums[idx]) or rec(idx + 1, target)
            return self.dp[idx][target]
        
        total = sum(nums)
        if total % 2: 
            return False 
        self.dp = [[-1]*((total//2) + 1) for _ in range(len(nums))]
        return rec(0, total//2)