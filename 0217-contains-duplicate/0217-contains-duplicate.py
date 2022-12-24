class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ls_l = len(nums)
        s_l = len(set(nums))
        if ls_l > s_l:
            return True
        return False
        