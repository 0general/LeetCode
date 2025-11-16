class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # https://leetcode.com/problems/maximize-distance-to-closest-person/solutions/137912/javacpython-one-pass-easy-understood-by-1va44/
        mx, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                mx = max(mx, i if last < 0 else (i - last) // 2)
                last = i
        return max(mx, n - last - 1)