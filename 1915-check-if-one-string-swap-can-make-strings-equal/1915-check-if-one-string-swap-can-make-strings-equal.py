class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        x, y, cnt = -1, -1, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if x == -1:
                    x = i
                elif y == -1:
                    y = i
                else:
                    return False
        if cnt == 0 or (cnt == 2 and s1[x] == s2[y] and s1[y] == s2[x]):
            return True
        return False