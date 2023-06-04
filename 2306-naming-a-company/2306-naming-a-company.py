class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        result = 0
        ideasSet = {idea for idea in ideas}
        match = [[0 for _ in range(26)] for i in range(26)]
        for idea in ideas:
            for j in range(ord('a'), ord('z')+1):
                item = chr(j) + idea[1:]
                if item not in ideasSet:
                    match[ord(idea[0]) - ord('a')][j - ord('a')] += 1
        for i in range(26):
            for j in range(26):
                result += match[i][j] * match[j][i]
        return result
        