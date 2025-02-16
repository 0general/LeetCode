class Solution:
    def reformat(self, s: str) -> str:
        a = []
        b = []
        for chr in s:
            if 'a' <= chr <= 'z':
                a.append(chr)
            else:
                b.append(chr)
        if len(a) < len(b):
            a, b = b, a
        ans = ""
        if len(a) - len(b) >= 2:
            return ans
        for i in range(len(s)):
            if i%2 == 0:
                ans += a[i//2]
            else:
                ans += b[i//2]
        return ans