from collections import Counter
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        s_map = Counter(s)
        for idx, char in enumerate(s):
            if char not in s_map or char.swapcase() not in s_map:
                result1 = self.longestNiceSubstring(s[:idx])
                result2 = self.longestNiceSubstring(s[idx+1:])
                return result1 if len(result1) >= len(result2) else result2
        return s