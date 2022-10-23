class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (-x[1],x[0]))
        ans = 0
        s, e = 0, 0
        for i in range(len(intervals)):
            if s <= intervals[i][0] and e >= intervals[i][1]:
                continue
            s = intervals[i][0]
            e = intervals[i][1]
            ans += 1
        return ans