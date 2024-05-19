from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        targetCounter = Counter(target)
        sCounter = Counter(s)
        ans = len(s)
        for key, value in targetCounter.items():
            ans = min(ans, sCounter[key] // value)
        return ans
        