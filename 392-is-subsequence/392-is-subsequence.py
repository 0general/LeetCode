class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        idx = 0
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx += 1
            if idx == len(s):
                return True
        return False