class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        reliability = [n-1] * n
        for a, b in trust:
            reliability[b-1] -= 1
            reliability[a-1] += 1
        for i, r in enumerate(reliability):
            if r == 0: return i+1
        return -1
        