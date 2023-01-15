from collections import defaultdict
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        dic = defaultdict(int)
        target = 2**k
        num = 0
        for i in range(len(s)-k+1):
            if dic[s[i:i+k]] == 0:
                dic[s[i:i+k]] += 1
                num += 1
            if num == target:
                return True
        return False
