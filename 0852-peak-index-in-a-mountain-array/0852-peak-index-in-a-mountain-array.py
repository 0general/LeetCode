class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s, e = 0, len(arr)-1
        ans = 0
        while s <= e:
            mid = (s+e)//2
            if arr[mid] >= arr[s] and arr[mid] >= arr[e]:
                ans = mid
            if mid > 0 and arr[mid-1] >= arr[mid]:
                e = mid - 1
                continue
            if mid < len(arr)-1 and arr[mid+1] >= arr[mid]:
                s = mid + 1
                continue
            break
        return ans