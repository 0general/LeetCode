from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # https://leetcode.com/problems/sliding-window-median/discuss/806480/Python-real-O(nlogk)-solution-easy-to-understand 참고
        sl = SortedList()
        
        res = []
        for i in range(len(nums)):
            sl.add(nums[i])
            if len(sl) > k:
                sl.remove(nums[i-k])
            if len(sl) == k:
                median = sl[k//2] if k%2 == 1 else (sl[k//2-1] + sl[k//2]) / 2
                res.append(median)
        return res
        