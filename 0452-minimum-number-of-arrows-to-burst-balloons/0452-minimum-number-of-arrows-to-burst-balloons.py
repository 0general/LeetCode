class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))
        result = 1
        xs, xe = points[0][0], points[0][1]
        for s, e in points[1:]:
            if s > xe:
                result += 1
                xs, xe = s, e
            else:
                xs = s
                xe = min(e, xe)
        return result