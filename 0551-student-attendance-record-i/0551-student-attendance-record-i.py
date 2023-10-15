class Solution:
    def checkRecord(self, s: str) -> bool:
        Atotal = 0
        for idx, c in enumerate(s):
            if c == 'A':
                Atotal += 1
            if idx >=2 and c == 'L' and s[idx-2:idx+1] == 'LLL':
                return False
            if Atotal >= 2: return False
        return True
        