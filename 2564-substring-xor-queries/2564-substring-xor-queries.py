from collections import defaultdict

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/substring-xor-queries/discuss/5718477/Clean-Python-Beats-60
        n = defaultdict(list)
        for i in range(1, 31):
            for j in range(len(s) - i + 1):
                if s[j] == '1' or i==1:
                    if int(s[j:j + i], 2) not in n:
                        n[int(s[j:j + i], 2)] = [j, j + i-1]
        res = []
        for s, e in queries:
            if s ^ e in n:
                res.append(n[s^e])
            else:
                res.append([-1, -1])
        return res
        