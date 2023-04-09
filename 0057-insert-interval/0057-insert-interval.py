class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if newInterval[0] in range(intervals[i][0],intervals[i][1]+1) \
            or newInterval[1] in range(intervals[i][0],intervals[i][1]+1) \
            or (newInterval[1] >= intervals[i][1] and newInterval[0] <= intervals[i][0]):
                if intervals[i][0] < newInterval[0]:
                    newInterval[0] = intervals[i][0]
                if intervals[i][1] > newInterval[1]:
                    newInterval[1] = intervals[i][1]
                intervals.pop(i)
                if i <= 0:
                    i = 0
                else:
                    i -= 1
            else:
                i += 1
        intervals.append([newInterval[0],newInterval[1]])
        intervals.sort()
        return intervals