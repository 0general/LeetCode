class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sample = defaultdict(int)
        if len(s) < 10:
            return []
        for i in range(len(s)-9):
            sample[s[i:i+10]] += 1
        ans = []
        for key,value in sample.items():
            if value>1:
                ans.append(key)
        return ans
            