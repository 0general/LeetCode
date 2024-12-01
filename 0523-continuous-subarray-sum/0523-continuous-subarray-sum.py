class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rest = {0: -1}
        x = 0
        for i, num in enumerate(nums):
            x += num
            rem = x % k
            if rem in rest:
                if (i - rest[rem] > 1): 
                    return True
            else:
                rest[rem] = i
        return False