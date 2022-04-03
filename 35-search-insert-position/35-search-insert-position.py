class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        answer = len(nums)
        while s <= e:
            mid = (s+e)//2
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                answer = mid
                e = mid - 1
            
        return answer
        