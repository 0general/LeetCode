class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bleft():
            s, e = 0, len(nums) - 1
            result = -1
            while s <= e:
                mid = (s  +  e)//2
                if nums[mid] == target:
                    result = mid
                    e = mid - 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return result
        def bright():
            s, e = 0, len(nums) - 1
            result = -1
            while s <= e:
                mid = (s  +  e)//2
                if nums[mid] == target:
                    result = mid
                    s = mid + 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return result
        return [bleft(), bright()]
                
        