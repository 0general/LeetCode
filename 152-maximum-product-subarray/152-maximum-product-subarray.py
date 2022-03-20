class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = [nums[0],nums[0]]
        mx = nums[0]
        for i in range(1,len(nums)):
            a, b = x[0]*nums[i], x[1]*nums[i]
            x = [max(nums[i],a,b), min(nums[i],a,b)]
            mx = max(mx,a,b,nums[i])
            
        return mx
            
        