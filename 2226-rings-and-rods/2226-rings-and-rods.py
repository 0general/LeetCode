class Solution:
    def countPoints(self, rings: str) -> int:
        m = [0] * 10
        bit = {'R': 1, 'G': 2, 'B': 4}
        for i in range(0, len(rings), 2):
            c = rings[i] 
            r = ord(rings[i + 1]) - 48
            m[r] |= bit[c]
        return sum(x == 7 for x in m)