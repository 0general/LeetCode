class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = sorted(set(nums), reverse=True)
        return x[0] if len(x) < 3 else x[2]