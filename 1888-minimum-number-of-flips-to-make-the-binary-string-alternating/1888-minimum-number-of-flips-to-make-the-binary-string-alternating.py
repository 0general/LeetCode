class Solution:
    def minFlips(self, s: str) -> int:
        # https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/discuss/2613715/Python-Fixed-Size-Sliding-Window-EXPLAINED
        minimumFlips = len(s)
        
        k = len(s)
        
        s = s if k % 2 == 0 else s + s
        
        altArr1, altArr2 = [], []        
        for i in range(len(s)):
            altArr1.append("0" if i % 2 == 0 else "1")
            altArr2.append("1" if i % 2 == 0 else "0")
            
        alt1 = "".join(altArr1)
        alt2 = "".join(altArr2)
        
        diff1, diff2 = 0,0
        
        # Sliding Window Template Begins
        i,j = 0,0
        
        while j < len(s):
            if s[j] != alt1[j] : diff1 += 1
            if s[j] != alt2[j] : diff2 += 1
                
            if j - i + 1 < k: j += 1
            else:
                minimumFlips = min(minimumFlips, diff1, diff2)
                if s[i] != alt1[i] : diff1 -= 1
                if s[i] != alt2[i] : diff2 -= 1
                i += 1
                j += 1
        
        return minimumFlips