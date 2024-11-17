class Solution:
    # 참고 : https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/discuss/5623743/Python-DP-with-explanation
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        
        dp = [[0] * 51 for _ in range(n)]
        
        for j in range(nums[0] + 1):
            dp[0][j] = 1
            
        for i in range(1, n):
            for j in range(nums[i] + 1):
                for p in range(j + 1):
                    arr2_j = nums[i] - j
                    arr2_p = nums[i-1] - p
                    if arr2_j <= arr2_p:
                        dp[i][j] += dp[i-1][p]
        return sum(dp[-1]) % mod
                    