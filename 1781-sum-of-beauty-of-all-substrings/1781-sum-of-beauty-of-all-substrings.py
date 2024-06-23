from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
    
        for i in range(len(s) - 1):
            d = defaultdict(int)
            d[s[i]] += 1
            for j in range(i + 1, len(s)):
                d[s[j]] += 1
                ans += max(d.values()) - min(d.values())
        return ans
        