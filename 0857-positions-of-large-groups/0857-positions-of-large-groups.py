class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        si = 0
        li = 0
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c != s[i-1]:
                if li - si >= 2:
                    result.append([si, li])
                si = i
            li = i
        if li - si >= 2:
            result.append([si, li])
        return result
