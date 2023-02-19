class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        def all_sum(n):
            n %= mod
            return (n*(n+1)//2) % mod
        ans = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
                continue
            elif ones:
                ans += all_sum(ones)
                ans %= mod
                ones = 0
        if ones:
            ans += all_sum(ones)
            ans %= mod
        return ans
                
        
        