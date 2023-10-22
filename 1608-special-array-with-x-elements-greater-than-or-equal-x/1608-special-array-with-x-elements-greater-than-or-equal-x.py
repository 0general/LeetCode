class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        def bs(i):
            result = -1
            s, e = 0, length - 1
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] >= i:
                    e = mid - 1
                    result = mid
                else:
                    s = mid + 1
            return result
        
        for i in range(nums[-1] + 1):
            idx = bs(i)
            if idx != -1 and i == length - idx:
                return i
        return -1