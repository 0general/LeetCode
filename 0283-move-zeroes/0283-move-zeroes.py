class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeronum = nums.count(0)
        idx = 0
        length = len(nums)
        for i, x in enumerate(nums):
            if x != 0:
                nums[idx] = x
                idx += 1
            if i >= length - zeronum:
                nums[i] = 0
        