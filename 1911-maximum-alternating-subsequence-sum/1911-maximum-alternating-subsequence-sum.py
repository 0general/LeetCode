class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[0,0,0,0] for _ in range(length)] # dp[i] = [+로 포함, -로 포함, +차례 불포함, - 차례 불포함]
        dp[0][0] = nums[0]
        for i in range(1,length):
            dp[i][0] = max(nums[i], dp[i-1][2]+nums[i],dp[i-1][1] + nums[i])
            dp[i][1] = max(dp[i-1][0] - nums[i], dp[i-1][3]-nums[i])
            dp[i][2] = max(dp[i-1][1], dp[i-1][2], 0)
            dp[i][3] = max(dp[i-1][0], dp[i-1][3], 0)
        return max(dp[length-1])