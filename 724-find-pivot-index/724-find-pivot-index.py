class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(nums)
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum -= nums[i]
            
            leftsum += nums[i-1] if i != 0 else 0
            
            if leftsum == rightsum:
                return i
        return -1
            
        