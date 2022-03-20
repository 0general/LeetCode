class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        k = len(nums) # nums[0]보다 작은 수 중에 가장 작은 수의 위치
        if k == 0:
            return -1
        if nums[0] > nums[-1]:
            s, e = 1, len(nums)-1
            ans = len(nums) - 1
            while s <= e:
                mid = (s+e)//2
                if nums[mid] > nums[0]:
                    s = mid + 1
                else:
                    ans = mid
                    e = mid - 1
            k = ans
        s, e = 0, len(nums)-1
        if nums[0] < target:
            e = k-1
        elif nums[0] > target:
            s = k
        while s <= e:
            mid = (s+e)//2
            if nums[mid] > target:
                e = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                s = mid + 1
        return -1
        