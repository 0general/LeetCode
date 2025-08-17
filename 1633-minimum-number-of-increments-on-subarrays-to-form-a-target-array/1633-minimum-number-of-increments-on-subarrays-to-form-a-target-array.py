class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        prev = 0
        for x in target:
            if x > prev:
                ans += x - prev
            prev = x
        return ans