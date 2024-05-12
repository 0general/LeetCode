from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        val = [i - int(str(i)[::-1]) for i in nums]
        ans = 0
        for i in [x for x in Counter(val).values() if x >= 2]:
            ans += math.comb(i, 2)
            ans %= mod
        return ans % mod